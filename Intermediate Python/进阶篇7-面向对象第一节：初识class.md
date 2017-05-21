# 老王Python学习笔记
> 运行环境：代码编辑器sublime text 3（配置anaconda）
## 二、进阶篇

### 进阶篇7-面向对象第一节：初识class
> class即为**类**


#### 1.如何定义一个最基本的class
> 当定义一个class的内置方法method时，method参数的第一个永远是self，self代表class自身。

```
# 定义一个最基本的class

class test(object):

"__init__和get被称之为test对象的方法"

	def __init__(self,var1):
		self.var1 = var1 
	
        '''
	    class传参，将变量var1赋值给self.var1
	    self.var1类似于函数中的全局变量，class内部都可以调用
        '''

	def get(self,a=None):
		return self.var1


#定义一个基本函数
def get(a):
	return a

```

#### 2. 如何去使用class内置的方法
- 1. 实例化这个class（即test） t = test()
- 2. 使用 class.method()的方式去调用 class 的内置方法

```

"t是class test的一个实例"

t = test('test str heiheihei') # class对象的初始化
print t.get()
```



#### 3. class和函数的区别
- class和函数有很多地方非常相似
- class可以看做是函数的集合
- class内函数的第一个变量必须是self
- python主张简洁，能用函数解决，尽量就不要用class，除非需要用class整理框架结构，因此需要注意方法的合理使用，。

---

### 面向对象习题

```
'''
一：定义一个学生类。有下面的类属性：

1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]

类方法：

1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int


写好类以后，可以定义2个同学测试下:

zm = student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100

lq = student('liqiang',23,[82,60,99])

返回结果：
liqiang
23
99

'''


class student(object):
    """
    一：定义一个学生类。有下面的类属性：
    1 姓名
    2 年龄
    3 成绩（语文，数学，英语)[每课成绩的类型为整数]

    类方法：
    1 获取学生的姓名：get_name() 返回类型:str
    2 获取学生的年龄：get_age() 返回类型:int
    3 返回3门科目中最高的分数。get_course() 返回类型:int
    """

    def __init__(self, name, age, course):
        "初始化"
        super(student, self).__init__()
        self.name = name
        self.age = age
        self.course = course

    def get_name(self):
        "输出学生姓名"
        if isinstance(self.name, str):
            return self.name
        else:
            return "TypeError"

    def get_age(self):
        "输出学生年龄"
        if isinstance(self.age, int):
            return self.age
        else:
            return "TypeError"

    def get_course(self):
        "输出学生语文、数学、英语三门课程中的最高成绩"
        for x in self.course:
            if not isinstance(x, int):
                return "TypeError"
        return max(self.course)


zm = student('zhangming', 20, [69, 88, 100])

print(zm.get_name())
print(zm.get_age())
print(zm.get_course())
>>>
zhangming
20
100

lq = student('liqiang', 23, [82, 60, 99])

print(lq.get_name())
print(lq.get_age())
print(lq.get_course())
>>>
liqiang
23
99

```

---

```
"""
二：定义一个字典类：dictclass。完成下面的功能：


dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)


2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})
"""


class dictclass(object):
    """
    二：定义一个字典类：dictclass。完成下面的功能：

    dict = dictclass({你需要操作的字典对象})

    1 删除某个key
    del_dict(key)

    2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
    get_dict(key)

    3 返回键组成的列表：返回类型;(list)
    get_key()

    4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
    update_dict({要合并的字典})
    """

    def __init__(self, **arg):
        "初始化"
        super(dictclass, self).__init__()
        self.arg = arg

    def del_dict(self, key):
        "删除某个key"
        del self.arg[key]
        return "删除key后的dict：%s" % self.arg

    def get_dict(self, key):
        "判断某个键是否在字典里，如果在返回键对应的值，不存在则返回'not found'"
        return self.arg.get(key, "not found")

    def get_key(self):
        "返回键组成的列表"
        return self.arg.keys()

    def update_dict(self, **arg1):
        "合并字典，并且返回合并后字典的values组成的列表"
        self.arg.update(arg1)
        return self.arg.values()


dict = dictclass(n='name', a='age', g='gender')
print(dict.del_dict('n'))
>>> 删除key后的dict：{'a': 'age', 'g': 'gender'}

print(dict.get_dict('g'))
>>> gender

print(dict.get_dict('n'))
>>> not found

print(dict.get_key())
>>> dict_keys(['a', 'g'])

print(dict.update_dict(m='math', e='english'))
>>> dict_values(['math', 'english', 'age', 'gender'])

```