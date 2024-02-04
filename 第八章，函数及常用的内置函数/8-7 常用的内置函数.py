'''
一、数据类型转换函数：
1、bool(obj) 获取指定对象obj的布尔值           2、str(obj) 将指定对象obj转换成字符串类型
3、int(x ) 将x转成int整数类型                 4、float(x) 将x转换成float浮点数类型
5、list(sequence) 将序列转为列表类型           6、tuple(sequence) 将序列转为元组类型
7、set(sequence) 降序列转为集合类型
'''
#bool()
print('非空字符串的布尔值',bool('hello'))
print('空字符串的布尔值：',bool(''))
print('空列表的布尔值：',bool([]),bool(list()))
print('空元组的布尔值：',bool(()),bool(tuple()))
print('空集合的布尔值：',bool(set()))
print('空字典的布尔值：',bool({}),bool(dict()))
print('-'*10,'str()','-'*10)
#str()
lst=[10,20,30,40]
print(lst,type(lst))#<class 'list'>
s=str(lst)
print(s,type(s))#<class 'str'> 字符串类型
#int()
print('-'*10,'int()','-'*10)
print(int(98.5))#98 整数类型没有小数点
print(int(98.5)+int('95'))#'95'是字符串类型  193
#print(int('98.5'))#ValueError: invalid literal for int() with base 10: '98.5'
print('序列转换--------------------------')
s='ningda'
print(list(s))#['n', 'i', 'n', 'g', 'd', 'a']
seq=range(1,11)
print(tuple(seq))
print(set(seq))
'''
二、常用的数学函数：
1、abs(x) 获取x的绝对值                2、divmod(x,y) 获取x与y的商和余数
3、max(seq) 获取seq的最大值            4、min(seq) 最小值
5、sum(iter) 对可迭代对象进行求和运算    6、pow(x,y) 获取x的y次幂
7、round(x,d) 对x进行保留d位小数，结果四舍五入
'''
print('绝对值：',abs(100),abs(-100),abs(0))
print('商和余数：',divmod(13,3))#商4余1
print('最大值：',max('hello'))
print('最大值：',max(20,30,40))
print('最大值：',min('hello'))
print('求和：',sum([10,20,30]))
print('2的3次幂：',pow(2,3))#8
print('四舍五入：',round(3.1415,2))#对3.1415保留两位小数 3.14
print('四舍五入：',round(312,-1))#对个位数进行四舍五入 310
'''
三、常用的迭代器操作函数
1、sorted(iter) 对可迭代对象进行排序
2、reversed(seq) 翻转序列生成新的迭代器对象
3、zip(iter1,iter2) 将两个列表打包成元组并返回一个可迭代的zip对象
4、enumerate(iter) 根据iter对象创建一个enumerate对象
5、all(iter) 判断可迭代对象iter中的所有元素的布尔值是否为True
6、any(iter) 同上，布尔值为False
7、next(iter) 获取迭代器的下一个元素
8、filter(fun,iter) 通过指定条件过滤序列并返回一个迭代器对象
9、map(fun,iter) 通过函数function对可迭代对象iter的操作返回一个迭代器对象
'''
#sorted()排序
lst=[54,56,8,42,23,89]
up_lst=sorted(lst)#升序
des_lst=sorted(lst,reverse=True)#降序
print('原列表：',lst)
print('升序：',up_lst)
print('降序：',des_lst)
print('-'*60)
#反向reversed（）
new_lst=reversed(lst)
print(type(new_lst))
print(lst)# [54, 56, 8, 42, 23, 89]
print(list(new_lst))# 转换成列表类型[89, 23, 42, 8, 56, 54]
print(tuple(lst))#转换成元组类型 (54, 56, 8, 42, 23, 89)
print('-'*60)
#zip()映射
x=['a','b','c','d','e']
y=[10,20,30,40,50]
zipobj=zip(x,y)
print(zipobj,type(zipobj))
#print(list(zipobj))#[('a', 10), ('b', 20), ('c', 30), ('d', 40), ('e', 50)]
print('-'*60)
#enumerate()
enum=enumerate(y,1)
print(tuple(enum))
print('-'*20,'all()','-'*20)
lst2=[10,56,'',20]
print(all(lst2))#False
print(all(lst))#True
print('-'*20,'next()','-'*20)
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))
#filter()
print('-'*60)
def fun(num):
    return num%2==1 #判断条件是否为真
obj=filter(fun,range(10))#filter(函数，数据)
print(list(obj))#[1, 3, 5, 7, 9]
print('map()','-'*50)
def fun2(x):
    return x.upper() #全部转为大写
#使用map()函数调用
new_lst2=['ningda','python','school']
obj2=map(fun2,new_lst2)
print(list(obj2))#['NINGDA', 'PYTHON', 'SCHOOL']

'''
四、常用的其他内置函数：
1、format(value,format_spec) 将value以formation_spec格式进行显示
2、len(s) 获取s的长度或s元素个数
3、id(obj) 获取对象的内存地址
4、type(x) 获取x的数据类型
5、eval(s) 执s这个字符串所表示的python代码
'''
print('format()','-'*40)
print(format(3.14,'20'))#左侧数据，右侧字符串数量。数据型默认为右对齐
print(format('python','20'))# 字符串类型默认为左对齐
print(format('hello','*<20'))#hello***************
print(eval('20+30'))#eval()将字符串类型转为整数类型并运算  50

