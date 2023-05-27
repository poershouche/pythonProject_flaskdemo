"""
1.    给定一个非空正整数的列表，按照列表内数字重复出现次数，从高到低排序
int_list = [2,3,4,2,2,5,6,6,3,2,1,1,2,3]

example:
int_list = [2,3,4,2,2,5,6,6,3,2,1,1,2,3]
count_list= {}

empty_list=[]

for i in int_list:
    count = int_list.count(i)
    count_list[i]=count

l = sorted(count_list.items(), key=lambda x: x[1], reverse=True)
print(l)

"""
"""
# 2.   月份缩写：如果有 months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."，
# 编写一个程序，用户输入一个月份的数字，输出月份的缩写。
months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."
split = months.split('.')
split.remove('')
print(split)
list1=[i for i in range(1,11)]
dict1=dict(zip(list1,split))
print(dict1)
num=int(input('num:'))
if num in dict1.keys():
    print(dict1[num])
"""

d=dict(
    a=13,
       b=14)
print(d)
print(type(d))