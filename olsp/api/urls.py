from django.urls import path
from django.conf.urls import url
from api import views


urlpatterns=[
	url(r'^$', views.QuestionList.as_view()),
]