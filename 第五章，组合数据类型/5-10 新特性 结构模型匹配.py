'''
结构模型匹配  接4-2
语法结构：
1、match data:             2、字典合并运算符|
    case{}:
      pass
    case[]:
      pass
    case():
      pass
    case_:
      pass
3、同步迭代：
match data1,data2:
   case data1,data2:
         pass
'''
data=eval(input('请输入要匹配的数据：'))
match data:
    case{'ningbo':20,'xingtai':30}:
        print('字典')
    case [20,30,40,50]:
        print('列表')
    case (10,20):
        print('元组')
    case _:
        print('都不匹配')
#合并字典的运算符
d1={'学号':22190200}
d2={'学位':'专硕'}
com_dict=d1|d2
print(com_dict)#{'学号': 22190200, '学位': '专硕'}
#同步迭代
fruits=['apple','banana','orange','grape']
counts=[10,5,6,25]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',10:
            print('十个苹果')
        case 'banana',5:
            print('5个香蕉')
        case 'orange',6:
            print('6个橘子')
        case 'grape',25:
            print('25个葡萄')
