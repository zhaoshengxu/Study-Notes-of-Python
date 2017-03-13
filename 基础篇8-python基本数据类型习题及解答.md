# 老王Python学习笔记
## 一、基础篇

> - 代码运行环境为jupyter notebook 4.3.1
> - 符号“>>>”后边内容表示代码运行输出结果

---

### 基础篇8-python基本数据类型习题及解答

#### python基本数据类型习题
一.已经字符串 s = "i,am,lilei",请用两种办法取出之间的“am”字符。

二.在python中，如何修改字符串？

三.bool("2012" == 2012) 的结果是什么。

---

四.已知一个文件 test.txt，内容如下：

- 2012来了。
- 2012不是世界末日。
- 2012欢乐多。
- 

1. 请输出其内容。
2. 请计算该文本的原始长度。
3. 请去除该文本的换行。
4. 请替换其中的字符"2012"为"2013"。
5. 请取出最中间的长度为5的子串。
6. 请取出最后2个字符。
7. 请从字符串的最初开始，截断该字符串，使其长度为11.
8. 请将{4}中的字符串保存为test1.py文本.
 
---

五.请用代码的形式描述python的引用机制。

---

六.已知如下代码

```
a = "中文编程"
b = a
c = a
a = "python编程"
b = u'%s' %a
d = "中文编程"
e = a
c = b
b2 = a.replace("中","中")
```

1. 请给出str对象"中文编程"的引用计数
2. 请给出str对象"python编程"的引用计数

---

七.已知如下变量

a = "字符串拼接1"

b = "字符串拼接2"


1. 请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
2. 请将a与b拼接成字符串c，并用逗号分隔。
3. 请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
 
---

八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案。

1.包含0-9的数字。
2.所有小写字母。
3.所有标点符号。
4.所有大写字母和小写字母。
5.请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。

---

九.已知字符串

a = "i,am,a,boy,in,china"

1. 假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
2. 请使用2种办法取出其间的字符"boy"和"china"。
3. 请找出第一个"i"出现的位置。
4. 请找出"china"中的"i"字符在字符串a中的位置。
5. 请计算该字符串一共有几个逗号。
 
---

十.请将模块string的帮助文档保存为一个文件。

---

#### python基本数据类型习题答案

> 重在巩固练习，答案仅供参考。

---

一. 已知字符串 s = "i,am,lilei",

请用两种办法取出之间的“am”字符。

```
#方法1
s = "i,am,lilei"
print s[2:4]
>>> am

#方法2
c = s.split(',')[1]
print c
>>> am
```
---

二. 在python中，如何修改字符串？

```
# 可以用字符串的replace方法.
a = 'i love php'
a_replace = a.replace('php','python')

print a_replace
>>> i love python
```
---

三. bool("2012" == 2012) 的结果是什么。

```
"2012" == 2012
>>> False

"""
结果是False,
==判断对象的数据类型，尽管看起来数值是一样的，
但是他们的类型不同，一个是字符串，一个是数字.
"""
```
---

四.已知一个文件 test.txt，内容如下：
- 2012来了。
- 2012不是世界末日。
- 2012欢乐多。
-   

```
f = open('test.txt','r')
content = f.read()
dcontent = content.decode('utf-8') # 转换为unicode

## 1.请输出内容
print content
>>> 
2012来了。
2012不是世界末日。
2012欢乐多。
# 一个空行

## 2.请计算该文本的原始长度.
print len(dcontent)
>>> 29

## 3.请去除该文本的换行
print content.replace('\n','')
>>> 2012来了。2012不是世界末日。2012欢乐多。

## 4.请替换其中的字符"2012"为"2013"。
print content.replace('2012','2013')
>>>
2013来了。
2013不是世界末日。
2013欢乐多。
# 一个空行

## 5.请取出最中间的长度为5的子串。
print dcontent[len(dcontent)/2:len(dcontent)/2+5].encode('utf-8')
>>> 世界末日。

## 6.请取出最后2个字符。
print dcontent[-2:].encode('utf-8')
>>>
。
# 一个空行

## 7.请从字符串的最初开始，截断该字符串，使其长度为11.
print dcontent[:11].encode('utf-8')
>>> 
2012来了。
201

## 8.请将{4}中的字符串保存为test1.py文本.

rinfo = content.replace('2012','2013')
f = open('test1.py','w')
f.write(rinfo)
f.close() ## 关闭文件

f = open('test1.py','r')
print(f.read())
>>>
2013来了。
2013不是世界末日。
2013欢乐多。
# 一个空行
```
---

五. 请用代码的形式描述python的引用机制。

```
import sys

cinfo = '1234'
print id(cinfo)
print sys.getrefcount('1234')   

binfo = '1234'
print id(binfo)
print sys.getrefcount('1234')
```
---

六.已知如下代码

```
a = "中文编程"
b = a
c = a
a = "python编程"
b = u'%s' %a
d = "中文编程"
e = a
c = b
b2 = a.replace("中","中")
```
1. 请给出str对象"中文编程"的引用计数
2. 请给出str对象"python编程"的引用计数


```
a = "中文编程"  ##引用计数开始是3，然后a变量引用了字符串对象3 + 1 =4
print "a:%s" % id(a)

b = a
print "b:%s" % id(b)##4 + 1 = 5

c = a
print "c:%s" % id(c)## 5 + 1 = 6

print sys.getrefcount('中文编程')##输出结果是6
print 'ssss'
a = "python编程"
print "a:%s" % id(a)###6-1 = 5##a引用另外一个字符串对象

b = u'%s' % a.decode('utf-8')
print "b:%s" % id(b)###5-1 = 4

print sys.getrefcount('中文编程')##输出结果是4

d = "中文编程"
print "d:%s" % id(d)###新建一个变量，引用字符串 4 + 1 = 5

e = a
print "e:%s" % id(e)

c = b
print "c:%s" % id(c)### c引用另外一个字符串对象，5 - 1 = 4

print sys.getrefcount('中文编程')


b2 = a.replace("中","中")
print "b2:%s" % id(b2)

print sys.getrefcount('中文编程')
print sys.getrefcount('python编程')
```
---

七.已知如下变量

a = "字符串拼接1"

b = "字符串拼接2"

1. 请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣.

```
# 方法1：+  在做大量的字符串对象拼接的时候不推荐 
c = a + b
print c
>>> 字符串拼接1字符串拼接2

## 方法2：模板
c = "%s%s" % (a,b)
print c
>>> 字符串拼接1字符串拼接2

# 方法3：format
c = "{a}{b}" .format (a=a,b=b)
print c
>>> 字符串拼接1字符串拼接2

# 方法4：join
c = "".join([a,b])
print c
>>> 字符串拼接1字符串拼接2

# 方法5：字典
c= "%(a)s%(b)s" % {'a':"字符串拼接1", 'b':"字符串拼接2"}
print c
>>> 字符串拼接1字符串拼接2
```

2. 请将a与b拼接成字符串c，并用逗号分隔。

```
c = ",".join([a,b])
print c
>>> 字符串拼接1,字符串拼接2
```
3. 请计算出新拼接出来的字符串长度，并取出其中的第七个字符。

```
lennum = len(c.decode('utf-8'))
lennum
>>> 12

print c.decode('utf-8')[6].encode('utf-8')
>>> 字
```
---

八. 请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案:

1.包含0-9的数字。
2.所有小写字母。
3.所有标点符号。
4.所有大写字母和小写字母。

```
import string as str
digits = str.digits
lowercase = str.ascii_lowercase
punc = str.punctuation
letters = str.ascii_letters 
print(digits)
print(lowercase)
print(punc)
print(letters)
>>>
0123456789
abcdefghijklmnopqrstuvwxyz
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```
5. 请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。

```
all = ''.join([digits, lowercase, punc, letters])
all
>>> 
'0123456789abcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
```
---

九. 已知字符串

a = "i,am,a,boy,in,china"

1. 假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
2. 
```
# dictionary meth
ac = "i,am,a,%(sex)s,in,%(country)s"  % {'sex':'girl','country':'china'}

print ac
>>> i,am,a,girl,in,china

# format method
bc = "i,am,a,{sex},in,{country}" .format (sex='girl',country='india')

print bc
>>> i,am,a,girl,in,india
```

2. 请使用2种办法取出其间的字符"boy"和"china"。
```
##方法1
print a[7:10]
print a[-5:]
>>>
boy
china

##方法2
cinfo = a.split(',')

print cinfo[3]
print cinfo[-1]
>>>
boy
china

```
3. 请找出第一个"i"出现的位置。

```
# find和index的区别在于如果找不到要查找的对象，find返回-1，而index则报错
print a.find('i')
print a.index('i') 
>>>
0
0
```

4. 请找出"china"中的"i"字符在字符串a中的位置。

```
# method 1 ,首先锁定查找位置
print a.find('i',a.find('china'))
>>> 16

# method 2 , 返回查找对象的最大索引
print a.rfind('i')
>>> 16
```

5. 请计算该字符串一共有几个逗号
```
print a.count(',')
>>> 5
```
---

十. 请将模块string的帮助文档保存为一个文件。

```
import sys
import string

f = open('test.log','w')
sys.stdout = f
help(string)
f.close()
```