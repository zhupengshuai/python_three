"""
集合类型:
python中的集合与数学中的集合的概念一致
python中的集合是一个无序的不重复的元素序列
集合中只存储不可变数据类型
在python中集合使用{}定义
与列表、字典一样，都是Python中的可变数据类型
集合的创建方式：
1、使用{}直接创建：
s={e1,e2,e3,......,eN}
2、使用内置函数set()创建
s=set(可迭代对象)
集合的删除：
del 集合名
"""
#使用{}直接创建集合
s={10,20,30,40}
print(s,type(s))
#<class 'set'> 集合与字典的区别是字典是{}里是键值对，集合是{}里单个元素
#s={[10,20],[30,40]}
#print(s)#TypeError: unhashable type: 'list'
#注意  集合只能存储不可变数据类型，而像列表、字典属于可变数据类型
print('-'*60)
#使用set()创建集合
s=set()#创建一个空集合，布尔值是false
print(s,type(s))#set() <class 'set'> 集合类型
s={}
print(s,type(s))#{} <class 'dict'> 字典类型
s=set('ningda')
print(s)#{'i', 'n', 'g', 'd', 'a'} 集合的元素是无序的
s2=set([10,20,30])
print(s2)#{10, 20, 30}
s3=set(range(1,11))
print(s3)#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('-'*60)
#集合也属于序列
print('max:',max(s))
print('min:',min(s))
print('len:',len(s))
print('n在集合中存在吗：',('n'in s))#True
print('f在集合中不存在吗：',('f' not in s))#True
#集合的删除
#del s
'''
集合的操作符：
交集 A&B 取两集合相同的元素
并集 A|B 取两集合所以的元素
差集 A-B 取A集合独有部分元素
补集 A^B 取A B两集合独有的部分
'''


