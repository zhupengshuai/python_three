#if.....else
num=eval(input('请输入你的中奖号码：'))
if num==123:
    print('恭喜发财！')
else:
    print('谢谢惠顾！')
print('----简化方法--------')
res='恭喜发财！'if num==123 else'谢谢惠顾！'
print(res)
print('-------------------')
print('恭喜发财！'if num==123 else'谢谢惠顾！' )
#多分支结构
wighte=eval(input('请输入你的体重：'))
if 0<wighte<60:
    print('偏瘦')
elif 60<=wighte<100:
    print('正常')
elif 100<=wighte<120:
    print('偏重')
elif 120<=wighte<150:
    print('超重')
#嵌套if语句使用
print('-------嵌套if语句使用-------')
answer=(input('请问你喝酒了吗？'))
if answer=='he':
    proof=eval(input('输入酒精含量：'))
    if proof<=20:
        print('不构成酒驾，可以开车')
    elif proof<=80:
        print('请不要开车，经构成酒驾')
    else:
        print('已形成醉驾，你已犯法')
else:
    print('可以走了')
#模式匹配，match....case结构
print('--------------------------------------')
score=input('请输入你的等级：')
match score:
    case 'a':
        print('优秀')
    case 'b':
        print('良好')
    case 'c':
        print('中等')
    case 'd':
        print('不及格')

