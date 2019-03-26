'''
除去注释部分代码，Django运行会报错
'''

from django.http import HttpResponse, JsonResponse
from gdbEntry import GdbDemo
import os

def start(request):
    print(request)
    gdbCon = gdbEntry.GdbDemo()
    ret = gdbCon.start()
    print(ret)
    retMsg = {
        'code': 0,
        'message': 'success',
    }
    return JsonResponse(retMsg)    # 返回一个json
