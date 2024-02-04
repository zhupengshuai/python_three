'''
格式化字符串的三种方式：
1、占位符：
%s:字符串格式/   %d: 十进制整数格式/   %f:浮点数格式
2、f-string
3、str.format()
'''
#使用占位符
name='祝鹏帅'#字符串类型
age=20#整数类型
score=99.5#浮点数类型
print('姓名：',name,'年龄：',age,'成绩：',score)
#姓名： 祝鹏帅 年龄： 20 成绩： 99.5
print('姓名:%s,年龄:%d,成绩:%f'%(name,age,score))
#姓名:祝鹏帅,年龄:20,成绩:99.500000
print('姓名:%s,年龄:%d,成绩:%.2f'%(name,age,score))
#姓名:祝鹏帅,年龄:20,成绩:99.50   %.2f是指成绩精确到小数点后两位
#f-string
print('1'+'-'*60)
print(f'姓名:{name},年龄:{age},成绩:{score}')
#姓名:祝鹏帅,年龄:20,成绩:99.5
#使用字符串format方法
print('姓名:{0},年龄:{1},成绩:{2}'.format(name,age,score))
#姓名:祝鹏帅,年龄:20,成绩:99.5
print('姓名:{1},年龄:{0},成绩:{2}'.format(name,age,score))
#姓名:20,年龄:祝鹏帅,成绩:99.5   0、1、2对应后面的排序
'''
format格式化字符串的详细格式(从左到右的格式）
:引导符号 /填充：用于填充单个字符/对齐方式：<左对齐、>右对齐、^居中对齐/宽度：字符串的输出宽度/
,：数字的千位分隔符/.精度：浮点数小数部分的精度或字符串的最大输出长度/类型：整数类型（b、d、o、x、X),
浮点数类型(e、E、f、%)
'''
s='helloworld'
print('{0:*<20}'.format(s))#字符串显示宽度为20，左对齐，空白部分用*填充
print('{:*<20}'.format(s))
print('{0:*>20}'.format(s))#右对齐
print('{0:*^20}'.format(s))#居中对其
print(s.center(20,'*'))#与format函数的对其方式相同
print('-'*60)
#千位分隔符（只适用于整数和浮点数）
print('{0:,}'.format(1002345621))#1,002,345,621
print('{0:,}'.format(1002345621.123))#1,002,345,621.123
#浮点数小数部分的精度
print('{0:.2f}'.format(3.1415926))#3.14  .2f是指精确到小数点后2位
print('{0:.5}'.format('helloworld'))#hello  .5是指最大输出长度
print('-'*60)
#整数类型
a=100
print('二进制：{0:b},十进制：{0:d},八进制：{0:o},十六进制：{0:x}'.format(a))
#二进制：1100100,十进制：100,八进制：144,十六进制：64
#浮点数类型
b=3.14159
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))
#3.14,3.14E+00,3.14e+00,314.16%
