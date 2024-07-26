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
        print(data)
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
                logger.error(e)

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
                logger.error(e)

class CoroutineSpeedup:
    def __init__(self, work_q: asyncio.Queue = None, task_docker=None):
        self.worker = work_q if work_q else asyncio.Queue()
        self.channel = asyncio.Queue()
        self.task_docker = task_docker
        self.power = 32
        self.max_queue_size = 0
        self.cache_space = []
        self.max_results = 2000

    async def _adaptor(self):
        print("Starting _adaptor...")

        while not self.worker.empty():
            task: dict = await self.worker.get()
            print(f"Processing task: {task}")  # Debugging

            if task.get("pending"):
                await self.runtime(context=task.get("pending"))
            elif task.get("response"):
                await self.parse(context=task)

    def _progress(self):
        p = self.max_queue_size - self.worker.qsize() - self.power
        p = 0 if p < 1 else p
        return p

    async def runtime(self, context: dict):
        keyword_ = context.get("keyword")
        print(f"Searching for keyword: {keyword_}")
        
        res = arxiv.Search(
            query="ti:"+keyword_+"+OR+abs:"+keyword_,
            max_results=self.max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        ).results()
        print(f"Query results: {list(res)}")

        context.update({"response": res, "hook": context})
        await self.worker.put(context)

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
                print(f"Response for paper ID {paper_id}: {response}")

                response = await ToolBox.handle_html(session, code_url)
                official_ = response.get("official")
                repo_url = official_.get("url", "null") if official_ else "null"
                
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
            with open(os.path.join(SERVER_PATH_DOCS, f'{context["topic"]}', f'{context["subtopic"]}.md'), 'w') as f:
                f.write(md_obj["content"])

            template_ = ot.generate_markdown_template("".join(list(file_obj.values())))
            ot.storage(template_, obj_="database")

        return template_

    async def go(self, power: int):
        self.offload_tasks()
        if self.max_queue_size != 0:
            self.power = self.max_queue_size if power > self.max_queue_size else power
        print(f"Creating {self.power} tasks.")

        tasks = [asyncio.create_task(self._adaptor()) for _ in range(self.power)]
        await asyncio.gather(*tasks)

class _OverloadTasks:
    def __init__(self):
        self._build()
        self.update_time = ToolBox.log_date(mode="log")
        self.storage_path_by_date = SERVER_PATH_STORAGE_BACKUP.format(ToolBox.log_date('file'))
        self.storage_path_readme = SERVER_PATH_README
        self.storage_path_docs = SERVER_PATH_DOCS

    @staticmethod
    def _build():
        if not os.path.exists(SERVER_DIR_STORAGE):
            os.mkdir(SERVER_DIR_STORAGE)

    @staticmethod
    def _set_markdown_hyperlink(text, link):
        return f"[{text}]({link})"

    @staticmethod
    def _check_for_illegal_char(input_str):
        illegal = '\u0022\u003c\u003e\u007c\u0000\u0001\u0002\u0003\u0004\u0005\u0006\u0007\u0008' + \
                '\u0009\u000a\u000b\u000c\u000d\u000e\u000f\u0010\u0011\u0012\u0013\u0014\u0015' + \
                '\u0016\u0017\u0018\u0019\u001a\u001b\u001c\u001d\u001e\u001f\u003a\u002a\u003f\u005c\u002f'
        output_str, _ = re.subn('[' + illegal + ']', '_', input_str)
        output_str = output_str.replace('\\', '_')
        output_str = output_str.replace('..', '_')
        output_str = output_str[:-1] if output_str[-1] == '.' else output_str
        return output_str

    import yaml
    
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
        template = f"# Arxiv Daily Update\n\n{content}"
        return template

    def storage(self, content, obj_):
        path = self.storage_path_by_date if obj_ == "database" else self.storage_path_docs
        file_path = os.path.join(path, f"{self.update_time}.md")
        with open(file_path, "w") as f:
            f.write(content)

async def main():
    toolbox = ToolBox()
    data = toolbox.get_yaml_data()

    cs = CoroutineSpeedup()
    tasks = [asyncio.create_task(cs.go(power=10)) for _ in range(1)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
