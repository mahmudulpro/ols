from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<center><h1>Welcome To OLS</h1></center>")
    

