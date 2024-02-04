'''
列表的相关操作：
1、lst.append(x):在列表lst最后增加一个元素
2、lst.insert(index,x):在列表中第index位置增加一个元素
3、lst.clear():清楚列表lst中的元素
4、lst.pop(index):将列表lst中第index位置的元素取出，并从列表中将其删除
5、lst.remove(x):将列表lst中出现的第一个元素x删除
6、lst.revrse(x):将列表lst中的元素反转
7、lst.copy():拷贝列表lst中的所有元素，生成一个新的元素
'''
lst=list('ningbodaxue')
print('原列表:',lst,id(lst))#输出原列表，并输出该列表的位置信息
#增加元素
lst.append('s')
print('增加后：',lst,id(lst))#增加元素后列表的位置信息不变
print('------------------------------------------------------------')
#在指定位置插入元素
lst.insert(1,100)#在序号1的位置插入元素100
print('插入后：',lst)
print('---------------------------------------------------------------------')
#删除列表中的元素
lst.remove('n')
print('去除后：',lst,id(lst))# 去除元素后，列表位置信息不变
print('---------------------------------------------------------------------')
#将索引元素取出并将其删除
lst.pop(1)
print(lst,id(lst))
#清除列表中的所有元素
#lst.clear()
#print(lst,id(lst))#将列表中的所用元素都清楚，并其位置信息不变
print('-'*60)
#列表的反向
lst.reverse()
print('反向后：',lst)
print('-'*60)
#列表的拷贝，产生一个新的列表
lst2=lst.copy()#将列表lst中的元素拷贝到lst2中，但两个列表的位置信息不一样
print(lst,id(lst))
print(lst2,id(lst2))
print('-'*60)
#列表元素的修改
lst[2]='20'#将列表序号2对应的元素改为20
print(lst)
'''
列表的排序方法：
1、列表对象的sort方法：
lst.sort(key=None,reverse=False):key是排序规则默认没有规则，reverse表示排序方式，默认升序
2、内置函数sorted()
sorted(iterable,key=None,reverse=False)  iterable是列表
'''
#sort方法
lst3=[3,0,6,7,5,4,1,0,3]
print(lst3,id(lst3))
#排序
lst3.sort()#默认升序
print('升序：',lst3)
lst3.sort(reverse=True)
print('降序：',lst3)
print('-'*60)
lst4=['Word','ppt','python','Matlab']
lst4.sort()#排序方式，先大写后小写
print(lst4)#['Matlab', 'Word', 'ppt', 'python']
print('-'*60)
lst4.sort(key=str.lower)#str.lower忽略大小写并进行排序
print(lst4)
#内置函数sorted()
lst5=[2,3,1,1,1,7,0,0,3,0]
print(lst5,id(lst5))
#排序
new_lst5=sorted(lst5)#升序
print(new_lst5,id(new_lst5))
print('-'*60)
up_lst5=sorted(lst5,reverse=True)#降序
print(up_lst5)
'''
列表生成式的语法结构
lst=[expression for item in range]

lst=[expression for item in range if condition]
'''
import random  #导入随机数
lst=[item for item in range(1,11)]
print(lst)
lst=[item*item for item in range(1,11)]
print(lst)
lst=[random.randint(1,100) for _ in range(10)]#随机产生10个1——100之间的随机数
print(lst)#[66, 2, 20, 48, 44, 36, 5, 9, 36, 18]
#使用if语句选择合适的元素组成新的列表
lst=[i for i in range(10) if i%2==0]#在0-10中是偶数的作为列表元素
print(lst)