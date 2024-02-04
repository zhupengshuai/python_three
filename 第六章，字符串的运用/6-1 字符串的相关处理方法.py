'''
字符串是python中的不可变数据类型：
字符串的常用操作：
1、str.lower() 将str字符串全部转为小写字母，结果为一个新的字符串
2、str.upper() 将str字符串全部转为大写字母
3、str.split(sep=None) 将str按照指定的分隔符sep进行分割，结果为列表类型
4、str.count(sub) 结果为sub这个字符串在str中出现的次数
5、str.find(sub) 查询sub这个字符串在str中是否存在，不存在结果为-1.存在，结果为sub首次出现的索引
6、str.index(sub) 功能find()相同，区别在于要查询的子字符串不存在时，程序报错
7、str.startswith(s) 查询字符串str是否以子串s开头
8、str.endswith(s) 查询字符串str是否已子串s结尾
9、str.replace(old,news) 使用news字符串替换字符串s中的old字符串，结果是一个新的字符串
10、str.center(width,fillchar) 字符串str在指定的宽度范围内居中，可以使用fillchar进行填充
11、str.join(iter) 在iter中的每个元素的后面都增加一个新的字符串str
12、str.strip(chars) 从字符串中去掉左右两侧chars中列出新的字符串
13、str.lstrip(chars) 去掉字符串左侧chars中列出的字符串
14、str.rstrip(chars) 去掉字符串右侧chars中列出的字符串
'''
#大小写转换
s='NINGBO'
low_s=s.lower()#转换成小写
print(s,low_s)#NINGBO ningbo
up_s=low_s.upper()#转换成大写
print(up_s)
print('-'*60)
#字符串的分隔
e_mail='zps@qq.com'
lst=e_mail.split('@')#将字符串从@进行分割
print('邮箱名：',lst[0],'邮件服务域名：',lst[1])#结果为列表形式
#统计次数
print('-'*60)
print(s.count('N'))#2
#检索操作
print(s.find('N'))#N字符串中首次出现的字符串位置
print(s.find('p'))#-1 没有找到
print(s.index('N'))
#print(s.index('p'))#ValueError: substring not found
print('-'*60)
#判断前缀和后缀，结果为布尔类型
#前缀
print(s.startswith('N'))#True
print(s.startswith('P'))#False
#后缀
print('text.txt'.endswith('.txt'))#True
#字符串的替换
print('-'*60)
s1='ningbodaxue'
new_s1=s1.replace('n','宁波',1)#count值替换次数，默认是全部替换
new2_s1=s1.replace('n','宁波')
print(new_s1,new2_s1)#宁波ingbodaxue 宁波i宁波gbodaxue
#字符串在指定的宽度范围内居中
print(s1.center(50))
print(s1.center(50,'-'))#_width指的自定字符串宽度，_fillchar指定空白部分的填充字符
#-------------------ningbodaxue--------------------
#去掉字符串左右两侧的字符
s2='     ningbo     daxue      '
print(s2)#     ningbo     daxue      \
print(s2.strip())#左右两侧 ningbo     daxue\
print(s2.lstrip())#左侧 ningbo     daxue      \
print(s2.rstrip())#右侧      ningbo     daxue\
print('-'*60)
#去掉指定字符
s3='he-helloworld-eh'
print(s3.strip('he'))
print(s3.lstrip('eh'))
print(s3.rstrip('he'))
'''
-helloworld-
-helloworld-eh
he-helloworld-
'''
#去掉的指定字符串与顺序无关

