# -*- coding:utf-8 -*-
from socket import *
from django.http import HttpResponse, JsonResponse
import os

HOST='localhost'
PORT=8001
BUFSIZ=1024
ADDR=(HOST,PORT)

def start(request):
    print(request)

    # 创建一个socket对象，AF_INET指定使用IPv4协议(AF_INET6代表IPV6)，SOCK_STREAM指定使用面向流的TCP协议
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect(ADDR) # 连接gdb服务器

    data = 'hello, i am django'
    tcp_client_socket.send(data.encode('utf-8')) 	# 将字符串进行字节编码，并发送出去
    data = tcp_client_socket.recv(BUFSIZ)					# 接受服务器返回的字节
    data_str = data.decode('utf-8')								# 对字节进行解码
    print(data_str)

    retMsg = {
        'code': 0,
        'message': 'success',
    }
    return JsonResponse(retMsg)    # 返回一个json
