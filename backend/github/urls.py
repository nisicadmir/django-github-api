from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import Index

urlpatterns = [
    url(r'^q', Index.as_view(), name='index'),
     url(r'^.*$', RedirectView.as_view(url='q', permanent=False), name='index2')
]