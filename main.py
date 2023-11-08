#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   daily_arxiv.py
@Time    :   2021-10-29 22:34:09
@Author  :   Bingjie Yan
@Email   :   bj.yan.pa@qq.com
@License :   Apache License 2.0
"""

import json.decoder
import os.path
import shutil
import re

from gevent import monkey

monkey.patch_all()
import gevent
from gevent.queue import Queue
from datetime import datetime
import requests
import arxiv
import yaml
from  random import randint
# from  appblog_post_render import _OverloadTasks as _OverloadTasks_appblog
from fire import Fire

from config import (
    SERVER_PATH_TOPIC,
    SERVER_DIR_STORAGE,
    SERVER_PATH_README,
    SERVER_PATH_DOCS,
    SERVER_PATH_STORAGE_MD,
    SERVER_PATH_STORAGE_BACKUP,
    TIME_ZONE_CN,
    topic,
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
    def handle_html(url: str):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
        }
        proxies = {"http": None, "https": None}
        session = requests.session()
        response = session.get(url, headers=headers, proxies=proxies)
        try:
            data_ = response.json()
            return data_
        except json.decoder.JSONDecodeError as e:
            logger.error(e)
    @staticmethod
    def handle_md(url: str):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
        }
        proxies = {"http": None, "https": None}
        session = requests.session()
        response = session.get(url, headers=headers, proxies=proxies)
        try:
            data_ = response.text()
            return data_
        except Exception as e:
            logger.error(e)


class CoroutineSpeedup:
    """轻量化的协程控件"""

    def __init__(
            self,
            work_q: Queue = None,
            task_docker=None,
    ):
        # 任务容器：queue
        self.worker = work_q if work_q else Queue()
        self.channel = Queue()
        # 任务容器：迭代器
        self.task_docker = task_docker
        # 协程数
        self.power = 32
        # 任务队列满载时刻长度
        self.max_queue_size = 0

        self.cache_space = []

        self.max_results = 30

    def _adaptor(self):
        while not self.worker.empty():
            task: dict = self.worker.get_nowait()
            if task.get("pending"):
                self.runtime(context=task.get("pending"))
            elif task.get("response"):
                self.parse(context=task)

    def _progress(self):
        p = self.max_queue_size - self.worker.qsize() - self.power
        p = 0 if p < 1 else p
        return p

    def runtime(self, context: dict):
        keyword_ = context.get("keyword")
        # import arxivscraper.arxivscraper as ax
        # import pandas as pd
        
        # scraper = ax.Scraper(
        #     category="cs",
        #     date_from="2022-04-25",
        #     date_until="2022-04-26",
        #     t=10,
        #     filters={"abstract": ["healthcare", "medical", "hospital"]},
        # )
        # output = scraper.scrape()
        # cols = ("id", "title", "categories", "abstract", "doi", "created", "updated", "authors")
        # df = pd.DataFrame(output, columns=cols)
        res = arxiv.Search(
            query=keyword_,
            max_results=self.max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        ).results()

        context.update({"response": res, "hook": context})
        self.worker.put_nowait(context)


    def parse(self, context):
        base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
        _paper = {}
        arxiv_res = context.get("response")
        for result in arxiv_res:
#             beaware result is a https://github.com/lukasschwab/arxiv.py 
            attributes_and_methods = dir(result)


            paper_id = result.get_short_id()
            paper_title = result.title

            paper_url = result.entry_id
            paper_abstract= result.summary.strip().replace('\n',' ').replace('\r'," ")
            print(paper_abstract)
            code_url = base_url + paper_id
            paper_first_author = result.authors[0]

            publish_time = result.published.date()

            ver_pos = paper_id.find('v')
            paper_key = paper_id if ver_pos == -1 else paper_id[0:ver_pos]

            # 尝试获取仓库代码
            # ----------------------------------------------------------------------------------
            # Origin(r)
            # ----------------------------------------------------------------------------------
            # {
            #   'paper_url': 'https://',
            #   'official': {'url': 'https://github.com/nyu-wireless/mmwRobotNav'},
            #   'all_official': [{'url': 'https://github.com/nyu-wireless/mmwRobotNav'}],
            #   'unofficial_count': 0,
            #   'frameworks': [],
            #   'status': 'OK'
            # }
            # ----------------------------------------------------------------------------------
            # None(r)
            # ----------------------------------------------------------------------------------
            # {
            #   'paper_url': 'https://',
            #   'official': None,
            #   'all_official': [],
            #   'unofficial_count': 0,
            #   'frameworks': [],
            #   'status': 'OK'
            # }
            response = ToolBox.handle_html(code_url)
            official_ = response.get("official")
            repo_url = official_.get("url", "null") if official_ else "null"
            # ----------------------------------------------------------------------------------
            # 编排模型
            # ----------------------------------------------------------------------------------
            # IF repo
            #   |publish_time|paper_title|paper_first_author|[paper_id](paper_url)|`[link](url)|`paper_abstract``
            # ELSE
            #   |publish_time|paper_title|paper_first_author|[paper_id](paper_url)|`null`
            _paper.update({
                paper_key: {
                    "publish_time": publish_time,
                    "title": paper_title,
                    "authors": f"{paper_first_author} et.al.",
                    "id": paper_id,
                    "paper_url": paper_url,
                    "repo": repo_url,
                    "abstract" :paper_abstract
                },
            })
        self.channel.put_nowait({
            "paper": _paper,
            "topic": context["hook"]["topic"],
            "subtopic": context["hook"]["subtopic"],
            "fields": ["Publish Date", "Title", "Authors", "PDF", "Code","Abstract"]
        })
        logger.success(
            f"handle [{self.channel.qsize()}/{self.max_queue_size}]"
            f" | topic=`{context['topic']}` subtopic=`{context['hook']['subtopic']}`")

    def offload_tasks(self):
        if self.task_docker:
            for task in self.task_docker:
                self.worker.put_nowait({"pending": task})
        self.max_queue_size = self.worker.qsize()

    def overload_tasks(self):
        render_style='appleblog'
        if render_style=='appleblog':
            
            ot = _OverloadTasks()
        
        file_obj: dict = {}
        while not self.channel.empty():
            # 将上下文替换成 Markdown 语法文本
            context: dict = self.channel.get()
            md_obj: dict = ot.to_markdown(context)

            # 子主题分流
            if not file_obj.get(md_obj["hook"]):
                file_obj[md_obj["hook"]] = md_obj["hook"]
            file_obj[md_obj["hook"]] += md_obj["content"]

            # 生成 mkdocs 所需文件
            os.makedirs(os.path.join(SERVER_PATH_DOCS, f'{context["topic"]}'), exist_ok=True)
            with open(os.path.join(SERVER_PATH_DOCS, f'{context["topic"]}', f'{context["subtopic"]}.md'), 'w') as f:
                f.write(md_obj["content"])
               

        # 生成 Markdown 模板文件
        template_ = ot.generate_markdown_template(
            content="".join(list(file_obj.values())))
        # 存储 Markdown 模板文件
        ot.storage(template_, obj_="database")

        return template_

    def go(self, power: int):
        # 任务重载
        self.offload_tasks()
        # 配置弹性采集功率
        if self.max_queue_size != 0:
            self.power = self.max_queue_size if power > self.max_queue_size else power
        # 任务启动
        task_list = []
        for _ in range(self.power):
            task = gevent.spawn(self._adaptor)
            task_list.append(task)
        gevent.joinall(task_list)

class _OverloadTasks:
    def __init__(self):
        self._build()

        # yyyy-mm-dd
        self.update_time = ToolBox.log_date(mode="log")

        self.storage_path_by_date = SERVER_PATH_STORAGE_BACKUP.format(
            ToolBox.log_date('file'))
        self.storage_path_readme = SERVER_PATH_README
        self.storage_path_docs = SERVER_PATH_DOCS

    # -------------------
    # Private API
    # -------------------
    @staticmethod
    def _build():
        if not os.path.exists(SERVER_DIR_STORAGE):
            os.mkdir(SERVER_DIR_STORAGE)

    @staticmethod
    def _set_markdown_hyperlink(text, link):
        return f"[{text}]({link})"
    @staticmethod
    def _check_for_illegal_char(input_str):
        # remove illegal characters for Windows file names/paths 
        # (illegal filenames are a superset (41) of the illegal path names (36))
        # this is according to windows blacklist obtained with Powershell
        # from: https://stackoverflow.com/questions/1976007/what-characters-are-forbidden-in-windows-and-linux-directory-names/44750843#44750843
        #
        # PS> $enc = [system.Text.Encoding]::UTF8
        # PS> $FileNameInvalidChars = [System.IO.Path]::GetInvalidFileNameChars()
        # PS> $FileNameInvalidChars | foreach { $enc.GetBytes($_) } | Out-File -FilePath InvalidFileCharCodes.txt

        illegal = '\u0022\u003c\u003e\u007c\u0000\u0001\u0002\u0003\u0004\u0005\u0006\u0007\u0008' + \
                '\u0009\u000a\u000b\u000c\u000d\u000e\u000f\u0010\u0011\u0012\u0013\u0014\u0015' + \
                '\u0016\u0017\u0018\u0019\u001a\u001b\u001c\u001d\u001e\u001f\u003a\u002a\u003f\u005c\u002f' 

        output_str, _ = re.subn('['+illegal+']','_', input_str)
        output_str = output_str.replace('\\','_')   # backslash cannot be handled by regex
        output_str = output_str.replace('..','_')   # double dots are illegal too, or at least a bad idea 
        output_str = output_str[:-1] if output_str[-1] == '.' else output_str # can't have end of line '.'

        if output_str != input_str:
            print(f"The name '{input_str}' had invalid characters, "
                f"name was modified to '{output_str}'")

        return output_str
        
    def _generate_markdown_table_content(self, paper: dict,tags=None):
        paper['publish_time'] = f"**{paper['publish_time']}**"
        paper['title'] = f"**{paper['title']}**"
        _pdf = self._set_markdown_hyperlink(
            text=paper['id'], link=paper['paper_url'])
        _repo = self._set_markdown_hyperlink(
            text="link", link=paper['repo']) if "http" in paper['repo'] else "null"
        paper['abstract']=f"{paper['abstract']}"
        paper['keywords'] = list(set(tags))
        line = f"|{paper['publish_time']}" \
               f"|{paper['title']}" \
               f"|{paper['authors']}" \
               f"|{_pdf}" \
               f"|{_repo}" \
               f"|{paper['abstract']}|\n"
        print(':::',line)
        paper_contents= f"# title:{paper['title']} \r " \
                        f"## publish date: \r{paper['publish_time']} \r" \
                        f"## authors: \r  {paper['authors']} \r" \
                        f"## abstract: \r  {paper['abstract']} \r" 
                        # f"## {paper['summary']}"            
        #    gpt paper summary section
        postname=self._check_for_illegal_char(paper['title'])
        postname=postname.replace(' ','_')
        ## if filename start with __ ,astro post will 404
        if postname.startswith('__'):
            postname=postname.replace('__',"")
        paper_path_appleblog=SERVER_PATH_STORAGE_MD.format(postname)
        repo_url=os.getenv('repo')
        repo_name=repo_url.split('/')[-1].replace('-',' ')
        
        
        QA_md_link =f"https://github.com/taesiri/ArXivQA/blob/main/papers/{paper['id']}.md"
        paper['QA_md_contents']=ToolBox.handle_md(QA_md_link)
        if paper['QA_md_contents']==None:
            print('gen realtime')
            paper['QA_md_contents']='coming soon'
            # https://huggingface.co/spaces/taesiri/ClaudeReadsArxiv
            # https://github.com/Nipun1212/Claude_api
        paper_contents= f"---\n" \
        f"layout: '../../layouts/MarkdownPost.astro'\n" \
        f"title: '{paper['title'].replace('**','')}'\n" \
        f"pubDate: {str(datetime.now(TIME_ZONE_CN)).split('.')[0]}\n" \
        f"description: ''\n" \
        f"author: '{editor_name}'\n" \
        f"cover:\n" \
        f"    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'\n" \
        f"    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'\n" \
        f"    alt: 'cover'\n" \
        f"tags: {paper['keywords']} \n" \
        f"theme: 'light'\n" \
        f"featured: true\n" \
        f"\n" \
        f"meta:\n" \
        f" - name: author\n" \
        f"   content: {paper['authors']}\n" \
        f" - name: keywords\n" \
        f"   content: key3, key4\n" \
        f"\n" \
        f"keywords: key1, key2, key3\n" \
        f"---\n" \
        f"\n" \
        f"## paper id\n" \
        f"{paper['id']}\n" \
        f"## download\n" \
        f"{_pdf}\n" \
        f"## abstracts:\n" \
        f"{paper['abstract']}\n" \
        f"## QA:\n" \
        f"{paper['QA_md_contents']}\n" 
        
        
        
        # paper_contents= f"---\n" \
        # f"layout: '../../layouts/MarkdownPost.astro'\n" \
        # f"title: '{paper['title'].replace('**','')}'\n" \
        # f"pubDate: {str(datetime.now(TIME_ZONE_CN)).split('.')[0]}\n" \
        # f"description: 'Automated track arxiv-daily latest papers around {topic}'\n" \
        # f"author: 'wanghaisheng'\n" \
        # f"cover:\n" \
        # f"    url: '../../public/assets/{randint(1, 100)}.jpg'\n" \
        # f"    square: '../../public/assets/{randint(1, 100)}.jpg'\n" \
        # f"    alt: 'cover'\n" \
        # f"tags: ['brand','brand monitor']\n" \
        # f"theme: 'light'\n" \
        # f"featured: true\n" \
        # f"meta:\n" \
        # f" - name: author\n" \
        # f"   content: 作者是我\n" \
        # f" - name: keywords\n" \
        # f"   content: key3, key4\n" \
        # f"keywords: key1, key2, key3\n" \
        # f"---" \
        # f"\n" \
        # f"## authors:\r{paper['authors']} \r" \
        # f"## publish_time:\r{paper['publish_time']} \r" \
        # f"## abstract:\r{paper['abstract']}\n"

        with open(paper_path_appleblog, "w", encoding="utf8") as f:
                f.write(paper_contents)      


        return line

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


class Scaffold:
    def __init__(self):
        pass

    @staticmethod
    @logger.catch()
    def run(env: str = "development", power: int = 16):
        """
        Start the test sample.

        Usage: python daily_arxiv.py run
        or: python daily_arxiv.py run --env=production  生产环境下运行

        @param power:  synergy power. The recommended value interval is [2,16].The default value is 37.
        @param env: Optional with [development production]
        @return:
        """
        # Get tasks
        context = ToolBox.get_yaml_data()

        # Set tasks
        pending_atomic = [{"subtopic": subtopic, "keyword": keyword.replace('"', ""), "topic": topic}
                          for topic, subtopics in context.items() for subtopic, keyword in subtopics.items()]

        # Offload tasks
        booster = CoroutineSpeedup(task_docker=pending_atomic)
        booster.go(power=power)

        # Overload tasks
        template_ = booster.overload_tasks()

        # Replace project README file.
        if env == "production":
            with open(SERVER_PATH_README, "w", encoding="utf8") as f:
                for i in template_:
                    f.write(i)
            
            shutil.copyfile(SERVER_PATH_README, os.path.join(SERVER_PATH_DOCS, "index.md"))

if __name__ == "__main__":
    
    Fire(Scaffold)
