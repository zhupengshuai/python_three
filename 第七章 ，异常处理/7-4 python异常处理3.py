'''
3、try...except...else的语法结构：
try:
    可能会抛出异常的代码
except 异常类型：
    异常处理代码（报错后执行的代码）
else:
    没有抛异常要执行的代码
4、try...except...else...finally的语法结构：
try:
    可能会抛出异常的代码
except 异常类型：
    异常处理代码（报错后执行的代码）
else:
    没有抛异常要执行的代码
finally:
    无论是否产生异常都要执行的代码
'''
#try...except...else的语法结构：
try:
    num1 = int(input('请输入一个整数：'))
    num2 = int(input('请输入另一个整数：'))
    res = num1 / num2
   # print('结果为：', res)
except ZeroDivisionError:
    print('出错！除数不能为0')
except ValueError:
    print('出错！不能将字符串转为整数')
except BaseException:
    print('未知异常！！')
else:
    print('结果为：', res)#最后执行结果
print('-'*60)
#try...except...else...finally的语法结构：
try:
    num1 = int(input('请输入一个整数：'))
    num2 = int(input('请输入另一个整数：'))
    res = num1 / num2
   # print('结果为：', res)
except ZeroDivisionError:
    print('出错！除数不能为0')
except ValueError:
    print('出错！不能将字符串转为整数')
except BaseException:
    print('未知异常！！')
else:
    print('结果为：', res)
finally: #无论是否产生异常都要执行的代码
    print('程序执行结束！！')


