# organasition --> moatafaKhaled

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from github import Github

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('TOKEN')
repoName = "ml"

g = Github(TOKEN)
organization = g.get_organization('moatafaKhaled')
repo = organization.create_repo(repoName, 'test script')
repoUrl = repo.html_url
print(repoUrl)
# #
# git add Readme.md
# git commit -m "frist commit"
# git remote add "%myvar%"
# git push -u origin master
