# 老王Python学习笔记
> 运行环境：
>- VirtualBox4.8.0 /Ubuntu16.04.1 /x86_64(Python2.7)
>- 代码编辑器sublime text 3
## 二、进阶篇

### 进阶篇29-http相关讲解
用python写一个服务器server

#### 1. 服务器

客户端/服务器(c/s)
无论是PC

网页端/服务器(b/s)
包含但不限于如网站、服务器脚本之类


#### 2. 以[php]为例简单介绍服务器是什么

```
<?

echo phpinfo();

?>

# php足够简单，是因为底层很多东西被掩藏或者已经被处理好，开发者只需要关注业务逻辑即可
```

web应用，基于HTTP协议，HTTP协议基于TCP协议

HTTP协议是基于请求的，常用是GET和POST。换句话说，web应用本质上时基于请求的。

以浏览器为例
0. 用户向浏览器发送一个请求（如网址）

1. 浏览器向服务器发送一个HTTP请求；

2. 服务器收到请求，生成一个HTML文档；

3. 服务器把HTML文档作为HTTP响应的Body发送给浏览器；

4. 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

#### 3. WSGI及Python的wsgiref包
PythonWeb服务器网关接口（Python Web Server Gateway Interface，缩写为WSGI)是Python应用程序或框架和Web服务器之间的一种接口，已经被广泛接受，它已基本达成它的可移植性方面的目标。

WSGI 没有官方的实现, 因为WSGI更像一个协议。只要遵照这些协议,WSGI应用(Application)都可以在任何服务器(Server)上运行, 反之亦然。
参见百度词条[wsgi](http://baike.baidu.com/link?url=nEcbaJpCo3_GIc1aAL2K7hft5aeIfDLggDTh-Mcr3xOZEAw8DoPidGEIbQnqqTzE53F0TOhr_MapQCyQJ0oqka)

wsgiref包是一个用于测试、验证和简单部署的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。
示例可参考：[廖雪峰的官方网站：WSGI接口](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832689740b04430a98f614b6da89da2157ea3efe2000)
---

### 作业

利用WSGI编写服务器实现以下功能：
1. 输入网址http://localhost:8000 输出hello world
2. 输入网址http://localhost:8000/name 输出hello name

```
# coding=utf-8
from wsgiref.simple_server import make_server

def my_app(environ, start_response):
    '''
    Web应用程序的WSGI处理函数
    实现以下功能：
    1. 输入网址http://localhost:8000 输出hello world
    2. 输入网址http://localhost:8000/name 输出hello name
    '''
    start_response("200 OK", [('Content_type', 'text/plain')])
    return 'Hello %s' % (environ['PATH_INFO'][1:] or 'World')

# 创建服务器，IP地址为空，端口是8000，加载函数my_app
# 如果8000端口已被其他程序占用，启动将失败，请修改成其他端口
serv = make_server('', 8000, my_app)
print('Serving HTTP on port 8000, input Website in Brower')  # 提示输入网址
serv.serve_forever()  # 开始监听HTTP请求
```