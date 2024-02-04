'''
位置参数：
是指调用时的参数个数和顺序必须与定义的参数个数和顺序相同
关键词参数：
是在函数调用时，使用“形参名称=值”的方式进行传参，传递参数顺序可以与定义时参数的顺序不同
默认值参数：
是在函数定义时，直接对形式参数进行赋值，在调用时如果该参数不传值，将使用默认值，如果该参数传值，
则使用传递的值。
'''
#定义一个函数
def happy_birthday(name,age):
    print('祝'+name+'生日快乐！！！')
    print(name+str(age)+'岁开心每一天！！')
#正确调用
happy_birthday('孙卉',22)#name是字符串类型，str(age)将字符串类型转为整数类型
#注意：位置参数的调用必须与形参的顺序和类型都完全相同
#关键字传参：
print('-'*60)
happy_birthday(age=22,name='孙卉')#使用关键字传参时，调用参数与形式参数顺序可以不同
print('-'*60)
happy_birthday('李白',age='1000')#调用时可以位置参数和关键字参数一起使用，但必须遵循未知参数在前，关键字参数在后，否则会报错
print('-'*60)
#默认值参数
def spring_festival(name='孙卉',age=22):  #默认值参数是指在定义函数时就定义好参数对象
    print('祝'+name+'新年快乐！！！')
    print(str(age)+'开心每一天！！！')
#调用
spring_festival()#使用默认参数后，调用时无需定义参数，就可使用默认值
# 祝孙卉新年快乐！！！
# 22开心每一天！！！
spring_festival('李哈')#使用默认值参数，调用时可以单独定义参数，则另一个参数就是默认值
print('-'*60)
spring_festival(age=22)
print('-'*60)
def fun(a,b=20):#使用默认值定义函数时，必须要求未知参数在前，关键词参数在后
    pass
#def fun2(a=20,b):
#     pass
'''
可变参数：
可变参数分为个数可变的位置参数和个数可变的关键字参数两种，
"个数可变的位置参数"是在参数前加一颗星(*para),para形式参数的名称，函数调用
时可接收任意个数的实际参数，并放到一个元组中。
"个数可变的关键词参数"是在参数前加两颗星（**para),在函数调用时可接收任意多个
“参数=值”形式的参数，并放到一个字典中。
'''
#个数可变的位置参数
def fun3(*para):#定义函数
    print(type(para))
    for item in para:
        print(item)#遍历参数元素
#调用
fun3(10,20,30)#*para可以接受多个参数
print('1'+'-'*30)
fun3(40)
print('2'+'-'*30)
fun3([1,2,3])
print('3'+'-'*30)
fun3(*[10,20,30,40])
#个数可变的关键字参数
print('-'*60)
#定义函数
def fun4(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'----->',value)
#调用
fun4(name='孙卉',age='22',height='160')#必须使用关键字参数调用
print('-'*60)
d={'name':'孙卉','age':'22','height':'160'}
#fun4(d)  错误调用
fun4(**d)#加**是解包操作
# <class 'dict'>
# name -----> 孙卉
# age -----> 22
# height -----> 160
