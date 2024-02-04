'''
函数的返回值：
1、如果函数的运行结果需要在其他函数中使用，那么函数就应该被定义为带返回值的函数
2、函数的运行结果使用return关键词进行返回
3、return可以出现在函数中的任意一个位置，用于结束函数
4、返回值可以是一个值，或多个值，如果返回的值是多个，结果是一个元组类型
'''
def calc(a,b):#函数定义
    print(a+b)
#调用
calc(10,20)
print(calc(10,20))#None
print('-'*30)
def calc2(a,b):
    s=a+b
    return s
get_s=calc2(10,20)#存储到变量中
print(get_s)#30
get_s2=calc2(calc2(1,2),3)#1+2+3  先去执行calc2(1,2),结果为3，再去执行calc(3,3)
print(get_s2)#6
print('-'*60)
#返回值可以是多个
def get_sum(num):
    s=0
    odd_sum=0
    even_sum=0
    for i in range(1,num+1):
        if i%2!=0:#说明是奇数
            odd_sum+=i#奇数和
        else:
            even_sum+=i
    s+=i
    return s,odd_sum,even_sum
result=get_sum(20)
print(type(result))#<class 'tuple'> 元组类型
print(result)#(20, 100, 110)
#系列解包赋值
print('-'*30)
a,b,c=get_sum(30)
print(a,b,c)#30 225 240   将三个结构分别赋值给a、b、c


