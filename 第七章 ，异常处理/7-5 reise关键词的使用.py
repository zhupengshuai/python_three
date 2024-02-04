'''
raise：抛出一个异常，从而提醒程序出现了异常情况，程序能够正确处理这些异常现象
语法结构：
raise[Exception类型（异常描述信息）]
'''
try:
    gender=input('请输入您的性别：')
    if gender!='男'and gender!='女':
        raise ValueError('性别只有男和女！！！')
    else:
        print('您的性别是：',gender)
except Exception as e:
    print(e)
