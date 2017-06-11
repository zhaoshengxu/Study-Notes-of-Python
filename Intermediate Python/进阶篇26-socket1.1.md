# 老王Python学习笔记
> 运行环境：代码编辑器sublime text 3（配置anaconda，python3.5）
## 二、进阶篇

### 进阶篇26-socket1.1

#### 1. 两种通讯协议：udp, tcp/ip
- tcp/ip：确保消息传达到位，有握手，有验证，相对而言比较安全，性能相对没有那么好，如
- udp：只管将信息传出，不确保能否到位，相对安全性较差，性能较好。
> socket大部分时间就是用作进程之间的通讯

#### 2. netcat小技巧(Unix)
建立基于tcp/ip的服务端、客户端，比如两人的简单聊天室
```
# 分别在Linux中打开两个terminal
# 1. 服务端
nc -l 1234 # 生成一个服务端聊天窗口

# 2. 客户端
nc localhost 1234 # 生成一个服务端聊天窗口

# 联通之后即可相互对话
```
#### 3. socket服务端/客户端

##### 3.1 创建socket对象socket.socket(arg1, arg2)
- arg1: AF_INET（基于IP的通讯）或AF_UNIX（本地基于文件的通讯）
- arg2: SOCK_STREAM（tcp/ip）或者SOCK_DGRAM（udp）
##### 3.2 绑定端口 socket.bind(('localhost', 8888))
参数是一个元组，两个参数分别是IP和端口号

##### 3.3 socket.lisen(n)
n代表允许多少个同时请求

##### 3.4 connection,address = socket.accept()
将接收到的元组数据分别赋值给connection,address

##### 3.5 buf = connection.recv(10)
接收长度为10个字节的消息

##### 3.6 connection.send(buf)
测试通讯是否建立

##### 3.7 socket.close()
关闭通讯

```
# coding=utf-8

# 用socket创建服务端(while语句，需要单独关闭socket)
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(10)
while 1:
    connection, address = s.accept()
    print('connected by: ', address)
    buf = connection.recv(1024)
    connection.send(buf)
s.close()

# 用socket创建服务端(with语句，无需单独关闭socket)
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.3', 1234))
    s.listen(10)
    connection, address = s.accept()
    print('connected by: ', address)
    re = connection.recv(1024)
    connection.send(b'all is well')
    print('received: ', re)


# 用socket创建客户端(with语句，无需单独关闭socket)
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.3', 1234))
    s.sendall(b'hello world')
    data = s.recv(1024)
    print('received: ', data)

``` 

### 作业
1. socket创建服务端，接收数据之后，返回相同值，以测试通讯是否成功建立。为什么只有在第一次会返回值，而接下来则不会重复出现？


---
2. 用建立了一个客户端，与服务端联通
```
# coding=utf-8
# 用socket创建服务端(with语句，无需单独关闭socket)
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.3', 1234))
    s.listen(10)
    connection, address = s.accept()
    print('connected by: ', address)
    re = connection.recv(1024)
    connection.send(b'all is well')
    print('received: ', re)


# 用socket创建客户端(with语句，无需单独关闭socket)
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.3', 1234))
    s.sendall(b'hello world')
    data = s.recv(1024)
    print('received: ', data)

```
