import json
import requests


class SearchRepo():
    
    NUMBER_OF_REPOS = 5
    
    def __init__(self, search_term):
        self.search_term = search_term

    def get_from_github(self):
        response = requests.get(('https://api.github.com/search/repositories?q={}').format(self.search_term))
        #get repos from request
        resp_dict = json.loads(response.content)
        #get items only and order by created_at desc
        resp_dict['items'] = sorted(resp_dict['items'], key=lambda x:x['created_at'], reverse=True)
        #slice to NUMBER_OF_REPOS
        repos = resp_dict['items'][:self.NUMBER_OF_REPOS]
        return repos