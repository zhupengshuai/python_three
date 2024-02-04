'''
遍历循环for结构
'''
#遍历字符串
for i in 'hellonm':
    print(i)
print('-------------------')
#range()函数产生一个[n,m)的整数序列，包含n不包含m
for i in range(1,13):
    if i%2==0:
        print(i,'是偶数')
    else:
        print(i,'是奇数')
print('-------计算1-10的累加和')
s=0
for i in range(1,11):
    s+=i#相当于s=s+i
print(s)#s=55
print('-----计算100-999之前的水仙花数--------')
#水仙花数：如153=3*3*3+5*5*5+1*1*1
for i in range(100,1000):
    a=i%10#获取个位数字
    b=i//10%10#获取十位数字
    c=i//100#获取百位数字
if i==pow(a,3)+pow(b,3)+pow(c,3):#水仙花数
   print(i)
