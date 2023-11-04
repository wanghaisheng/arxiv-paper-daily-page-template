##apple blog style post markdown converter
import datetime
import requests
import json
import arxiv
import os
import shutil
import yaml
import time
import random
def sort_papers(papers):
    output = dict()
    keys = list(papers.keys())
    keys.sort(reverse=True)
    for key in keys:
        output[key] = papers[key]
    return output

def json_to_md(filename, to_web=False):
    """
    @param filename: str
    @return None
    """

    DateNow = datetime.date.today()
    DateNow = str(DateNow)
    DateNow = DateNow.replace('-', '.')

    with open(filename, "r") as f:
        content = f.read()
        if not content:
            data = {}
        else:
            data = json.loads(content)

    if to_web == False:
        md_filename = "README.md"
        # clean README.md if daily already exist else create it
        with open(md_filename, "w+") as f:
            pass

        # write data into README.md
        with open(md_filename, "a+") as f:

            f.write("## Updated on " + DateNow + "\n\n")

            f.write(
                "> Welcome to contribute! Add your topics and keywords in `topic.yml`\n\n")

            for topic in data.keys():
                f.write("## " + topic + "\n\n")
                for subtopic in data[topic].keys():
                    day_content = data[topic][subtopic]
                    if not day_content:
                        continue
                    # the head of each part
                    f.write(f"### {subtopic}\n\n")

                    f.write("|Publish Date|Title|Authors|PDF|Code|Abstract|\n" +
                            "|---|---|---|---|---|---|\n")

                    # sort papers by date
                    day_content = sort_papers(day_content)

                    for _, v in day_content.items():
                        if v is not None:
                            f.write(v)

                    f.write(f"\n")
    else:
        if os.path.exists('docs'):
            shutil.rmtree('docs')
        if not os.path.isdir('docs'):
            os.mkdir('docs')

        shutil.copyfile('README.md', os.path.join('docs', 'index.md'))

        for topic in data.keys():
            os.makedirs(os.path.join('docs', topic), exist_ok=True)
            md_indexname = os.path.join('docs', topic, "index.md")
            with open(md_indexname, "w+") as f:
                f.write(f"# {topic}\n\n")

            # print(f'web {topic}')

            for subtopic in data[topic].keys():
                md_filename = os.path.join('docs', topic, f"{subtopic}.md")
                # print(f'web {subtopic}')

                # clean README.md if daily already exist else create it
                with open(md_filename, "w+") as f:
                    pass

                with open(md_filename, "a+") as f:
                    day_content = data[topic][subtopic]
                    if not day_content:
                        continue
                    # the head of each part
                    f.write(f"# {subtopic}\n\n")
                    f.write("| Publish Date | Title | Authors | PDF | Code | Abstract |\n")
                    f.write(
                        "|:---------|:-----------------------|:---------|:------|:------|:------|\n")

                    # sort papers by date
                    day_content = sort_papers(day_content)

                    for _, v in day_content.items():
                        if v is not None:
                            f.write(v)

                    f.write(f"\n")

                with open(md_indexname, "a+") as f:
                    day_content = data[topic][subtopic]
                    if not day_content:
                        continue
                    # the head of each part
                    f.write(f"## {subtopic}\n\n")
                    f.write("| Publish Date | Title | Authors | PDF | Code | Abstract |\n")
                    f.write(
                        "|:---------|:-----------------------|:---------|:------|:------|:------|\n")

                    # sort papers by date
                    day_content = sort_papers(day_content)

                    for _, v in day_content.items():
                        if v is not None:
                            f.write(v)

                    f.write(f"\n")

    print("finished")