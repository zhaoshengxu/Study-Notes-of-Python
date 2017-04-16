# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:53:04 2017

@author: ZSX
"""
import linecache #读取多行文件
import collections #统计频次
import time  #计算代码运行时间

now = time.time() #代码开始运行时间

# 前期处理，整理数据
f = linecache.getlines("t.txt") #读取文件t.txt

#每一条tweet包含的字段名称
data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')

keys = {data_keys[k]:k for k in range(len(data_keys))} #将tweet字段编号，便于接下来的使用

lines = [x[1:-1].split('","') for x in f] #将每一条tweet以","分隔符拆分

#1.该文本里，有多少个用户。（要求：输出为一个整数。）
"""
@解题思路：1.把所有用户名放在一个列表中；2.将列表转换为集合，去除重复用户，集合长度即为用户数量
@吐槽：
"""
users = [line[keys["username"]] for line in lines]  

users_total = len(set(users))

assert type(users_total) == int #断言注释对象数据类型

print("1.该文本的用户数：%d" % users_total)
 
#2.该文本里，每一个用户的名字。 （要求：输出为一个list。）
"""
@解题思路：题目1中已经得到了所有用户名的列表，即为本题答案
@吐槽：
"""
assert type(users) == list

print("2. 该文本的所用户名：%s" % users)

#3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）
"""
@解题思路：根据发布时间，筛选在2012年11月发布的推文，并放在一个列表中，列表长度即为答案
@吐槽：还可以直接使用列表推导式
len([line[keys['created_at']] for line in lines if line[keys['created_at']].startswith('2012-11')])
"""
lines_from_2012_11 = filter(lambda line: line[keys['created_at']].startswith('2012-11'), lines)

lines_total_from_2012_11 = len(lines_from_2012_11)

assert type(lines_total_from_2012_11) == int

print("3. 2012年11月发布的tweets数量：%d" % lines_total_from_2012_11)

#4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）
"""
@解题思路：1.把所有日期放在一个列表中；2.利用集合，去除重复元素，列表排序即可
@吐槽：
"""
users_by_date = [line[keys['created_at']].split(' ')[0] for line in lines]  

lines_by_created = list(set(users_by_date))

lines_by_created.sort()

assert type(lines_by_created) == list #断言注释对象数据类型

print("4. 该文本里，有哪几天的数据：%s" % lines_by_created)

#5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）
"""
@解题思路：1.把所有的小时放在一个列表中；2.统计频次输出结果
@吐槽：统计频次用内置方法collections.Counter(hours).most_common()[0][0]简洁方便
"""
hours = [int(line[keys['created_at']][11:13]) for line in lines]

hours_most_common = collections.Counter(hours).most_common()[0][0]

assert type(hours_most_common) == int

print('5.该文本里，在哪个小时发布的数据最多: %d' % hours_most_common)

#6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）
"""
@解题思路：
1.扫描每一条推文，解析其中的发布日期和用户名；
2.统计该日期该用户名出现的次数；
3.将上述统计结果按照发布数量排序，即可得到每天发布推文数量最多的用户
@吐槽：感觉好复杂
"""
dateline_by_user = {k:dict() for k in lines_by_created}

for line in lines:
    dateline = line[keys['created_at']].split(' ')[0]
    username = line[keys['username']]
    if dateline_by_user[dateline].has_key(username):
        dateline_by_user[dateline][username] += 1
    else: 
        dateline_by_user[dateline][username] = 1

for k,v in dateline_by_user.items():
    us = v.items()
    us.sort(key=lambda k: k[1], reverse = True)
    dateline_by_user[k] = {us[0][0]:us[0][1]}

assert type(dateline_by_user) == dict

print('6.该文本里，输出在每一天发表tweets最多的用户:%s' % dateline_by_user)

#7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets） 
"""
@解题思路：1.将2012-11-03发布推文筛选出来；2.将2012-11-03发布的推文的小时取出放在列表中；3.统计频率
@吐槽：
"""

lines_from_2012_11_03 = filter(lambda line: line[keys['created_at']].startswith('2012-11-03') ,lines)

hourlines_from_2012_11_03 = [line[keys['created_at']][11:13] for line in lines_from_2012_11_03]

hour_timeline_from_2012_11_03 = collections.Counter(hourlines_from_2012_11_03).most_common()

assert type(hour_timeline_from_2012_11_03) == list

print('7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率: %s' % hour_timeline_from_2012_11_03)

#8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）
"""
@解题思路：1.将每条tweet的source取出放入一个list；2.统计频率
@吐槽：
"""

source = [line[keys["source"]] for line in lines]

source_list = collections.Counter(source).most_common()

assert type(source_list) == list

print('8. 统计该文本里，来源的相关信息和次数:%s' % source_list)

#9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)
"""
@解题思路：1.筛选出以目标网址开头的tweet放入list；2.list长度即为答案
@吐槽：列表推导式
"""
umi = filter(lambda line: line[keys['rt_v_url']].startswith('https://twitter.com/umiushi_no_uta') ,lines)

umi_total = len(umi)

assert type(umi_total) == int

print('9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个:%d'% umi_total)

#10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）
"""
@解题思路：1.根据UID筛选出用户的tweet放入list；2.list长度即为答案
@吐槽：列表推导式
"""
tweets_from_573638104 = filter(lambda line: line[keys['uid']] == '573638104' ,lines)

tweets_total_from_573638104 = len(tweets_from_573638104)

assert type(tweets_total_from_573638104) == int

print('10. UID为573638104的用户 发了多少个微博: %d' % tweets_total_from_573638104)

#11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。
"""
@解题思路：1.uid类型转换，并判断是否为空；2.统计每个用户及发表tweet数量；3.排序输出结果
@吐槽：参数可为字符串或者数字    
"""
def get_user_by_max_tweets(*uids):
    uids = filter(lambda u:type(u) == int or u.isdigit(),uids)
    uids = map(str,uids)
    if len(uids) > 0:
         uids_dict = {x:0 for x in uids}
         for uid in uids:
             uids_dict[uid] = len(filter(lambda line: line[keys['uid']] == uid ,lines))
             uids_and_tweets_total = [(x,y) for x,y in uids_dict.items()]
             uids_and_tweets_total.sort(key=lambda k:k[1],reverse=True)
         return uids_and_tweets_total[0][0]
    else:
        return "null"

assert get_user_by_max_tweets() == 'null'
assert get_user_by_max_tweets('ab','cds') == 'null'
assert get_user_by_max_tweets('ab','cds','123b') == 'null'
assert get_user_by_max_tweets('12342','cd') == '12342'
assert get_user_by_max_tweets('28803555',28803555) == '28803555'
assert get_user_by_max_tweets('28803555',28803555,'96165754') == '28803555'

print('11. 定义一个函数，该函数可放入任意多的用户uid参数:get_user_by_max_tweets(*uids)')

#12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）
"""
@解题思路：1.将发布的每条tweet的uid和长度组成一个元组，进而组成一个列表；2.按照长度降序排列，输出结果
@吐槽：
"""
lines_by_content_length = [(line[keys['uid']],len(line[keys['content']])) for line in lines]

lines_by_content_length.sort(key = lambda k: k[1],reverse = True)

user_by_max_content = lines_by_content_length[0][0]

assert type(user_by_max_content) == str

print('12. 该文本里，谁发的微博内容长度最长: uid = %s' % user_by_max_content)

#13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）
"""
@解题思路：1.将发布的每条tweet的uid和转发数组成一个元组，进而组成一个列表；2.按照转发数降序排列，输出结果
@吐槽：
"""
 
lines_by_rt = [(line[keys['uid']],int(line[keys['rt_num']])) for line in lines if line[keys['rt_num']] != '']

lines_by_rt.sort(key = lambda k: k[1],reverse = True)

user_by_max_rt = lines_by_rt[0][0]
# todo 如果有多个最多怎么办？
assert type(user_by_max_rt) == str

print('13. 该文本里，谁转发的URL最多: uid = %s' % user_by_max_rt)

#14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）
"""
@解题思路：1.筛选11点发布的所有tweet组成列表；2.取出每条tweet的uid组成列表；3.根据uid统计频率
@吐槽：
"""
lines_on_hour11 = filter(lambda line:line[keys['created_at']].startswith('11',11,13),lines)

uid_on_hour11 = [line[keys['uid']] for line in lines_on_hour11]

uid_by_max_tweets_on_hour11 = collections.Counter(uid_on_hour11).most_common()[0][0]
# todo 如果有多个最多怎么办？

assert type(uid_by_max_tweets_on_hour11) == str

print('14. 该文本里，11点钟，谁发的微博次数最多: uid = %s' % uid_by_max_tweets_on_hour11)

#15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）
"""
@解题思路：1.判断源微博URL是否非空，将源微博URL非空的用户uid取出组成列表；2.统计频率，输出频率最高者
@吐槽：
"""
uid_by_v_url = [line[keys['uid']] for line in lines  if line[keys['v_url']] !='']

uid_by_max_v_url = collections.Counter(uid_by_v_url).most_common()[0][0]
# todo 如果有多个最多怎么办？
assert type(uid_by_max_v_url) == str

print('15. 该文本里，哪个用户的源微博URL次数最多: uid = %s' % uid_by_max_v_url)

print '运算时间：%s'%(time.time() - now) #整体运行时间


