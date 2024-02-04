'''
变量的作用域
是指变量起作用的范围，根据范围作用的大小可分为局部变量和全局变量
局部变量：
定义：在函数定义处的参数和函数内部定义的变量，作用仅在函数内部，函数执行结束，局部变量的生命周期也结束
全局变量：
定义：在函数外定义的变量或函数内部使用global关键词修饰的变量，作用于整个程序，程序运行结束，全局变量
的生命周期才结束
'''
#局部变量
def calc(a,b):
    s=a+b
    return s
#调用
#print(a,b,s) 会出错，因为a,b,c都属于局部变量，仅在函数内部使用，函数结束变量消失
re=calc(10,20)
print(re)#30
#全局变量
print('-'*60)
a=200#在函数外定义的变量叫做全局变量
def calc1(x,y):
    return a+x+y  #x,y属于局部变量
print(calc1(10,20))#230
print(a)#200  全局变量参与整个程序，所以可以输出
print('-'*60)
def calc2(m,n):
    d=100
    s=d+m+m
    return s
print(calc2(10,20))
#print(d)#NameError: name 'd' is not defined. 因为d是局部变量，故出函数就不能输出
print('-'*60)
def calc3(x,y):
    global s  #s虽然在函数内定义应该属于局部变量，但使用global关键词声明后，s变为全局变量
    s=300  #声明和赋值要分开执行
    return s+x+y
print(calc3(20,50))#370
print(s) #300
print(s*2) #600




