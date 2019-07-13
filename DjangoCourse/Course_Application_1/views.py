from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    insertion_variable = {'insert_me': 'I am inserted dynamically, as I was not part of hard coded HTML'}
    return render(request, 'Course_Application_1/index.html', context=insertion_variable)