# 老王Python学习笔记
## 一、基础篇

> - 代码运行环境为jupyter notebook 4.3.1
> - 符号“>>>”后边内容表示代码运行输出结果

---

### 基础篇16-python语句1.1

#### 1.print语句

##### 1.1 基本输出

```
print 2
>>> 2
```

##### 1.2 print的逗号

```
# 两行输出多个对象
print 2
print 3
>>>
2
3

# 单行输出多个对象，逗号分隔每个对象
print 2, 3
>>> 2 3
```	

##### 1.2 输出到文件：>>为重定向

```    
# 正常读写文件方法
a = open('info.txt','w')
a.write("hello world!")
a.close()
    
a = open('info.txt','r')
print a.read()
>>> hello world!


# print >>为重定向
a = open('info1.txt','w')
print >> a, "hello world!","all is well."
a.close()

a = open('info1.txt','r')
print a.read()
>>> hello world! all is well
```
---

#### 2.控制流语句（control flow）
##### 2.1 组成
控制流语句**由条件和执行代码块组成。**

其中，条件可分为**决策**（if语句）、**循环**（for、while语句）和**分支**（switch语句）。

也就是说，if、while、for 函数，皆为控制流语句。

```
if True:  # 条件
    print "hello world!"  #执行代码块
```

##### 2.2 格式
控制流语句中的冒号(:)分隔了条件和执行代码块。

条件之后，执行代码块之前的4个空格是计算机用来识别执行代码块。

---

#### 3.布尔值
##### 3.1 条件皆为布尔值
控制流语句中的条件均为布尔值。另外，不要误解了真假与布尔值。

```
x=1
if x:  # if x 等价于if bool(x) 
    print "all is well"
```

##### 3.2 布尔值的几个最基本运算符

- 1. **and**：几个条件同时为bool真，则条件为真

```
True and True
>>>True
```

- 2. **or**：至少有一个条件为bool真，则条件为真

```
True or False
>>>True
```

- 3. **is**：检查共享，检查是否引用统一数据对象。

```
False is False
>>>True
    
1 is True
>>>False
```

- 4. **==**：检查值是否相等

``` 
1 == True
>>> True
```

- 5. **not**：not False

```
# 通常的if语句
if True:  # 条件为真
    print "hello world!"  #执行代码块
>>> hello world!

# 条件为“不假”的if语句
if not False:  # 条件为不假，即为真
    print "hello world!"  #执行代码块
>>> hello world!
```
---

#### 4. if语句 （控制流语句）

##### 4.1 if的组成：if else elif pass
> python中用elif替代了switch。

```
if True：
    print "True"
elif not True:
    print "not True"
else:
    pass # 什么也不输出
```	

##### 	4.2 奇技淫巧：三元表达式
###### x if  else

```
1  if True else 0
# 如果条件为真返回1，否则返回0
>>> 1
```

###### 活用list  

```
[3,4][True]
# 如果条件为真，则bool值为1，返回值为list[1]，即为4
# 否则bool值为0，返回值为list[0]，即为3
>>> 4
```
需要说明的是，
> python之禅中提到，简洁优于复杂，所以越简单清晰越好，三元表达式偶尔使用一下即可。




