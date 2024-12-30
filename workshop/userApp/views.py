from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def wel(request):
	return HttpResponse("<h1>welcome to project"</h1>)

def demo(request):
	return HttpResponse("welcome to college")

def style(request):
	return HttpResponse("<h1 style='background-color:blue;color:pink'>welcome to college</h1")

def login(request):
	return HttpResponse("<input type='submit' value='submit'>")