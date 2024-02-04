'''
实战一：千年虫，在员工出生年分前加上19或20
'''
lst=[88,89,90,98,00,99]#表示员工的两位整数出生年份
print(lst)
#for循环遍历
for index in range(len(lst)):
    if str(lst[index])!='0':#str()将整数类型转化为字符串类型,判断列表数据是否为零，是的话前加200，不是前加19
        lst[index]='19'+str(lst[index])
    else:
        lst[index]='200'+str(lst[index])
print('修改后的年份列表：',lst)#['1988', '1989', '1990', '1998', '2000', '1999']
print('-'*60)
#使用enumerate()函数
lst1=[88,89,90,98,00,99]
for index,value in enumerate(lst1):
    if str(value) !='0':
        lst1[index]='19'+str(value)
    else:
        lst1[index]='200'+str(value)
print('修改后的年份列表：',lst1)
'''
实战二、京东购物流程
'''
#创建一个空列表用于存储商品信息
lst=[]
for i in range(5):#循环五次商品
    goods=input('请输入商品编号和商品名进行入库：')
    lst.append(goods)#将存入的商品存入空列表中
print('入库商品列表：',lst)
#输出所以商品信息
for i in lst:
    print(i)
#创建一个开空列表存储购物车中的商品
cart=[]
while True:#一直循环
    flag=False#代表没有商品的情况
    num=input('请输入要购买的商品：')
    #遍历商品列表，查询一下购买的商品是否存在
    for item in lst:
        if num==item[0:3]:#切片操作，切片商品的前四位编号
            flag=True
            cart.append(item)#将商品添加到购物车中
            print('商品已成功添加到购物车！')
            break#退出for循环
    if not flag and num!='q':
        print('商品不存在！')
    if num=='q':
        break#退出while循环
print('-'*60)
print('你购物车里已选的商品为：')
cart.reverse()
for item in cart:
    print(item)
