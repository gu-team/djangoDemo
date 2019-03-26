# -*- coding:utf-8 -*-
from socket import *
from django.http import HttpResponse, JsonResponse
import os

HOST='localhost'
PORT=8001
BUFSIZ=1024
ADDR=(HOST,PORT)

def start(request):
    print('web request is:' + request)

    tcp_client_socket = socket(AF_INET,SOCK_STREAM)
    tcp_client_socket.connect(ADDR)
    while True:
        data = input('>')
        if not data:
            break
        tcp_client_socket.send(data)
        data = tcp_client_socket.recv(BUFSIZ)
        if not data:
            break
        print(data)
    tcp_client_socket.close()

    retMsg = {
        'code': 0,
        'message': 'success',
    }
    return JsonResponse(retMsg)    # 返回一个json