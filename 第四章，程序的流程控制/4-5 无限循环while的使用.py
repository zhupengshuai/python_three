answer=input('今天要上课吗？y/n')
while answer=='y':
    print('好好学习，天天向上！')
    answer=input('今天要上课吗?y/n')
print('-------计算1-100的累加和---------')
s=0#存储累加和
i=1#1、初始变量
while i<=100:#2、条件判断
    s+=i#3、语句块
    i=i+1#4、改变变量
print('累加和为：',s)
'''
无限循环whlie-else模式
'''
s=0#存储累加和
i=1#1、初始变量
while i<=100:#2、条件判断
    s+=i#3、语句块
    i=i+1#4、改变变量
else:
    print('累加和：',s)
#使用无限循环模拟用户输入密码
i=0
while i<3:
    user_name=input('请输入你的用户名：')
    pwd=input('请输入你的密码：')
    if user_name=='宁波大学' and pwd=='2311170030':
        print('系统登录成功！')
        i=4#退出循环
    else:
        if i < 2:  # 第一次输入错误
            print('输入错误你还有', 2 - i, '次机会')
        i+=1
if i==3:#当三次都输入错误时
    print('密码错误，您没有机会了')
#循环结构也可以互相嵌套，但不要嵌套太多