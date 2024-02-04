'''
使用and连接多个判断条件，只有同时满足多个条件，才能执行if后面的语句块
'''
user_name=input('请输入您的用户名：')
pwd=input('请输入您的密码：')
if user_name=='zps'and pwd=='22190200':
    print('登陆成功！')
else:
    print('密码错误！')
'''
使用or连接多个判断条件时，只要满足多个条件中的一个就可以执行if后面的语句块
'''
score=eval(input('请输入你的成绩：'))#eval可将字符串类型转换成整数型
if score<20 or score>60:
    print('成绩有效')
else:
    print('成绩无效')