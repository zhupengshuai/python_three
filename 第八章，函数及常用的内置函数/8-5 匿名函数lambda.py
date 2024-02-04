'''
匿名函数lambda
是指没有名字的函数，这种函数只能使用一次，一般是在函数的函数体只有一句代码且只有一个返回值时，
可以使用匿名函数来简化。语法结构：
result=lambda 参数列表：表达式
'''
#定义函数
def calc(a,b):
    return a+b
print(calc(10,20))
#匿名函数的定义
print('-'*30)
s=lambda a,b:a+b #a,b是参数列表，a+b是表达式
print(type(s))#<class 'function'> 函数类型
#匿名函数的调用
print(s(10,20)) #30
print('-'*30)
#列表的正确遍历
lst=[10,20,30,40]
for i in range(len(lst)):
    print(lst[i])
print()#换行操作
#使用匿名函数遍历
for i in range(len(lst)):
    result=lambda x:x[i]# x是形式参数
    print(result(lst))#lst是实际参数
print('-'*60)
#使用匿名函数的成绩排序
student_score=[
    {'name':'张三','score':100},
{'name':'李四','score':85},
{'name':'李白','score':110},
{'name':'王五','score':65},
{'name':'王伟','score':60}
]
student_score.sort(key=lambda x:x.get('score'),reverse=True)#降序
print(student_score)


