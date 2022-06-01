from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello yall')

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())