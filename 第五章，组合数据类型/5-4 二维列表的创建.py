lst=[
    ['城市','环比','同比'],
    ['北京',10222,13567],
    ['上海',12345,45678],
    ['深圳',42678,56932]
]
print(lst)
#遍历二维列表使用双循环for
for row in lst:#行
    for item in row:#列
        print(item,end='\t')
    print()   #换行
#生成一个5行6列的二维列表
lst2=[[j for j in range(6)]for i in range(5)]
print(lst2)