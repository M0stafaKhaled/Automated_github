from github import Github
g = Github("M0stafaKhaled", "24235258m")
repos = g.get_user().get_repos()

for repo in repos:
    print(repo.name)
