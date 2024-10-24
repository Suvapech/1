from django.http import HttpResponse
from django.shortcuts import render

def list_projects(request):
    return HttpResponse("This is the List Projects page")

def add_project(request):
    return HttpResponse("This is the Add Project page")

def user_registration(request):
    return HttpResponse("This is the User Registration page")

def app_project(request):
    return HttpResponse("This is the App Project page")

def hello(request):
    return HttpResponse("Hello, world!")
