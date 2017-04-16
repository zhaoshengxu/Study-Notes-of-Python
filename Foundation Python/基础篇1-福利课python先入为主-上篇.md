# 老王Python学习笔记
## 一、基础篇

> - 代码运行环境为jupyter notebook 4.3.1
> - 符号“>>>”后边内容表示代码运行输出结果

---

### 基础篇1-福利课python先入为主-上篇
---
#### 一、python特性概要



##### 1. python是脚本解释型语言，与编译型语言（如C）对比如下：

**脚本解释型语言的内部机制**

在运行脚本之后，得到结果之前，python需要做以下工作：
- 1. python先将脚本编译成字节码文件（pyc，pyo）
- 2. python虚拟机解释并运行字节码文件

**编译型语言的内部机制**
- 1. 先将源代码编译成机器码（简单理解为机器能读懂的代码），生成可执行文件
- 2. 运行可执行文件

---

##### 2. Python特性总结
- 字节码
- 动态语义
- 缩进

---

##### 3. python之禅（the zen of python）

> 输入命令 import this ,返回结果即为python之禅

**The Zen of Python, by Tim Peters**

Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than right now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!


**中文版python之禅（国内大牛赖教主翻译）**：
![python之禅(赖教主翻译)](http://oez33r3ch.bkt.clouddn.com/Python%E4%B9%8B%E7%A6%85.jpg)

---

#### 二、简述python编程的基本方式

##### 1. 一个标准模块脚本的写作范式

- 1. **定义编码**，如#coding= utf-8 ，特别是需要书写中文的时候。
- 2. 在脚本的开头，**撰写脚本文档**，说明脚本的功能用途。
- 3. **定义函数，程序主体**，期间涉及到单行和多行注释。

```
#coding= utf-8 

"这是一个标准模块脚本的写作范式，此处为脚本文档。"

#这里是给下面的语句作注释（单行注释）
new_str = "这是一个全局变量"

def hello():
    """
    这是一个函数定义的多行注释，
    继续多行
    没有问题。
    """
    return "hello world"

#程序主体
if __name__ == "__main__":
    print hello()
```
---

##### 2. 回顾字节码
根据python的内部机制：
在运行脚本之后，得到结果之前，python需要做以下工作：
- 1. python先将脚本编译成字节码文件（pyc，pyo）
- 2. python虚拟机解释并运行字节码文件

可以知道，脚本运行一次之后，即便删除脚本文件，仍然可以输出结果，因为python已经将脚本文件编译成字节码文件（pyc，pyo）。

---

##### 3. 优美处理结构：反斜杠与小括号

```
# 反斜杠'\'可用来连续输入时的换行
# 小括号'()'将部分内容括起来作为一个整体
def hello(a):
    if (a % 2 == 1) & (a > 0) \
       & (a < 100):
       return "hello world"
    else: 
        return "Error 404"

hello(3)
>>> 'hello world'

hello(2)
>>> 'Error 404'
```
