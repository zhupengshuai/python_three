'''
算数运算符：
加法 +：1+1=2；减法 - ：1-1=0；乘法：2*3；
除法：10/2(浮点数的除法）；整除：10//3=3(只保留整数的除法）
取余：10%3=1（保留余数）；幂运算：2**4（2*2*2*2)
算数运算符的优先级：
第一级：**
第二级：*、/、%、//
第三级：+、-
'''

"""
赋值运算符：
简单的赋值：=
加赋值（+=）：x+=y相当于x=x+y
减赋值（-=）：x-=y相当于x=x-y
乘赋值（*=）：x*=y相当于x=x*y
处赋值（/=)：x/=y相当于x=x/y
取余赋值（%=）：x%=y相当于x=x%y
幂赋值（**=）：x**=y相当于x=x**y
整除赋值（//=):x//=y相当于x=x//y
"""
x=2
y=5
z=y//x
print(z)
x+=y
print(x)#7
x*=y
print(x,type(x))#5*7=35 <class 'int'>
m=2
n=3
y**=m
print(y)#25
y/=n
print(round(y,2),type(y))#8.33 <class 'float'>
#python支持链式赋值
print('--------------------------')
a=b=c=100
print('a=',a,'b=',b,'c=',c)#a= 100 b= 100 c= 100
#python支持系列解包赋值
a,b=20,30
print('a=',a,'b=',b)#a= 20 b= 30
print('-----如何交换两个变量的值----------')
a,b=b,a
print('a=',a,'b=',b)#a= 30 b= 20
'''
比较运算符
输出结果以布尔形式存在真就是True,假就是False
等于==     不等于！=    大于等于>=    小于等于<=
'''
print('----举例：------------')
print('60大于50码？',60>50)#60大于50码？ True
print('60大于50码？',60<50)#60大于50码？ False
print('60等于50码？',60==50)#60等于50码？ False
print('60大于等于50码？',60>=50)#60大于等于50码？ True
print('60不等于50吗？',60!=50)#60不等于50吗？ True
'''
逻辑运算符
and逻辑与：全真为真；or逻辑或：一真为真；not逻辑非:取反
'''
print('------and--------')
print(True and True)#True
print(True and False)#False
print(False and False)#False
print(False and True)#False
print(8>7 and 6>4)
print(8>7 and 6>5 and 4>5)
print(7>8 and 10/0)#False  因为10/0没有运算，当第一个表达式结果为False，直接输出结果
print('------or---------')
print(True or True)#True
print(True or False)#True
print(False or False)#False
print(False or True)#True
print('------not--------')
print(not True)#False
print(not False)#True
print(not 8>7)#False
'''
运算的优先级：
幂运算：**
取反、正号、负号：~、+、-
算数运算符：*、/、%、//
          +、-
位运算符中的左位移和右位移：>>、<<
位运算中的按位与：&
位运算中的异或：^
位运算中的按位或：|
比较运算符：<、<=、>、>=、！=、==
赋值运算符：=
'''
