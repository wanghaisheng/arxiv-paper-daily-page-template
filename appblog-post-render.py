class _OverloadTasks:
    def __init__(self):
        self._build()

        # yyyy-mm-dd
        self.update_time = ToolBox.log_date(mode="log")

        self.storage_path_by_date = SERVER_PATH_STORAGE_MD.format(
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

    def _generate_markdown_table_content(self, paper: dict):
        paper['publish_time'] = f"**{paper['publish_time']}**"
        paper['title'] = f"**{paper['title']}**"
        _pdf = self._set_markdown_hyperlink(
            text=paper['id'], link=paper['paper_url'])
        _repo = self._set_markdown_hyperlink(
            text="link", link=paper['repo']) if "http" in paper['repo'] else "null"
        paper['abstract']=f"{paper['abstract']}"
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
        paper_path_weekly=SERVER_PATH_STORAGE_PAPER_MD_weekly.format(paper['id'])
        with open(paper_path_weekly, "w", encoding="utf8") as f:
                f.write(paper_contents)        
        paper_path_appleblog=SERVER_PATH_STORAGE_PAPER_MD_appleblog.format(paper['id'])
        repo_url=os.getenv('repo')
        repo_name=repo_url.split('/')[-1].replace('-',' ')
        paper_contents= f"---\n" \
        f"layout: '../../layouts/MarkdownPost.astro'\n" \
        f"title: '{paper['title'].replace('**','')}'\n" \
        f"pubDate: {str(datetime.now(TIME_ZONE_CN)).split('.')[0]}\n" \
        f"description: 'Automated track arxiv-daily latest papers around {topic}'\n" \
        f"author: 'wanghaisheng'\n" \
        f"cover:\n" \
        f"    url: '../../public/assets/{randint(1, 100)}.jpg'\n" \
        f"    square: '../../public/assets/{randint(1, 100)}.jpg'\n" \
        f"    alt: 'cover'\n" \
        f"tags: ['brand','brand monitor']\n" \
        f"theme: 'light'\n" \
        f"featured: true\n" \
        f"meta:\n" \
        f" - name: author\n" \
        f"   content: 作者是我\n" \
        f" - name: keywords\n" \
        f"   content: key3, key4\n" \
        f"keywords: key1, key2, key3\n" \
        f"---" \
        f"\n" \
        f"## authors:\r{paper['authors']} \r" \
        f"## publish_time:\r{paper['publish_time']} \r" \
        f"## abstract:\r{paper['abstract']}\n"

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

    def to_appleblog_post_markdown(self, context: dict) -> dict:
        _fields = context["fields"]
        _topic = context["topic"]
        _subtopic = context["subtopic"]
        _paper_obj = context["paper"]

        _topic_md = f"\n## {_topic}\n"
        _subtopic_md = f"\n### {_subtopic}\n"
        _fields_md = f"|{'|'.join(_fields)}|\n"
        _style_md = f"|{'|'.join([self._set_style_to('center') for _ in range(len(_fields))])}|\n"
        table_lines = "".join([self._generate_markdown_table_content(
            paper) for paper in _paper_obj.values()])

        _content_md = _subtopic_md + _fields_md + _style_md + table_lines

        return {"hook": _topic_md, "content": _content_md}
