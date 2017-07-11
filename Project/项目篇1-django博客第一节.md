# 老王Python学习笔记
> 运行环境：
>- VirtualBox4.8.0 /Ubuntu16.04.1 /x86_64(Python2.7)
>- 代码编辑器sublime text 3
## 三、项目篇

### 项目篇1-django博客第一节：扫盲

#### 0. 沙盒环境搭建及使用
> 参考资料：[Python 之 沙盒环境--virtualenv ](http://blog.csdn.net/vip_wangsai/article/details/52139035)

```
"1.安装virtualenv"
sudo easy_install virtualenv

"2.创建沙盒环境"
virtualenv <envname>

"3.进入沙盒环境"
source  <envname>/bin/avtivate

"4.安装所需的包"
pip install <pkgname>

"5.退出沙盒环境"
deactuvate
```

#### 1.概念扫盲：网站的基本构成（开发方向）

以blog（自媒体）为例，blog主要包含以下几个部分：

- 1. 文章
- 2. 分类
- 3. 评论
- 4. 搜索
- 5. 统计

blog url特征：

http://blog.sina.com.cn/s/blog_9ffa2c9b01011**z8f**.html
http://blog.sina.com.cn/s/blog_9ffa2c9b01011**wjp**.html



开发网站的基本元素

- 1.1 通过访问不同的url，来得到不同的网页。（用户的角度）
- 1.2 通过解析不同的url，来输出（render）该url指向的网页内容。 （开发者的角度）

解析：
- 用户的请求（request）-》 通过访问不同的url 
- 响应的内容，也就是用户看到的内容   （response） -》 用户最终看到的内容

网站开发 （请求 -》 响应）


响应：

浏览器获得响应内容，解析html，css，javascript（这些都是代码哦）
（因为不同的浏览器对html，css，js这些东西的解析标准是不一样的，所以，看到的或许是不同的）


#### 2. 个人开发流程扫盲 

WEB应用开发基本流程：

- 1. 获得请求 request
- 2. 解析request （拿到url，解析url，让处理该url的方法去处理request）
- 3. 拼接response ，返回给用户
- 4. 浏览器获得响应内容，解析html，css，javascript（这些都是代码哦）

#### 3.安装django
> django理念：all in one

[Django tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)


```
"创建并进入沙盒环境，安装django"
pip install django

"创建project"
django-admin startproject <project name>

"启动project"
python manage.py runserver

"按照提示访问url"
http://127.0.0.1:8000/
```


- Django入门很容易，越到后面，有越多的东西需要处理，渐渐就会放弃使用。
- web框架只是拿来用的工具，更多的需要去研究框架的设计思路，总结方法，而不必沉迷于框架本身。

