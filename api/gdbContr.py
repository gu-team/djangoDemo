'''
除去注释部分代码，Django运行会报错
'''

from django.http import HttpResponse, JsonResponse
# from . import gdbDemo
# import os

def start(request):
    print(request)
    # os.system(r'echo "source ./gdbDemo.py" >> ~/.gdbinit')
    # os.system('gdb')
    # gdbCon = gdbDemo.GdbDemo()
    # ret = gdbCon.start()
    retMsg = {
        'code': 0,
        'message': 'success'
    }
    return JsonResponse(retMsg)    # 返回一个json