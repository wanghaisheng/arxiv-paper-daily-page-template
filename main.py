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
                if self.worker.empty():
                    print("Worker queue is empty. Waiting...")
                    await asyncio.sleep(1)  # Sleep to prevent tight loop
                else:
                    task: dict = await self.worker.get()
                    print(f"Got task: {task}")
                    if task.get("pending"):
                        print("Handling pending task...")
                        await self.runtime(context=task.get("pending"))
                    elif task.get("response"):
                        print("Handling response task...")
                        await self.parse(context=task)
                if self.worker.empty() and self.channel.empty():
                    break
            print("Adaptor loop completed.")
        except Exception as e:
            print(f"Error in _adaptor: {e}")

    def _progress(self):
        p = self.max_queue_size - self.worker.qsize() - self.power
        p = 0 if p < 1 else p
        return p

    async def runtime(self, context: dict):
        keyword_ = context.get("keyword")
        print(f"Searching for keyword: {keyword_}")
        try:
            res = arxiv.Search(
                query="ti:"+keyword_+"+OR+abs:"+keyword_,
                max_results=self.max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate
            ).results()
            print(f"Query results: {list(res)}")
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

    def to_markdown(self, context):
        # Mock implementation of to_markdown
        return {
            "hook": context["topic"],
            "content": f"# {context['topic']} - {context['subtopic']}\n\n" +
                       f"**Publish Time:** {context['paper']['publish_time']}\n" +
                       f"**Title:** {context['paper']['title']}\n" +
                       f"**Authors:** {context['paper']['authors']}\n" +
                       f"**PDF Link:** {context['paper']['paper_url']}\n" +
                       f"**Code Repo:** {context['paper']['repo']}\n" +
                       f"**Abstract:** {context['paper']['abstract']}\n"
        }

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
    await cs.go(power=1)  # Using power=1 for simplicity

if __name__ == "__main__":
    asyncio.run(main())
