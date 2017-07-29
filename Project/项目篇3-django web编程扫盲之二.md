# 老王Python学习笔记
> 运行环境：
>- VirtualBox4.8.0 /Ubuntu16.04.1 /x86_64(Python2.7)
>- 代码编辑器sublime text 3
## 三、项目篇

### 项目篇3-django web编程扫盲之二

#### 1. 为什么我只能做到这步？
- 没有样式，或者没有使用模板template
- 数据很少，没有使用数据库

#### 2. web码农三步问：

    2.1 web码农问题之一：web编程的核心是什么？ 折腾database
    数据库，又称为持久化存储，如pickle，mysql，mssql，bsddb, sqlitedb。
    非持久化存储 memcacehd（key- value，新浪曾经使用） mongodb(读取写入非常快)
    
    2.2 web码农问题之二：web编程的核心是什么？ 折腾template

    开发逻辑上的折腾： html(div,table) + css + javascript(ajax,异步) + 浏览器兼容性
    编程思路上的理解：表现和内容分离

    mvc: 
    控制器 
    数据 model orm（对象关系映射）
    展现

    2.3 web码农问题之三：web编程的核心是什么？ 折腾框架

    django: all in one

    flask: wsgi组件包

     tornado:异步IO模型，如知乎

      webpy web2py 

      框架：

      狭义：学习框架 ： 看文档，写项目，看源码，写框架
      
      广义：结构

    总之，就是折腾。
> **学习框架套路：看文档，写项目，看源码**


#### 3. 来折腾一下下templete,了解一下非持久存储。

    from django.template import Template, Context

    template_str =  ""My name is {{ name }}.""

    """
    占位符
    """

    t = Template(template_str)

    c = Context({"name": "Stephane"})
    t.render(c)


接下来的学习重点：
- [Djangobook1.0：适合django 0.96 ](http://djangobook.py3k.cn/chapter04/)
- [Djangobook2.0：适合django1.0和1.1](http://djangobook.py3k.cn/2.0/chapter04/)


