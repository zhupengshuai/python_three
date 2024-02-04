'''
集合的操作方法：
1、s.add(x): 如果x不在集合s中，则将x添加到集合s中
2、s.remove(x): 如果x在集合中，将其删除，如果不在集合中，程序报错
3、s.clear(): 清楚集合中所以元素
'''
s={10,20,30,40}
#向集合中添加元素
s.add(50)
print(s)#{40, 10, 50, 20, 30} 集合元素是无序的
#删除元素
s.remove(10)
print(s)#{40, 50, 20, 30}
#清空集合中所用元素
s.clear()
print(s)#空集合set()
print('-'*60)
#集合的遍历操作
s1={10,20,30,40}
for i in s1:
    print(i)
#使用enumerate()函数 接5-2
for index,item in enumerate(s1):
    print(index,'---->',item)#index是集合元素序号
print('-'*60)
#集合的生成式
s={i for i in range(1,10)}
print(s)
s={i for i in range(1,11) if i%2==1}#在1-10里是奇数的输出
print(s)#{1, 3, 5, 7, 9}
'''
列表、元组、字典、集合的区别 （接5-4)
数据类型		序列类型		元素是否可重复		是否有序		定义符号		
列表list		可变序列		可重复		有序		[]		
元组tuple		不可变序列		可重复		有序		()		
字典dict		可变序列		key可重复，value不了重复		无序		{key:value}		
集合set		可变序列		不可重复		无序		{}	
'''
lst=[
    ['数据类型','序列类型','元素是否可重复','是否有序','定义符号'],
    ['列表list','可变序列','可重复','有序','[]'],
    ['元组tuple','不可变序列','可重复','有序','()'],
    ['字典dict','可变序列','key可重复，value不了重复','无序','{key:value}'],
    ['集合set','可变序列','不可重复','无序','{}']
]
for row in lst:#行
    for item in row:#列
        print(item,end='\t\t')
    print()   #换行
