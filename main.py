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
import re
import aiohttp
import asyncio
from datetime import datetime
import arxiv
import yaml
import unicodedata
from config import (
    SERVER_PATH_TOPIC,
    SERVER_DIR_STORAGE,
    SERVER_PATH_README,
    SERVER_PATH_DOCS,
    SERVER_PATH_STORAGE_MD,
    SERVER_PATH_STORAGE_BACKUP,
    TIME_ZONE_CN,
    editor_name,
    logger
)

class ToolBox:
    @staticmethod
    def log_date(mode="log"):
        now = datetime.now(TIME_ZONE_CN)
        return now.strftime("%Y-%m-%d") if mode == "file" else now.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_yaml_data() -> dict:
        with open(SERVER_PATH_TOPIC, "r", encoding="utf8") as f:
            return yaml.safe_load(f)

    @staticmethod
    async def fetch_data(session, url: str, data_type: str):
        headers = {"user-agent": "Mozilla/5.0"}
        async with session.get(url, headers=headers) as response:
            return await response.json() if data_type == 'json' else await response.text()

class CoroutineSpeedup:
    def __init__(self, work_q: asyncio.Queue = None, task_docker=None):
        self.worker = work_q or asyncio.Queue()
        self.channel = asyncio.Queue()
        self.task_docker = task_docker
        self.power = 32
        self.max_queue_size = 0
        self.max_results = 2000

    async def _adaptor(self):
        while not self.worker.empty():
            task = await self.worker.get()
            if "pending" in task:
                await self.runtime(task["pending"])
            elif "response" in task:
                await self.parse(task)

    async def runtime(self, context: dict):
        keyword = context.get("keyword")
        results = arxiv.Search(
            query=f"ti:{keyword} OR abs:{keyword}",
            max_results=self.max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        ).results()

        context.update({"response": results, "hook": context})
        await self.worker.put(context)

    @staticmethod
    def clean_title(title):
        title = unicodedata.normalize('NFKD', title)
        title = re.sub(r'[^\w\s]', '', title)
        return title.strip()

    async def parse(self, context):
        base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
        papers = context.get("response")
        async with aiohttp.ClientSession() as session:
            paper_data = {}
            for result in papers:
                paper_id = result.get_short_id()
                title = self.clean_title(result.title)
                paper_url = result.entry_id
                abstract = result.summary.strip().replace('\n', ' ').replace('\r', " ")
                code_url = base_url + paper_id
                first_author = result.authors[0]
                publish_time = result.published.date()
                paper_key = paper_id.split('v')[0]

                response = await ToolBox.fetch_data(session, code_url, 'json')
                repo_url = response.get("official", {}).get("url", "null") if response else "null"
                
                paper_data[paper_key] = {
                    "publish_time": publish_time,
                    "title": title,
                    "authors": f"{first_author} et.al.",
                    "id": paper_id,
                    "paper_url": paper_url,
                    "repo": repo_url,
                    "abstract": abstract
                }
                
        await self.channel.put({
            "paper": paper_data,
            "topic": context["hook"]["topic"],
            "subtopic": context["hook"]["subtopic"],
            "fields": ["Publish Date", "Title", "Authors", "PDF", "Code", "Abstract"]
        })
        logger.success(
            f"Handled [{self.channel.qsize()}/{self.max_queue_size}]"
            f" | topic=`{context['topic']}` subtopic=`{context['hook']['subtopic']}`")

    def offload_tasks(self):
        if self.task_docker:
            for task in self.task_docker:
                self.worker.put_nowait({"pending": task})
        self.max_queue_size = self.worker.qsize()

    async def overload_tasks(self):
        ot = _OverloadTasks()
        file_data = {}
        while not self.channel.empty():
            context = await self.channel.get()
            md_content = ot.to_markdown(context)

            if md_content["hook"] not in file_data:
                file_data[md_content["hook"]] = md_content["content"]
            else:
                file_data[md_content["hook"]] += md_content["content"]

            os.makedirs(os.path.join(SERVER_PATH_DOCS, context["topic"]), exist_ok=True)
            with open(os.path.join(SERVER_PATH_DOCS, context["topic"], f'{context["subtopic"]}.md'), 'w') as f:
                f.write(md_content["content"])

            template = ot.generate_markdown_template("".join(file_data.values()))
            ot.storage(template, obj_="database")

        return template

    async def go(self, power: int):
        self.offload_tasks()
        self.power = min(self.max_queue_size, power) if self.max_queue_size != 0 else power
        tasks = [asyncio.create_task(self._adaptor()) for _ in range(self.power)]
        await asyncio.gather(*tasks)

class _OverloadTasks:
    def __init__(self):
        self.update_time = ToolBox.log_date("log")
        self.storage_path_by_date = SERVER_PATH_STORAGE_BACKUP.format(ToolBox.log_date('file'))
        self.storage_path_docs = SERVER_PATH_DOCS
        os.makedirs(SERVER_DIR_STORAGE, exist_ok=True)

    @staticmethod
    def _set_markdown_hyperlink(text, link):
        return f"[{text}]({link})"

    @staticmethod
    def _check_illegal_chars(input_str):
        illegal_chars = '\u0022\u003c\u003e\u007c\u0000-\u001f\u003a\u002a\u003f\u005c\u002f'
        return re.sub(f'[{illegal_chars}]', '_', input_str).replace('\\', '_').replace('..', '_').strip('_')

    def _generate_yaml_front_matter(self, paper) -> str:
        front_matter = {
            "layout": "../../layouts/MarkdownPost.astro",
            "title": paper["title"],
            "pubDate": self.update_time,
            "author": editor_name,
            "cover": {
                "url": "https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg",
                "alt": "cover"
            },
            "tags": paper.get('keywords', []),
            "meta": [
                {"name": "author", "content": paper['authors']},
                {"name": "keywords", "content": "key3, key4"}
            ]
        }
        return f"---\n{yaml.safe_dump(front_matter, default_flow_style=False)}---\n"

    def _generate_markdown_content(self, paper, pdf_link) -> str:
        return (
            f"# Title: {paper['title']}\n"
            f"## Publish Date: {paper['publish_time']}\n"
            f"## Authors: {paper['authors']}\n"
            f"## Paper ID: {paper['id']}\n"
            f"## Download: {pdf_link}\n"
            f"## Abstract: {paper['abstract']}\n"
            f"## QA: {paper.get('QA_md_contents', 'coming soon')}\n"
        )

    def _generate_markdown_table_content(self, paper):
        pdf_link = self._set_markdown_hyperlink(paper['id'], paper['paper_url'])
        yaml_front_matter = self._generate_yaml_front_matter(paper)
        markdown_content = self._generate_markdown_content(paper, pdf_link)
        content = f"{yaml_front_matter}\n{markdown_content}"
        postname = self._check_illegal_chars(paper['title']).replace(' ', '_')
        postname = postname.lstrip('_')

        paper_path = SERVER_PATH_STORAGE_MD.format(postname)
        with open(paper_path, "w", encoding="utf8") as f:
            f.write(content)

        tags_path = os.path.join(SERVER_DIR_STORAGE, 'tags.json')
        if os.path.exists(tags_path):
            with open(tags_path, 'r', encoding='utf8') as f:
                data = json.load(f)
            tags = list(set(data.get('tags', []) + paper['keywords']))
        else:
            tags = paper['keywords']

        with open(tags_path, 'w', encoding='utf-8') as f:
            json.dump({"tags": tags}, f, ensure_ascii=False, indent=2)

    def to_markdown(self, context) -> dict:
        fields = context["fields"]
        topic = context["topic"]
        subtopic = context["subtopic"]
        papers = context["paper"]

        table_lines = "".join([self._generate_markdown_table_content(paper) for paper in papers.values()])
        content = f"\n### {subtopic}\n|{'|'.join(fields)}|\n|{'|'.join(['center' for _ in fields])}|\n{table_lines}"
        return {"hook": f"\n## {topic}\n", "content": content}

    def generate_markdown_template(self, content):
        return f"# Arxiv Daily Update\n\n{content}"

    def storage(self, content, obj_):
        path = self.storage_path_by_date if obj_ == "database" else self.storage_path_docs
        file_path = os.path.join(path, f"{self.update_time}.md")
        with open(file_path, "w") as f:
            f.write(content)

async def main():
    toolbox = ToolBox()
    data = toolbox.get_yaml_data()

    cs = CoroutineSpeedup()
    await cs.go(power=10)

if __name__ == "__main__":
    asyncio.run(main())
