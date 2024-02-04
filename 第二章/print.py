a=20#变量a的值为20
b=5
print(a*b)
print(a/b)
print('宁波大学欢迎你！')
print("宁波大学科学技术学院")
print('宁波大学','祝鹏帅',2311170030,"科学技术学院",'机械专硕')#并列输出不换行用”，“
print('b')
print(chr(98))#输出ACII码对应的的字符用'chr()'
print(chr(56))#ACII码中的56指的是数字8
#中文编码的范围是[u4e00,u9fa5]
#实例
print(ord('宁'))
print(ord('波'))
#分别输出对应’宁‘和’波‘字的ACII码
print(chr(23425),chr(27874))
#实例3 使用print函数打开文件
fp=open('note.txt','w')#打开文件'note.txt'
print('宁波大学欢迎你',file=fp)#将宁波大学欢迎你写入文件中
fp.close#关闭文件
#多条print函数输出结果一行显示
print('宁波大学',end='_')
print('欢迎你')
print('宁波大学'+'科学技术学院','23机械专硕'+'2311170030')#可以用‘+’将两个字符串连起来。
import keyword
print(keyword.kwlist)#查询保留字
print(len(keyword.kwlist))#自动计算数量