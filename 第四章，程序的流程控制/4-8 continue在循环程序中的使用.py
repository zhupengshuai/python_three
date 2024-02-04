'''
continue的作用是用于跳过本次循环的后续代码，而执行下一次循环操作，常与if搭配
'''
s=0
i=1
while i<=1000:
    if i%2==1:#判断奇数
        i+=1#在while循环中要改变变量
        continue#当i是奇数时就停止循环
    s+=i
    i+=1
print('偶数和:',s)
#使用遍历for循环
print('-------------------------------------')
s=0
for i in range(1,101):
    if i%2==1:
        continue
    s+=i
print('偶数和：',s)
'''
空语句pass,在语法结构中起到占位符作用，可以使语法结构完整不报错
'''
for i in range(10):
    pass#没有语句块，但不报错！