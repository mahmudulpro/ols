from django.urls import path
from django.conf.urls import url
from snippets import views


urlpatterns = [
    url(r'^$', views.SnippetList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]
