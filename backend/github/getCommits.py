import json
import requests


class SearchCommit():
    
    def __init__(self, repos):
        self.repos = repos

    def get_from_github(self):
        commits = []
        for repo in self.repos:
            response = requests.get(('https://api.github.com/repos/{}/{}/commits').format(repo['owner']['login'], repo['name']))
            #get all commits
            all_commits = json.loads(response.content)
            #slice to one last commmit
            one_commit = all_commits[:1]
            #append to commits
            commits.append(one_commit[0])
        return commits
