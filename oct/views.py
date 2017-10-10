# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect


# 第二版
def index(request):
    return render(request, 'index.html')


def hello(request):
    return HttpResponse("Hello world ! ")


# 第一版
def index_v1(request):
    return render(request, 'index_v1.html')

