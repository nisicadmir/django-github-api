from django.shortcuts import render
from django.views import View

from .getRepos import SearchRepo
from .getCommits import SearchCommit

class Index(View):
    
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        search_term = self.request.GET.get('search_term', None)
        if search_term == '':
            context = {
                'search_term': search_term,
                'data': None,
            }
            #returns empty page
            return render(request, self.template_name, context)
        else:
            repos = SearchRepo(search_term).get_from_github()
            commits = SearchCommit(repos).get_from_github()
            data = zip(repos, commits)
        context = {
            'search_term': search_term,
            'data': data,
        }
        #return page with data and search_term
        return render(request, self.template_name, context)