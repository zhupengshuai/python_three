'''
字符串拼接的几种方式：
1、使用str.join()方式进行拼接
2、直接拼接
3、使用格式化字符串进行拼接
'''
#使用+直接拼接
s1='hello'
s2='world'
print(s1+s2)
print('-'*60)
#使用字符串join()方法拼接
print(''.join([s1,s2]))#使用空字符拼接 helloworld
print('*'.join([s1,s2]))#使用*进行拼接  hello*world
print('-'.join(['python','java','php']))#python-java-php
#直接拼接
print('-'*60)
print('hello','world')
#使用格式化字符串拼接 接6-2
print('%s%s'%(s1,s2))#helloworld
print(f'{s1}{s2}')#helloworld
print('{0}{1}'.format(s1,s2))#helloworld
'''
字符串的去重操作
'''
s='hejdcbhbdchbcjbsakkcbb'
new_s=''
for item in s:
    if item not in new_s:
        new_s+=item#拼接操作
print(new_s)#hejdcbsak
#使用索引+not in
new_s2=''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2+=s[i]
print(new_s2)
#通过集合去重+列表排序
new_s3=set(s)
lst=list(new_s3)
lst.sort(key=s.index)
print(''.join(lst))




