'''
字典类型是根据一个信息查找另一个信息的方式构成了“键值对”，它表示索引的键
和对应的值构成的成对关系。
一个键(key)对应一个值(value)，没有重复的键，但一个值可以有多个键与之对应
字典类型的创建方式：
1、使用{}直接创建字典
d={key1:value1,key2:value2......}
2、使用内置函数dict()
dict(key1=value1,key2=value2......)
3、通过映射函数创建字典
zip(lst1,lst2)
'''
#使用{}创建字典
d={10:'cat',20:'dog',30:'ningda',40:'python'}
d1={10:'cat',20:'dog',30:'ningda',30:'python'}
print(d1)#{10: 'cat', 20: 'dog', 30: 'python'} key值相同时，value值进行了覆盖
print(d)#{10: 'cat', 20: 'dog', 30: 'ningda', 40: 'python'}
print('-'*60)
#zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','ningda','python']
ziplst=zip(lst1,lst2)
print(ziplst)#<zip object at 0x000002AEDCE37FC0>
#print(list(ziplst))
#[(10, 'cat'), (20, 'dog'), (30, 'ningda'), (40, 'python')] 利用list()转为列表
d=dict(ziplst)
print(d)#{10: 'cat', 20: 'dog', 30: 'ningda', 40: 'python'}
#使用dict()前要将上面的print(list(ziplst))注释掉，因为已转为列表形式
print('-'*60)
#使用参数创建字典
d2=dict(cat=10,dog=20)#左侧cat是key,右侧10是value
d3=dict(a='cat',b='dog')
print(d3)
print(d2)
#元组也可以作为字典中的key
t=('cat',20)
print({t:'dog'})#{('cat', 20): 'dog'} t是key，dog是value
print('-'*60)
#字典属于序列
print('max:',max(d))
print('min:',min(d))
#字典删除：del d
'''
注意：字典中的key是无序的，因为后来的python版本对解释器进行了处理，才看到
顺序与添加的顺序“一致”
'''
'''
字典元素的取值：
d[key]或d.get(key)
字典元素的遍历：
1、遍历出key与value的元组
for element in d.items():
     pass
2、分别遍历出key和value
for key,value in d.items():
     pass
'''
d4={'ningda':10,'python':20,'word':30,'宁波':40}
#1、使用d[key]访问元素
print(d4['python'])
#2、使用d.get(key)
print(d4.get('ningda'))
#注意：二者之间的区别在于，如果key不存在，第一个会报错，第二个可以指定默认值
#print(d['java'])#KeyError: 'java'
print(d.get('java'))#None 默认
print(d.get('java','不存在'))#指定值 不存在
#字典的遍历
for item in d4.items():
    print(item,type(item))#key和对应的value组成的一个元组<class 'tuple'>
#分别遍历出key和value
for key,value in d4.items():
    print(key,'---->',value)#宁波 ----> 40

