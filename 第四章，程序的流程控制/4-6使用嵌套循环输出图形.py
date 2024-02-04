'''
由*号组成的三行四列图形:
****
****
****
'''
print('------三行四列图形-------------')
for i in range(1,4):#对行数进行循环一共三行
    for j in range(1,5):#对列进行循环，一共四列
        print('*',end='')
    print()#空的print语句表示换行
print('------正向直角三角形------------')
'''
正向的直角三角形：
*
**
***
****
*****
******
'''
for i in range(1,7):#行循环一共有6行
    for j in range(1,i):#第一行一个*，第二行**，第三行***.......
         print('*',end='')
    print()
'''
*****
****
***
**
*
'''
print('-------到向直角三角形-----------')
for i in range(1,6):#一共有五行
    for j in range(1,7-i):#第一行有6-1个*、第二行有6-2个*、第三行由6-3个*........,故range(1,6-i+1)
        print('*', end='')
    print()
'''
正向等腰三角形：
&&&&*
&&&***
&&*****
&*******
*********
'''
print('---------等腰三角形-----------------')
for i in range(1,6):#一共五行
    #先画外围的由&组成的倒三角形
    for j in range(1,6-i):
        #print('&',end='')
        print(' ',end='')#将&换为空格
    #画*组成的等腰三角形
    for k in range(1,2*i):#第一行range(1,2)--*、第二行range(1,4)--***、第三行range(1,6)--*****........
        print('*',end='')
    print()
'''
9行菱形
&&&&*
&&&***
&&*****
&*******
*********
&*******
&&*****
&&&***
&&&&*
'''
print('---------9行菱形------------')
#先判断行数的奇偶性
row=eval(input('请输入菱形行数：'))
while row%2==0:#判断行数是否为偶数，如果是请重新输入输入
    print('请重新输入行数：')
    row=eval(input('请输入菱形行数：'))
#输出菱形
top_row=(row+1)//2#输出上半部分
for i in range(1,top_row+1):#一共五行
    #先画外围的由&组成的倒三角形
    for j in range(1,top_row+1-i):
        #print('&',end='')
        print(' ',end='')#将&换为空格
    #画*组成的等腰三角形
    for k in range(1,2*i):#第一行range(1,2)--*、第二行range(1,4)--***、第三行range(1,6)--*****........
        print('*',end='')
    print()
#画下部分
up_row=row//2
#先画&组成的正直角三角形
for i in range(1,up_row+1):#下半部分正直角三角形行数
    for j in range(1,i+1):
        print(' ',end='')
    #画下等腰三角形
    for k in range(1,2*up_row-2*i+2):
        print('*',end='')
    print()
print('---------空心菱形-----------')
#先判断行数的奇偶性
row=eval(input('请输入菱形行数：'))
while row%2==0:#判断行数是否为偶数，如果是请重新输入输入
    print('请重新输入行数：')
    row=eval(input('请输入菱形行数：'))
#输出菱形
top_row=(row+1)//2#输出上半部分
for i in range(1,top_row+1):#一共五行
    #先画外围的由&组成的倒三角形
    for j in range(1,top_row+1-i):
        #print('&',end='')
        print(' ',end='')#将&换为空格
    #画*组成的等腰三角形
    for k in range(1,2*i):#第一行range(1,2)--*、第二行range(1,4)--***、第三行range(1,6)--*****........
        if k==1 or k==2*i-1:#只有第一个和最后一个输出*，其他都输出空格
            print('*', end='')
        else:
            print(' ',end='')
    print()
#画下部分
up_row=row//2
#先画&组成的正直角三角形
for i in range(1,up_row+1):#下半部分正直角三角形行数
    for j in range(1,i+1):
        print(' ',end='')
    #画下等腰三角形
    for k in range(1,2*up_row-2*i+2):
        if k==1 or k==2*up_row-2*i+2-1:
            print('*', end='')
        else:
            print(' ',end='')
    print()
