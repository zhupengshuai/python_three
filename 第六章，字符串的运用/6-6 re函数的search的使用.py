import re
pattern='\d.\d+' #规则模块
s='I study python 3.12 every day ,python 2.7 i love you'
s2='4.0 python I study everyday'
s3='I study python every day'
match=re.search(pattern,s)
match2=re.search(pattern,s2)
match3=re.search(pattern,s3)
print(match)# search函数只能找到第一个数字
print(match2)
print(match3)#None 没有查找到
#输出查找的内容
print(match.group())#3.12
print(match2.group())#4.0
'''
re模块的findall()函数的使用 结果是列表类型
'''
print('-'*60)
lst=re.findall(pattern,s)
lst2=re.findall(pattern,s2)
lst3=re.findall(pattern,s3)
print(lst)#['3.12', '2.7']
print(lst2)#['4.0']
print(lst3)#[]
'''
sub函数和split函数的使用
'''
#sub函数
s='我想用python爬虫，去反扒网上的黑客vip视频'
pattern='黑客|爬虫|反扒'
new_s=re.sub(pattern,'**',s)#repl:'**' 是指将规则敏感词语换做**
print(new_s)#我想用python**，去**网上的**vip视频
print('-'*60)
#split()函数
s2='https://www.baidu.com/s?wd=github&rsv_spt=1&rsv_iqid'
pattern2='[?|_]'
new_s2=re.split(pattern2,s2)
print(new_s2)#['https://www.baidu.com/s', 'wd=github&rsv', 'spt=1&rsv', 'iqid']
#从?和_处进行分隔，输出结果是列表类型



