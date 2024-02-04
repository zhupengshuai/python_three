'''
列表：是指一系列的按特定的顺序排列的元素组成
是python中内置的可变序列
在python中使用[]定义列表，元素与元素之间使用英文逗号分隔
列表中的元素可以是任意的数据类型
列表的创建方式：
1、使用[]直接创建：
列表名=[e1,e2,e3,.......]
2、使用内置的函数list()创建列表：
列表名=list(序列)
'''
#直接创建列表
lst=['ningda','宁大',98]
print(lst)
#使用内置函数创建列表
lst2=list('ningbo')
lst3=list('宁大')
print(lst2)
print(lst3)
lst4=list(range(1,10,2))#[1, 3, 5, 7, 9],从1开始到10结束，步长为2
print(lst4)
print('----------------------------------')
#列表是序列中的一种，对序列的操作符、运算符和函数均可使用
print(lst+lst2+lst3)#相加操作
print(3*lst3)#相乘操作
print(len(lst))#3 len()计算列表元素个数
print(max(lst4))
print(max(lst3))
#删除列表
#del lst3
#print(lst3)#NameError: name 'lst3' is not defined. Did you mean: 'lst'?
'''
列表的遍历操作：
for 、enumerate
'''
lst=['北京','上海','重庆','天津']
#使用for循环遍历列表元素
for i in lst:
    print(i,end='\t')
print('-----------------------------')
for i in range(0,len(lst)):
    print(i,'--->',lst[i])
#使用enumearte()函数
print('---------------------------------')
for index,item in enumerate(lst):
    print(index,item)#index是序号，item是元素
#手动修改起始值
for index,item in enumerate(lst,start=1):#序号从1开始
    print(index,'--->',item)