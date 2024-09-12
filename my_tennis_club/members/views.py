
# Create your views here.

from django.http import HttpResponse
from django.template import loader

def members(request):
    return HttpResponse("Hello world!")

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def signin(request):
    template = loader.get_template('signin.html')
    return HttpResponse(template.render())