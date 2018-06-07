from django.urls import path
from django.conf.urls import url
from api import views 

app_name = 'api'
urlpatterns=[
	
	path('', views.QuestionList.as_view(), name='index'),
	path('profile/', views.ProfileList.as_view(), name='profile'),
]
