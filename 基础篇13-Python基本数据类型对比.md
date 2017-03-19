#### Python基本数据类型对比

##### 表1 python基本数据类型特点（**顺序、变化、迭代**）
数据类型|有无顺序|是否可变|是否可迭代
:--------:|:--------:|:-------:|:--------:
数字|无|否|否
字符串|有|否|是
列表|有|是|是
元组|有|否|是
集合|无|是|否
字典|无|是|否


---

##### 表2 python基本数据类型的方法（**创建、添加、修改、删除、成员关系及其他**）
数据类型|字符串|元组|列表|集合|字典
:--------:|:-------------:|:-----------------------:|:-----------------------:|:----------------:|:-------------:
创建方法|str()|tuple()|list()|set()、frozenset()|dict()
添加修改|replace,join|-| +,extend,append,insert|add,update|赋值
删除操作|-|-|del,remove,pop|remove|del,clear,pop
成员关系|-|-|in,not in|in,not in|in,has_key
其他|count,upper,etc.|index,count|rang,xrange,sort,etc|交集、并、差集,etc|keys,values,etc
