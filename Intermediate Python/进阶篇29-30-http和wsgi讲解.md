# 老王Python学习笔记
> 运行环境：
>- VirtualBox4.8.0 /Ubuntu16.04.1 /x86_64(Python2.7)
>- 代码编辑器sublime text 3
## 二、进阶篇

### 进阶篇29-30-http和wsgi相关讲解
用python写一个服务器server

#### 1. 服务器的重要性

- 客户端/服务器(c/s)
- 网页端/服务器(b/s)包含但不限于如网站、服务器脚本之类
无论是客户端还是网页端，都离不开服务器。

#### 2. 简单介绍服务器

```
# php示例
<?
echo phpinfo();
?>
```
php仅有3行代码，足见php相对比较简单。之所以简单，这是因为底层很多东西被掩藏或者已经被处理好，开发者只需要关注业务逻辑即可。

web应用，基于HTTP协议（HTTP协议又基于TCP协议）。HTTP协议是基于请求的，常用是GET和POST。换句话说，web应用本质上时基于请求的。

以浏览器为例，web应用可以分解为以下几个过程：
0. 用户向浏览器发送一个请求（如网址）

1. 浏览器向服务器发送一个HTTP请求；

2. 服务器收到请求，生成一个HTML文档；

3. 服务器把HTML文档作为HTTP响应的Body发送给浏览器；

4. 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

#### 3. WSGI
Python Web Server Gateway Interface（Python Web服务器网关接口），缩写为WSGI。WSGI是Python应用程序或框架和Web服务器之间的一种接口，已经被广泛接受，它已基本达成它的可移植性方面的目标。

WSGI 没有官方的实现，因为WSGI更像一个协议。遵照该协议的WSGI应用(Application)可以在任何服务器(Server)上运行。
（参见百度词条[wsgi](http://baike.baidu.com/link?url=nEcbaJpCo3_GIc1aAL2K7hft5aeIfDLggDTh-Mcr3xOZEAw8DoPidGEIbQnqqTzE53F0TOhr_MapQCyQJ0oqka)）

#### 4. Python包：wsgiref
wsgiref包是一个用于测试、验证和简单部署的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。
示例可参考：[廖雪峰的官方网站：WSGI接口](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832689740b04430a98f614b6da89da2157ea3efe2000)

在ubuntu终端运行以下代码，感受一下wsgiref自带的一个简单服务器示例运行效果：
```
cd /usr/lib/python2.7/wsgiref  #更改工作目录至wsgiref
ls -l  # 找到文件simple_server.py，一个简单服务器示例
python simple_server.py  # 运行该文件，默认浏览器弹出运行结果
```
为了能够实现作业中功能要求的简单服务器，最快速的方法就是基于wsgiref自带的这个简单服务器（simple_server.py），经过探索和改进得到自己的服务器。具体步骤如下：
> 编写代码实现某功能的快速方法，就是基于系统文档，或者在前人的工作的基础上，进行改写，先实现功能，然后再去消化吸收其中的细节。

- 1. 从simple_server.py文件中摘录出主体内容，并新建下面的first_app.py文件，在终端运行结果和simple_server.py相同；

```
# coding=utf-8
from wsgiref.simple_server import make_server

def demo_app(environ, start_response):
    'Web应用程序的WSGI处理函数'
    from StringIO import StringIO
    stdout = StringIO()
    print >>stdout, "Hello world!"
    print >>stdout
    h = environ.items()
    h.sort()
    for k, v in h:
        print >>stdout, k, '=', repr(v)
    start_response("200 OK", [('Content-Type', 'text/plain')])
    return [stdout.getvalue()]

if __name__ == '__main__':
    # 创建服务器，IP地址为空，端口是8000，加载函数demo_app
    # 如果8000端口已被其他程序占用，启动将失败，请修改成其他端口
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    import webbrowser
    webbrowser.open('http://localhost:8000/xyz?abc')
    httpd.handle_request()  # serve one request, then exit
    httpd.server_close()
```

- 2. 探索和改写
> 遇到不懂的代码，积极使用help()和dir()以及借助百度谷歌
改写完成的代码如下(即为本次作业)：
```
# coding=utf-8
'''
要求：
利用WSGI编写服务器实现以下功能：
1. 输入网址http://localhost:8000 输出hello world
2. 输入网址http://localhost:8000/name 输出hello name
'''
from wsgiref.simple_server import make_server

def demo_app(environ, start_response):
    '''
    Web应用程序的WSGI处理函数
    @environ: 环境设置字典，即为上述wsgiref包自带的简单服务器的输出结果（不包括Hello world!），下面会解释每一个参数的含义。
    '''
    start_response("200 OK", [('Content-Type', 'text/plain')])
    # 取出输入网址端口号的字符串，如果没有输出字符串world
    return "hello %s" % (environ['PATH_INFO'][1:] or 'world') 

if __name__ == '__main__':
    '''
    创建服务器，IP地址为空，端口是8000，加载函数demo_app
    如果8000端口已被其他程序占用，启动将失败，请修改成其他端口
    '''
    httpd = make_server('', 8003, demo_app)
    sa = httpd.socket.getsockname()  # 获取服务器的IP地址和端口号
    print "Serving HTTP on", sa[0], "port", sa[1] # 提示需要输入的服务器的IP地址和端口号
    httpd.serve_forever() # 开始监听HTTP请求
```
#### 5. envirn变量
envirn变量，是环境设置字典，即为上述wsgiref包自带的简单服务器的输出结果（不包括Hello world!）。其中，下面添加注释的environ变量是environ环境设置字典必须有的，其含义和名称与CGI脚本中使用的一样，不过，最后以wsgi开头的几个变量是特定于WSGI的变量。

```
CLUTTER_BACKEND = 'x11'
CLUTTER_IM_MODULE = 'xim'
COLORTERM = 'xfce4-terminal'
CONTENT_LENGTH = ''  # 传入数据的长度
CONTENT_TYPE = 'text/plain'  # 查询数据的类型
DBUS_SESSION_BUS_ADDRESS = 'unix:abstract=/tmp/dbus-N2YE4pbYUM'
DEFAULTS_PATH = '/usr/share/gconf/xubuntu.default.path'
DESKTOP_SESSION = 'xubuntu'
DISPLAY = ':0.0'
GATEWAY_INTERFACE = 'CGI/1.1'
GDMSESSION = 'xubuntu'
GDM_LANG = 'en_US'
GLADE_CATALOG_PATH = ':'
GLADE_MODULE_PATH = ':'
GLADE_PIXMAP_PATH = ':'
GNOME_KEYRING_CONTROL = ''
GNOME_KEYRING_PID = ''
GPG_AGENT_INFO = '/home/zsx/.gnupg/S.gpg-agent:0:1'
GTK_IM_MODULE = 'fcitx'
GTK_OVERLAY_SCROLLING = '0'
HOME = '/home/zsx'
# 客户端接收的MIME类型
HTTP_ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
HTTP_ACCEPT_ENCODING = 'gzip, deflate'  
HTTP_ACCEPT_LANGUAGE = 'en-US,en;q=0.5'
HTTP_CONNECTION = 'keep-alive'
HTTP_HOST = 'localhost:8000'
HTTP_UPGRADE_INSECURE_REQUESTS = '1'
# 客户段浏览器
HTTP_USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
IM_CONFIG_PHASE = '1'
INSTANCE = ''
JOB = 'dbus'
LANG = 'en_US.UTF-8'
LANGUAGE = 'en_US:en'
LC_ADDRESS = 'zh_CN.UTF-8'
LC_IDENTIFICATION = 'zh_CN.UTF-8'
LC_MEASUREMENT = 'zh_CN.UTF-8'
LC_MONETARY = 'zh_CN.UTF-8'
LC_NAME = 'zh_CN.UTF-8'
LC_NUMERIC = 'zh_CN.UTF-8'
LC_PAPER = 'zh_CN.UTF-8'
LC_TELEPHONE = 'zh_CN.UTF-8'
LC_TIME = 'zh_CN.UTF-8'
LESSCLOSE = '/usr/bin/lesspipe %s %s'
LESSOPEN = '| /usr/bin/lesspipe %s'
LOGNAME = 'zsx'
LS_COLORS = 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01; ...'
MANDATORY_PATH = '/usr/share/gconf/xubuntu.mandatory.path'
OLDPWD = '/home/zsx/code'
PAPERSIZE = 'a4'
PATH = '/home/zsx/bin:/home/zsx/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
PATH_INFO = '/xyz'  # 传递的其他路径信息，即网页地址后面的name等
PWD = '/usr/lib/python2.7/wsgiref'
QT4_IM_MODULE = 'fcitx'
QT_ACCESSIBILITY = '1'
QT_IM_MODULE = 'fcitx'
QT_LINUX_ACCESSIBILITY_ALWAYS_ON = '1'
QT_STYLE_OVERRIDE = 'gtk'
QUERY_STRING = 'abc'  # 查询字符串
REMOTE_ADDR = '127.0.0.1'
REMOTE_HOST = 'localhost'
REQUEST_METHOD = 'GET' 请求的方法（常用GET or POST）
SCRIPT_NAME = ''  # 程序名称
SERVER_NAME = 'zsx-VirtualBox'  # 服务器主机名
SERVER_PORT = '8000'  #服务器端口号
SERVER_PROTOCOL = 'HTTP/1.1'  # 服务器协议
SERVER_SOFTWARE = 'WSGIServer/0.1 Python/2.7.12'
SESSION = 'xubuntu'
SESSIONTYPE = ''
SESSION_MANAGER = 'local/zsx-VirtualBox:@/tmp/.ICE-unix/1486,unix/zsx-VirtualBox:/tmp/.ICE-unix/1486'
SHELL = '/bin/bash'
SHLVL = '1'
SSH_AUTH_SOCK = '/run/user/1000/keyring/ssh'
TERM = 'xterm'
UPSTART_EVENTS = 'started xsession'
UPSTART_INSTANCE = ''
UPSTART_JOB = 'startxfce4'
UPSTART_SESSION = 'unix:abstract=/com/ubuntu/upstart-session/1000/1254'
USER = 'zsx'
WINDOWID = '79691780'
XAUTHORITY = '/home/zsx/.Xauthority'
XDG_CONFIG_DIRS = '/etc/xdg/xdg-xubuntu:/usr/share/upstart/xdg:/etc/xdg:/etc/xdg'
XDG_CURRENT_DESKTOP = 'XFCE'
XDG_DATA_DIRS = '/usr/share/xubuntu:/usr/share/xfce4:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop:/usr/share'
XDG_GREETER_DATA_DIR = '/var/lib/lightdm-data/zsx'
XDG_MENU_PREFIX = 'xfce-'
XDG_RUNTIME_DIR = '/run/user/1000'
XDG_SEAT = 'seat0'
XDG_SEAT_PATH = '/org/freedesktop/DisplayManager/Seat0'
XDG_SESSION_DESKTOP = 'xubuntu'
XDG_SESSION_ID = 'c2'
XDG_SESSION_PATH = '/org/freedesktop/DisplayManager/Session0'
XDG_SESSION_TYPE = 'x11'
XDG_VTNR = '7'
XMODIFIERS = '@im=fcitx'
_ = '/usr/bin/python'
# 以文本模式打开的类文件对象，用于写入错误的输出
wsgi.errors = <open file '<stderr>', mode 'w' at 0x7fd0189111e0>
wsgi.file_wrapper = <class wsgiref.util.FileWrapper at 0x7fd016703668>
# 表示输入流的类文件对象。表单数据或上传数据等其他数据都是从这里读取的。
wsgi.input = <socket._fileobject object at 0x7fd016833050>
wsgi.multiprocess = False  # 布尔标志，如果应用程序能够被另外一个进程并发执行，则为True
wsgi.multithread = True  # 布尔标志，如果应用程序可以被同一进程内的另外一个线程并发执行，则为True
wsgi.run_once = False  # 布尔标志，如果应用程序在执行过程的整个生命周期中只能执行一次，则为True
wsgi.url_scheme = 'http' # 表示url模式组件的字符串，如http或https
wsgi.version = (1, 0)  # 表示WSGI版本的元组，(1, 0)表示WSGI 1.0
```

