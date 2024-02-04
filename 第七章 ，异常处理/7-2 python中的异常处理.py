'''
python中的异常处理
1、try...except语法结构为：
try:
     pass(可能会抛出异常的代码）
except 异常类型：
     pass(异常处理代码，报错后执行的代码）
2、try...except...except的语法结构（可能会出现多种错误的语法结构）
try:
    pass(可能会抛出异常的代码）
except 异常类型A:
    异常处理代码
except 异常类型B:
    异常处理代码
'''
try:
    #可能会报错的代码
    num1=int(input('请输入一个整数：'))
    num2=int(input('请输入另一个整数：'))
    res=num1/num2
    print('结果为：',res)#当输入的是非整数或除数为0时，程序会报错
except ZeroDivisionError:
    print('出错！除数不能为0')



