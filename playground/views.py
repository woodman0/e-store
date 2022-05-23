from django.shortcuts import render
from django.http import HttpResponse

#request and response

def sayHello(request):
    return HttpResponse('Hello world')