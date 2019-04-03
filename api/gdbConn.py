# -*- coding:utf-8 -*-
from socket import *
from django.http import HttpResponse, JsonResponse
import os

HOST='localhost'
PORT=8001
BUFSIZ=1024

def start(request):
    # 创建一个socket对象，AF_INET指定使用IPv4协议(AF_INET6代表IPV6)，SOCK_STREAM指定使用面向流的TCP协议
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect((HOST, PORT)) # 连接gdb服务器

    command = 'start'
    tcp_client_socket.send(command.encode('utf-8')) 	# 将字符串进行字节编码，并发送出去
    resp = tcp_client_socket.recv(BUFSIZ)			# 接受服务器返回的字节
    resp_str = resp.decode('utf-8')				# 对字节进行解码
    print('response--->' + resp_str)
    tcp_client_socket.close()

    retMsg = {
        'code': 0,
        'message': resp_str,
    }
    return JsonResponse(retMsg)    # 返回一个json

def contin(request):
    # 创建一个socket对象，AF_INET指定使用IPv4协议(AF_INET6代表IPV6)，SOCK_STREAM指定使用面向流的TCP协议
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect((HOST, PORT)) # 连接gdb服务器

    command = 'continue'
    tcp_client_socket.send(command.encode('utf-8')) 	# 将字符串进行字节编码，并发送出去
    resp = tcp_client_socket.recv(BUFSIZ)			# 接受服务器返回的字节
    resp_str = resp.decode('utf-8')				# 对字节进行解码
    print('response--->' + resp_str)
    tcp_client_socket.close()

    retMsg = {
        'code': 0,
        'message': resp_str,
    }
    return JsonResponse(retMsg)    # 返回一个json
