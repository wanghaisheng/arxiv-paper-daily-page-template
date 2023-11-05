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

def json_to_appleblog_post_md(filename, to_web=False):
    """
    @param filename: str
    @return None
    """
    # ---
    # layout: '../../layouts/MarkdownPost.astro'
    # title: 'Apple 推出新款 HomePod，带来突破性音质与智能体验'
    # pubDate: 2035-03-25
    # description: '呈现出类拔萃的音质、增强的 Siri 功能以及安全放心的智能家居体验'
    # author: 'Apple Newsroom'
    # cover:
    #     url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    #     square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    #     alt: 'cover'
    # tags: ["新闻稿", "Apple", "HomePod"] 
    # theme: 'light'
    # featured: true
    
    # meta:
    #  - name: author
    #    content: 作者是我
    #  - name: keywords
    #    content: key3, key4
    
    # keywords: key1, key2, key3
    # ---
    DateNow = datetime.date.today()
    DateNow = str(DateNow)
    DateNow = DateNow.replace('-', '.')
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
