'''
字典的操作方法：
1、d.keys():获取所有的key数据
2、d.value():获取所以的value数据
3、d.pop(key,default):key存在获取相应的value，同时删除key-value对
，否则获取默认值
4、d.popitem():随机从字典中取得一个key-value对，结果为元组类型，同时将该
键值对删除
5、d.clear():清空字典中所有的key-value对
'''
d={'北京':101,'上海':102,'天津':103}
print(d)
#向字典中添加元素
d['重庆']=104
print(d)#{'北京': 101, '上海': 102, '天津': 103, 104: '重庆'}
print('-'*60)
#获取字典中所以的key
keys=d.keys()
print(keys,type(keys))#<class 'dict_keys'>
print(list(keys))#列表类型
print(tuple(keys))#元组类型
print('-'*60)
#获取字典中的value
val=d.values()
print(val,type(val))
#dict_values([101, 102, 103, 104]) <class 'dict_values'>
print(list(val))
print(tuple(val))
print('-'*60)
lst=list(d.items())
print(lst)#列表形式
d=dict(lst)
print(d)
print('-'*60)
#使用pop函数
print(d.pop('北京'))#选key值
print(d)#{'上海': 102, '天津': 103, '重庆': 104}
#随机删除一组键值对
print(d.popitem())
print(d)
#清除所有元素
#d=d.clear()
#print(d)
'''
字典生成式：
d={key:value for item in range}
d={key:value for key,value in zip(lst1,lst2)}
'''
import random  #随机产生随机数
d={item:random.randint(1,100) for item in range(5)}
print(d)#{0: 8, 1: 55, 2: 11, 3: 51, 4: 40}
#创建两个列表
lst1=[101,102,103]
lst2=['北京','上海','天津']
d={key:value for key,value in zip(lst1,lst2)}
print(d)#{101: '北京', 102: '上海', 103: '天津'}


