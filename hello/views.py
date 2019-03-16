from django.shortcuts import render
from django.http import HttpResponse    # http 模块

# 请求响应函数
def hello(request):
    return HttpResponse('Hello,world')