#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   daily_arxiv.py
@Time    :   2021-10-29 22:34:09
@Author  :   wanghaisheng
@Email   :   edwin_uestc@163.com
@License :   Apache License 2.0
"""

import json
import os
import shutil
import re
import aiohttp
import asyncio
from datetime import datetime
import arxiv
import yaml
from random import randint
import unicodedata
from config import (
    SERVER_PATH_TOPIC,
    SERVER_DIR_STORAGE,
    SERVER_PATH_README,
    SERVER_PATH_DOCS,
    SERVER_PATH_STORAGE_MD,
    SERVER_PATH_STORAGE_BACKUP,
    TIME_ZONE_CN,
    topic,
    render_style,
    editor_name,
    logger
)

class ToolBox:
    @staticmethod
    def log_date(mode="log"):
        if mode == "log":
            return str(datetime.now(TIME_ZONE_CN)).split(".")[0]
        elif mode == "file":
            return str(datetime.now(TIME_ZONE_CN)).split(" ")[0]

    @staticmethod
    def get_yaml_data() -> dict:
        with open(SERVER_PATH_TOPIC, "r", encoding="utf8") as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
        print("YAML Data:", data)
        return data

    @staticmethod
    async def handle_html(session, url: str):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
        }
        async with session.get(url, headers=headers) as response:
            try:
                data_ = await response.json()
                return data_
            except json.JSONDecodeError as e:
                logger.error(f"JSON decode error: {e}")
                return None

    @staticmethod
    async def handle_md(session, url: str):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
        }
        async with session.get(url, headers=headers) as response:
            try:
                data_ = await response.text()
                return data_
            except Exception as e:
                logger.error(f"Error fetching MD content: {e}")
                return None

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
                        task = await self.worker.get()
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
        if len(list(arxiv_res))==0:
            print('no respomsr data')
            # return
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
            context: dict = await self.channel.get()
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

class _OverloadTasks:
    def __init__(self):
        self.update_time = ToolBox.log_date()
        self.storage_path_by_date = os.path.join(SERVER_DIR_STORAGE, self.update_time)
        self.storage_path_docs = SERVER_PATH_DOCS
        self.storage_path_readme = SERVER_PATH_README
    def _generate_yaml_front_matter(self, paper: dict, editor_name: str) -> str:
        post_title = paper["title"]
        post_pubdate = str(datetime.now(TIME_ZONE_CN)).split('.')[0]
        post_tags = paper['keywords']
    
        front_matter = {
            "layout": "../../layouts/MarkdownPost.astro",
            "title": post_title,
            "pubDate": post_pubdate,
            "description": "",
            "author": editor_name,
            "cover": {
                "url": "https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg",
                "square": "https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg",
                "alt": "cover"
            },
            "tags": post_tags,
            "theme": "light",
            "featured": True,
            "meta": [
                {"name": "author", "content": paper['authors']},
                {"name": "keywords", "content": "key3, key4"}
            ],
            "keywords": "key1, key2, key3"
        }
    
        yaml_front_matter = yaml.safe_dump(front_matter, default_flow_style=False)
    
        return f"---\n{yaml_front_matter}---\n"
    def _generate_markdown_content(self, paper: dict, pdf_link: str) -> str:
        markdown_content = (
            f"# title: {paper['title']} \n"
            f"## publish date: \n{paper['publish_time']} \n"
            f"## authors: \n  {paper['authors']} \n"
            f"## paper id\n"
            f"{paper['id']}\n"
            f"## download\n"
            f"{pdf_link}\n"
            f"## abstracts:\n"
            f"{paper['abstract']}\n"
            f"## QA:\n"
            f"{paper['QA_md_contents']}\n"
        )

        return markdown_content

    def _generate_markdown_table_content(self, paper: dict,tags=None):
        # Formatting fields
        paper['publish_time'] = f"**{paper['publish_time']}**"
        # paper['title'] = f"**{paper['title']}"
        if not paper['keywords']:
            if not tags:
                paper['keywords'] = list(set(tags))
            
        QA_md_link =f"https://github.com/taesiri/ArXivQA/blob/main/papers/{paper['id']}.md"
        paper['QA_md_contents']=ToolBox.handle_md(QA_md_link)
        if paper['QA_md_contents']==None:
            print('gen realtime')
            paper['QA_md_contents']='coming soon'
            # https://huggingface.co/spaces/taesiri/ClaudeReadsArxiv
            # https://github.com/Nipun1212/Claude_api        
        pdf_link = self._set_markdown_hyperlink(text=paper['id'], link=paper['paper_url'])

        # Generate YAML front matter
        yaml_front_matter = self._generate_yaml_front_matter(paper, editor_name)

        # Generate Markdown content
        markdown_content = self._generate_markdown_content(paper, pdf_link)

        paper_contents= f"{yaml_front_matter}\n{markdown_content}"
        postname=self._check_for_illegal_char(paper['title'])
        postname=postname.replace(' ','_')
        ## if filename start with __ ,astro post will 404
        if postname.startswith('__'):
            postname=postname.replace('__',"")
        paper_path_appleblog=SERVER_PATH_STORAGE_MD.format(postname)
        repo_url=os.getenv('repo')
        repo_name=repo_url.split('/')[-1].replace('-',' ')        
        if not os.path.exists(SERVER_DIR_STORAGE):
            os.makedirs(SERVER_DIR_STORAGE)
            print(f"Directory '{SERVER_DIR_STORAGE}' was created.")
        else:
            print(f"Directory '{SERVER_DIR_STORAGE}' already exists.")

        with open(paper_path_appleblog, "w", encoding="utf8") as f:
                f.write(paper_contents)      
        
        if os.path.exists(SERVER_DIR_STORAGE.dirname()+'/tags.json'):
            old=json.load(open(SERVER_DIR_STORAGE.dirname()+'/tags.json'),encoding='utf8').get('tags',[])
            new=old+            paper['keywords'] + list(set(tags))
            new=list(set(new))
        else:
            data={}
            new=           paper['keywords'] + list(set(tags))

            new=list(set(new))

            data['tags']=new

            with open('data.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            


    @staticmethod
    def _set_style_to(style: str = "center"):
        return " :---: " if style == "center" else " --- "

    # -------------------
    # Public API
    # -------------------
    def storage(self, template: str, obj_: str = "database"):
        """
        将 Markdown 模板存档
        @param template:
        @param obj_: database:将 Markdown 模板存档至 database/store 中。其他值，替换根目录下的 README
        @return:
        """
        path_factory = {
            'database': self.storage_path_by_date,
            'readme': self.storage_path_readme,
            'docs': self.storage_path_docs
        }
        if obj_ not in path_factory.keys():
            path_ = path_factory['readme']
        else:
            path_ = path_factory[obj_]
        with open(path_, "w", encoding="utf8") as f:
            for i in template:
                f.write(i)

    def generate_markdown_template(self, content: str):


        
        repo_url=os.getenv('repo')
        repo_name=repo_url.split('/')[-1].replace('-',' ')
        print('-====,',repo_url)
        repo_url="https://github.com/"+repo_url

        _project = f"# arxiv-daily latest papers around {repo_name}\n"
        _pin = f"Automated deployment @ {self.update_time} Asia/Shanghai\n"
        _tos = f"> Welcome to contribute! Add your topics and keywords in " \
               f"[`topic.yml`]({repo_url}/blob/main/database/topic.yml).\n"
        _tos += f"> You can also view historical data through the " \
                f"[storage]({repo_url}/blob/main/database/storage).\n"

        _form = _project + _pin + _tos + content

        return _form

    def to_markdown(self, context: dict) -> dict:
        _fields = context["fields"]
        _topic = context["topic"]
        _subtopic = context["subtopic"]
        _paper_obj = context["paper"]

        _topic_md = f"\n## {_topic}\n"
        _subtopic_md = f"\n### {_subtopic}\n"
        _fields_md = f"|{'|'.join(_fields)}|\n"
        _style_md = f"|{'|'.join([self._set_style_to('center') for _ in range(len(_fields))])}|\n"
        table_lines = "".join([self._generate_markdown_table_content(
            paper,tags=[_topic,_subtopic]) for paper in _paper_obj.values()])

        _content_md = _subtopic_md + _fields_md + _style_md + table_lines

        return {"hook": _topic_md, "content": _content_md}

    def generate_markdown_template(self, content):
        # Mock implementation of generate_markdown_template
        return f"# Daily ArXiv Updates\n\n{content}"

    def storage(self, content, obj_=""):
        if not os.path.exists(self.storage_path_by_date):
            os.makedirs(self.storage_path_by_date)

        # Save markdown content
        with open(os.path.join(self.storage_path_by_date, f"updates_{self.update_time}.md"), "w", encoding="utf8") as f:
            f.write(content)

        # Save readme if it doesn't exist
        if not os.path.exists(self.storage_path_readme):
            with open(self.storage_path_readme, "w", encoding="utf8") as f:
                f.write(f"# Daily Updates\n\nUpdates saved in {self.storage_path_by_date}\n")

        # Copy latest updates to docs directory
        shutil.copytree(self.storage_path_by_date, self.storage_path_docs, dirs_exist_ok=True)

async def main():
    toolbox = ToolBox()
    context = toolbox.get_yaml_data()
    # example_task = {"keyword": "machine learning"}
        # Set tasks
    pending_atomic = [{"subtopic": subtopic, "keyword": keyword.replace('"', ""), "topic": topic}
                          for topic, subtopics in context.items() for subtopic, keyword in subtopics.items()]
    cs = CoroutineSpeedup(task_docker=pending_atomic)
    print('start to convert  to md')
    await cs.go(power=1)  # Using power=1 for simplicity

if __name__ == "__main__":
    asyncio.run(main())
