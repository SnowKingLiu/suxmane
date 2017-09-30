from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def hello(request):
    return HttpResponse("Hello world ! ")

