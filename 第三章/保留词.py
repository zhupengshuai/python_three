import keyword
print(keyword.kwlist)
'''2525
实例3，变量的定义和使用
'''
luck_number=7#创建一个整型变量并赋值为7
my_name='祝鹏帅'# 字符串类型的变量
print(type(luck_number),type(my_name))#输出变量的的数据类型
print(my_name+'的幸运数字是：',luck_number)
#python动态修改变量的数据类型，通过付不同的值就可以直接修改
luck_number='宁波大学欢迎你！'
print(type(luck_number))#变量的数据类型：<class 'str'>（字符串）
#python允许许多个变量指向同一个值
mo=no=2024#两个变量都赋值为2024
print(mo,no)
print(id(no))#id()查看对象的内存地址
print(id(mo))#两个变量的内存地址相同
'''
实例4，整数的四种表现形式
'''
num=987#默认是十进制，表示整数
num2=0b1010101#0b代表二进制来表示整数
num3=0o765#0o代表使用八进制表示整数
num4=0x87ABF#0x代表使用十六进制表示整数
print(num,num2,num3,num4)
#浮点数类型的使用
height=187.3#<class 'float'>（浮点数）
print(height)
print(type(height))#查看数据类型
x=1.99E4#科学技术法的形式
print(x)
print('科学技术法：',x,'x的数据类型：',type(x))
print(0.1+0.2)#0.30000000000000004不确定位数问题
print(round(0.12+0.20,2))#结果保留两位小数：0.32
#复数类型的使用
m=123+456j
print('实部部分：',m.real)#real查看实部，imag查看虚部
print('虚部部分：',m.imag)
print('2+3')
print(eval('2+3'))
print('-----计算100-999之前的水仙花数--------')
#水仙花数：如153=3*3*3+5*5*5+1*1*1
