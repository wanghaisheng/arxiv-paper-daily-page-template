import os
from os.path import dirname, join, abspath
from sys import platform

import pytz
from loguru import logger


# 定位项目根目录
SERVER_DIR_PROJECT = dirname(__file__) if "win" in platform else abspath(".")

SERVER_PATH_README = join(SERVER_DIR_PROJECT, "mkdocs/README.md")

SERVER_PATH_DOCS = join(SERVER_DIR_PROJECT, "mkdocs/docs")

os.makedirs(SERVER_PATH_DOCS, exist_ok=True)

editor_name='wanghaisheng'

site_name='smart watch latest research evidence'
# 风格选择
render_style1='weekly'
render_style2='appleblog'
render_style3='mkdocs'
render_style='appleblog'
#风格博文数据库 目录根



# 文件数据库 目录根


# ##mkdocs style
# SERVER_DIR_DATABASE = join(SERVER_DIR_PROJECT, "database")

# SERVER_DIR_STORAGE = join(SERVER_DIR_DATABASE, "storage")

# SERVER_PATH_STORAGE_MD = join(SERVER_DIR_STORAGE, "storage_{}.md")

# appleblog style

SERVER_DIR_DATABASE = join(SERVER_DIR_PROJECT, "appleblog/src/pages")

SERVER_DIR_STORAGE = join(SERVER_DIR_DATABASE, "posts")

SERVER_PATH_STORAGE_MD = join(SERVER_DIR_STORAGE, "{}.md")

SERVER_PATH_STORAGE_BACKUP = join("database", "backup/{}.md")

# weekly style

# SERVER_DIR_DATABASE = join(SERVER_DIR_PROJECT, "weekly/src/pages")

# SERVER_DIR_STORAGE = join(SERVER_DIR_DATABASE, "posts")

# SERVER_PATH_STORAGE_MD = join(SERVER_DIR_STORAGE, "{}.md")


topic="brand,brand monitor"



SERVER_PATH_TOPIC = join("database", "topic.yml")

# 服务器日志文件路径
SERVER_DIR_DATABASE_LOG = join(SERVER_DIR_DATABASE, "logs")
logger.add(
    join(SERVER_DIR_DATABASE_LOG, "runtime.log"),
    level="DEBUG",
    rotation="1 day",
    retention="20 days",
    encoding="utf8",
)
logger.add(
    join(SERVER_DIR_DATABASE_LOG, "error.log"),
    level="ERROR",
    rotation="1 week",
    encoding="utf8",
)

# 时区
TIME_ZONE_CN = pytz.timezone("Asia/Shanghai")
TIME_ZONE_NY = pytz.timezone("America/New_York")
