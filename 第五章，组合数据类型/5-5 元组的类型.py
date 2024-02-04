'''
元组：是python中内置的不可变序列
在python中使用()定义元组，元素与元素之间使用英文逗号分隔
元组中只有一个元素的时候吧，逗号也不能省略
元组的创建方式：
1、使用()直接创建元组
2、使用内置函数tuple()创建元组：
元组名=tuple(序列)
删除元组：
del 元组名
'''
#使用（）创建元组
tup=('ning',[2,6,7],'宁波','python')
print(tup)
print('-'*60)
#使用内置函数tuple()
tu1=tuple('ningbo')
tu2=tuple([20,60,5,7,8])
print(tu1)
print(tu2)
print('-'*60)
print('10是否存在：',(10 in tu2))
print('最大值是：',max(tu2))
print('元组个数：',len(tu2))
print('5的位置是：',tu2.index(5))
print('20出现的次数：',tu2.count(20))
print('-'*60)
#元组只有一个元素，逗号也不能省
tu3=(10)
tu4=(10,)
print(tu3,type(tu3))#10 <class 'int'>
print(tu4,type(tu4))#(10,) <class 'tuple'> 元组类型
print('-'*60)
#元组删除
#del tu4
#print(tu4)#NameError: name 'tu4' is not defined.