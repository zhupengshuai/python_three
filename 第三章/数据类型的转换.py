'''
类型转换包括 隐式转换和显示转换，其中隐式转换是无需其他函数就可自动转换数据类型，显示转换指通过函数来转换数据类型
常用的像是转换
1、int(x):将x转换为整数类型
2、float(x):转换成浮点数类型
3、str(x):转换成字符串
4、chr(x):将整数x转换成一个字符
5、ord(x):将字符x转换成其他对应得的整数值
6、hex(x):将十进制整数x转换成一个十六进制字符串
7、oct(x):将十进制整数x转换成一个八进制字符串
8、bin(x):将十进制整数x转换成一个二进制字符串
'''
x=10
y=3
z=x/y
print(z,type(z))#隐式转换
#float类型转换成int类型
print(int(3.14))#3
print(int(-3.14))#-3
print(float(3))#将int类型转换成float类型  3.0
print(int('20')+int('30'))#将字符串str转换整数int类型  20+30=50
print('---------------------------')
#chr（）和ord()
print(ord('宁'),ord('波'))#查找“宁”字的unicode中对应的整数值  23425 27874
print(chr(23425))#查找23425在unicode表中对应的字符  宁
print('-----------------------------')
print('进制之间的转换:')
print('十进制转换成十六进制：',hex(2024))#0x7e8
print('十进制转换成八进制：',oct(2024))# 0o3750
print('十进制转换成二进制：',bin(2024))# 0b11111101000
'''
eval函数的使用：
python的内置函数，用于去掉字符串最外侧的引号，并按照python语句方式执行去掉引号后的字符串
eval()函数经常和input()函数一起用
'''
s='3.14+4'
print(s,type(s))#输出的还是字符串
m=eval(s)#使用函数去掉s这个字符串中左右的引号，并执行加减运算
print(m,type(m))#7.140000000000001 <class 'float'>
print(round(m,2),type(m))#7.14 <class 'float'>
print('--------------------------------')
#常与input()函数一起使用，用来获取用户输入数值
age=eval(input('请输入你的年龄：'))#将字符串类型转换成整数型
print(age,type(age))#18 <class 'int'>
print('-----------------------------------')
school='宁波大学'#字符串类型
print(school)#宁波大学
print(eval('school'))#宁波大学
