'''
接视频p71
re模块
python中的内置模块，用于实现python的正则表达式
1、re.match(pattern,string,flags=0) 用于从字符串的开始位置进行配置，如果起始位置匹配成功
，结果为match对象，否则结果为None
2、re.search(pattern,string,flag=0) 用于在整个字符串中搜索第一个匹配值，如果匹配成功，结果
为match对象，否则为None
3、re.findall(pattern,string,flag=0) 用于在整个字符串搜索所有符合正则表达式的值，结果是一个
列表类型
4、re.sub(pattern,string,flag=0) 用于实现对字符串中指定子串的替换
5、re.split(pattern,string,flag) 字符串的split()方法功能相同，都是分隔字符串
'''
import re #导入re模块
pattern='\d.\d+' #匹配模版 +限定符，\d 指的是0-9数字出现一次
s='I study python 3.12 every day'#待匹配字符串
match=re.match(pattern,s,re.I) #re.I指的是忽略大小写
print(match)# None match模式是从头开始匹配，\d指的是数字，开头没有数字所以没有找到
s2='3.11python I study every day'
match2=re.match(pattern,s2)
print(match2)#<re.Match object; span=(0, 4), match='3.11'>
print('-'*60)
print('匹配的起始位置：',match2.start())
print('结束位置：',match2.end())
print('匹配区间的位置元素：',match2.span())
print('待匹配的字符：',match2.string)
print('匹配数据：',match2.group())


