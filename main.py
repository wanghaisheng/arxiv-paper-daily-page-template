import asyncio
import arxiv
import aiohttp
import re
import unicodedata
from typing import List, Dict, Optional

class CoroutineSpeedup:
    def __init__(self, work_q: asyncio.Queue = None, task_docker=None):
        self.worker = work_q if work_q else asyncio.Queue()
        self.channel = asyncio.Queue()
        self.task_docker = task_docker
        self.power = 32
        self.max_queue_size = 0
        self.cache_space = []
        self.max_results = 20

    async def _adaptor(self):
        try:
            print("Starting _adaptor...")
            while True:
                # Check if both queues are empty
                if self.worker.empty() and self.channel.empty():
                    print("Both worker and channel queues are empty. Breaking loop...")
                    break
    
                # Check for pending tasks in worker queue
                if not self.worker.empty():
                    try:
                        task = await asyncio.wait_for(self.worker.get(), timeout=10)  # 10 seconds timeout
                        print(f"Got task: {task}")
    
                        if task.get("pending"):
                            print("Handling pending task...")
                            await self.runtime(context=task.get("pending"))
                        elif task.get("response"):
                            print("Handling response task...")
                            await self.parse(context=task)
                        else:
                            print("Unexpected task format:", task)
                    except asyncio.QueueEmpty:
                        print("Queue was empty when trying to fetch a task. Continuing...")
                        continue
                    except asyncio.TimeoutError:
                        print("Timeout occurred while waiting for a task.")
                    except Exception as e:
                        print(f"Error processing task: {e}")
    
                # Debugging output for queue statuses
                print(f"Worker queue size: {self.worker.qsize()}")
                print(f"Channel queue size: {self.channel.qsize()}")
    
            print("Adaptor loop completed.")
        except Exception as e:
            print(f"Error in _adaptor: {e}")

    def _progress(self):
        p = self.max_queue_size - self.worker.qsize() - self.power
        p = 0 if p < 1 else p
        return p

    async def runtime(self, context: dict):
        keyword_ = context.get("keyword").lower()
        print(f"Searching for keyword: {keyword_}")
        try:
            res = arxiv.Search(
                query="ti:"+keyword_+"+OR+abs:"+keyword_,
                max_results=self.max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate
            ).results()
            print(f"Query results: {len(list(res))}")
            context.update({"response": res, "hook": context})
            await self.worker.put(context)
        except Exception as e:
            print(f"Error during arXiv query: {e}")

    @staticmethod
    def clean_paper_title(title):
        normalized_title = unicodedata.normalize('NFKD', title)
        cleaned_title = re.sub(r'[^\w\s]', '', normalized_title)
        cleaned_title = re.sub(r'\s+', ' ', cleaned_title)
        cleaned_title = cleaned_title.strip()
        return cleaned_title

    async def parse(self, context):
        base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
        _paper = {}
        arxiv_res = context.get("response")
        if len(list(arxiv_res)) == 0:
            print('No response data')
            return

        async with aiohttp.ClientSession() as session:
            for result in arxiv_res:
                paper_id = result.get_short_id()
                paper_title = self.clean_paper_title(result.title)
                paper_url = result.entry_id
                paper_abstract = result.summary.strip().replace('\n', ' ').replace('\r', " ")
                code_url = base_url + paper_id
                paper_first_author = result.authors[0]
                publish_time = result.published.date()
                ver_pos = paper_id.find('v')
                paper_key = paper_id if ver_pos == -1 else paper_id[0:ver_pos]
                print(f"Processing paper ID {paper_id}...")

                response = await ToolBox.handle_html(session, code_url)
                if response:
                    official_ = response.get("official")
                    repo_url = official_.get("url", "null") if official_ else "null"
                else:
                    repo_url = "null"

                _paper.update({
                    paper_key: {
                        "publish_time": publish_time,
                        "title": paper_title,
                        "authors": f"{paper_first_author} et.al.",
                        "id": paper_id,
                        "paper_url": paper_url,
                        "repo": repo_url,
                        "abstract": paper_abstract
                    },
                })
        await self.channel.put({
            "paper": _paper,
            "topic": context["hook"]["topic"],
            "subtopic": context["hook"]["subtopic"],
            "fields": ["Publish Date", "Title", "Authors", "PDF", "Code", "Abstract"]
        })
        logger.success(
            f"handle [{self.channel.qsize()}/{self.max_queue_size}]"
            f" | topic=`{context['topic']}` subtopic=`{context['hook']['subtopic']}`")

    def offload_tasks(self):
        if self.task_docker:
            for task in self.task_docker:
                print(f"Offloading task: {task}")
                self.worker.put_nowait({"pending": task})
        self.max_queue_size = self.worker.qsize()
        print(f"Queue size after offloading tasks: {self.max_queue_size}")

    async def overload_tasks(self):
        ot = _OverloadTasks()
        file_obj: dict = {}
        while not self.channel.empty():
            print('==')
            context: dict = await asyncio.wait_for(self.channel.get(), timeout=10)  # 10 seconds timeout
            md_obj: dict = ot.to_markdown(context)
            print('json2md')

            if not file_obj.get(md_obj["hook"]):
                file_obj[md_obj["hook"]] = md_obj["hook"]
            file_obj[md_obj["hook"]] += md_obj["content"]

            os.makedirs(os.path.join(SERVER_PATH_DOCS, f'{context["topic"]}'), exist_ok=True)
            with open(os.path.join(SERVER_PATH_DOCS, f'{context["topic"]}', f'{md_obj["hook"]}.md'), "w",
                      encoding="utf8") as f:
                f.write(md_obj["content"])

        if file_obj:
            for key, val in file_obj.items():
                path = os.path.join(SERVER_PATH_DOCS, f"{key}.md")
                with open(path, "w", encoding="utf8") as f:
                    f.write(val)

        ot.storage(
            content=ot.generate_markdown_template(file_obj),
            obj_="Update"
        )

    async def go(self, power: int = 1):
        self.power = power
        self.offload_tasks()
        self.max_queue_size = self.worker.qsize()
        await asyncio.gather(*(self._adaptor() for _ in range(self.power)))
        await self.overload_tasks()
