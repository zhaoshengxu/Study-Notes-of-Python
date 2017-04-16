# 老王Python学习笔记
## 一、基础篇

> - 代码运行环境为jupyter notebook 4.3.1
> - 符号“>>>”后边内容表示代码运行输出结果

---

### 基础篇17-python语句1.2



#### 1.复习

- 1.1 控制流的基本组成部分：**条件，执行代码块**。
- 1.2 if的基本格式 

```
if expression:
	statement(s)
```
	
- 1.3 控制流的条件表达式(expression)结果，必须为True真
- 1.4 冒号永不忘，尽量使用4个空格，而不是制表符。

---

#### 2.while语句
	
#### 2.1 while的基本格式

```
while expression:
	statement(s)
```
**举个例子**：

```
x = 0
while x < 5: # 条件表达式(expression)，循环终止条件
    x += 1
    print x
>>>
1
2
3
4
5
```
---

#### 2.2 while的基本组成部分

##### 2.2.1 break 结束整个while循环

```
x = 0
while True:
    x += 1
    print x
    if x > 5:
        break
>>>
1
2
3
4
5
6
```

##### 2.2.2 continue 跳出本次循环，但不结束while循环

```
x = 0
while True:
    x += 1
    print x
    
    continue
    # 重复执行上述两步，陷入死循环，下面两步却永远执行不到。
    
    if x > 20:
        break
>>>
1
2
3
.
.
.
```

##### 2.2.3 else 在结束while以后执行

```
x = 0
while x < 5:
    x += 1
    print x
else:
    print "end"
>>>
1
2
3
4
5
end
```
##### 2.2.4 while循环注意事项
> 1. 通常while循环一定要有终止条件，否则会陷入死循环。
> 2. while循环中，在continue、else之前，不能出现break，否则可能出现，break以后的命令执行不到的情况。
> 3. else可以和continue连用。例如：

```
x = 0
while x < 20:
    x += 1
    continue
    print x
else:
    print "end"
>>>
end
```
---

#### 3.for语句

##### 3.1 for的基本格式

```
for item in iterable：
# iterable是迭代器，为可迭代对象（如列表、字符串、元组等）
# item表示迭代器中的任意对象。
	statement（s）
```
举个例子

```
for x in range(5):
# range(5)是迭代器，x相当于上述的item
    print x,  #逗号可使得输出值在同一行
>>>
0 1 2 3 4
```
##### 3.2 for的基本组成部分
> for循环的基本组成和while循环一样。
- 3.2.1 break
- 3.2.2 continue
- 3.2.3 else 

##### 3.3 for的最后一个迭代值将保留

```
for x in range(5):
    print x,  # 依次输出0 1 2 3 4
else:
    print x # x保留最后一个迭代值，x = 4
>>>
0 1 2 3 4 4
```
---

#### 4.布尔值再议

##### 4.1 惰性求值，需要时再求值，短路逻辑。

```
True and False and True and True and False
>>> False
# 实际上Python只是从左到右计算了True and False的结果，后边的都没有计算。
```
有时可以利用Python的惰性求值的逻辑，将一些容易出现False的条件写在代码的前边，以此减少计算量。

##### 4.2 从左到右，从先到后。
Python的计算顺序：从左到右，从先到后。

##### 4.3 利用小技巧，or之默认值。

```
# 当从url中抓取"from"这个值，有时可能并没有这个值，这种情况就可以用or设置默认值，如None。
form_url = a.get("from") or None
```

#### 5. 本节习题

##### 习题一：

1 用while语句的2种方法输出数字：1到10


2 用for语句和continue 输出结果：1 3 5 7 9

##### 习题二：
假设有列表 a = [1,2,3,4,5,6]

1 用for if else 的方法查找数字8是否在列表a里，如果在的话，输出字符串'find'，如果不存在的话，

输出字符串'not find'

2 用while语句操作上面的列表a，输出下面结果：

[2,3,4,5,6,7]

---

#### 6. 本节习题答案
> 重在巩固练习，答案仅供参考。

##### 习题一：

1 用while语句的2种方法输出数字：1到10

```
# 方法1：# x初始值是0，每次循环x增1后输出。
x=0
while x<10:
    x +=1  
    print x,
>>> 1 2 3 4 5 6 7 8 9 10

# 方法2：# x初始值是1，每次循环先输出x，然后x增1。
x=1
while x<11:
    print x,
    x +=1
>>> 1 2 3 4 5 6 7 8 9 10
```
---

2 用for语句和continue 输出结果：1 3 5 7 9

```
for x in range(10):
    x += 1
    if x % 2 ==1:
        print x,  
>>> 1 3 5 7 9
```

---

##### 习题二：
假设有列表 a = [1,2,3,4,5,6]

1 用for if else 的方法查找数字8是否在列表a里，如果在的话，输出字符串'find'，如果不存在的话，输出字符串'not find'

```
a = [1,2,3,4,5,6]
for x in a:
    if x == 8:
        print "find"
    else:
        print "not find"
>>>
not find
not find
not find
not find
not find
not find
```



2 用while语句操作上面的列表a，输出下面结果：

[2,3,4,5,6,7]

```
a = [1,2,3,4,5,6]
i=0
while i<6:    
    a[i] += 1
    print a[i],
    i += 1
>>> 2 3 4 5 6 7


```
