#可能出现多种错误的异常处理情况
try:
    num1 = int(input('请输入一个整数：'))
    num2 = int(input('请输入另一个整数：'))
    res = num1 / num2
    print('结果为：', res)
except ZeroDivisionError:
    print('出错！除数不能为0')
except ValueError:
    print('出错！不能将字符串转为整数')
except BaseException:
    print('未知异常！！')