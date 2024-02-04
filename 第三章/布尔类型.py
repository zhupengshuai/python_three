'''
布尔类型一般用True和False表示，True表示1，False表示0，
布尔值为False的情况如下：
1、False或者None
2、数值中的0，包含0,0.0，和虚数0
3、空序列，包含空序列字符串、空元组、空列表、空集合
4、自定义对象的实例，该对象的_bool_()方法返回False_Len_()犯法返回0
'''
x=True
print(x)
print(type(x))#字符串类型<class 'bool'>
print(False+10)#0+10=10
print(x+10)#1+10=11
print('---------------------------------')
print(bool(10))#测试一下整数10的布尔值 True
print(bool(0),bool(0.0))#False
#非0整数的布尔值都为True
print(bool('宁波大学'))#true
print(bool(''))##false
#所有非空字符串的布尔值都为True
print(bool(False))
print(bool(None))#参见头提示1


