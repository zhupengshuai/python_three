#字符串的索引规则以helloworld为例，从左到右是0-9，从右到左是-1——-10
s='HELLOWORLD'
print(s[0],s[-10])#索引0和10表示同一个字符“h"
print('宁波大学欢迎你'[3])
print('宁波大学欢迎你'[-4])
print(s[2:8])#索引从2到8且不包含8之间的字符：LLOWOR（正向索引）
print(s[-8:-2])#反向索引：LLOWOR
print(s[:5])#默认从0开始到5结束，不包含5：HELLO
#字符串常用的操作
print('--------------------------------------')
x='宁波大学'
y='科学技术学院'
print(x+y)#连接x和y两个字符串
print(x*10)#把x的字符串复制10次
print('宁波'in x)#true
print('杭州'in x)#false