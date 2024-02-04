'''
序列是一个用于存储多个值的连续空间，每个值都对应一个整数编号，成为索引，
索引分为正向递增索引和反向递减索引
正向递增是从0——n-1,反向递减是从-1——-n
'''
s='ningbodaxue'
for i in range(0,len(s)):#len()可自动识别字符串长度
    print(i,s[i],end='\t\t')#i代表字符串对应字符的编号，s[i]表示该编号的字符
print('--------------------------------')
for i in range(-11,0):
    print(i,s[i],end='\t\t')
print('----------------------------------------------')
'''
切片操作的语法结构：
序列[开始：结束：步长]
'''
m='zhongguokuangyedaxue'
n=m[0:6:1]#从z开始，到u结束，但不包含u，步长为1
print(n)
print(m[:9:2])#zoguk,默认从0开始，到编号9结束，不包含编号9，步长为2
print(m[:9:])#zhongguok  默认从编号0开始，步长为1，到编号9结束，但不包含9
print(m[0::2])#zogukageau 默认索引到结尾
print(m[5::])#guokuangyedaxue
print(m[5:])#guokuangyedaxue  两者结果相同
#反向索引
print(m[-1::-1])#euxadeygnaukouggnohz
print('----------------------------------------------')
'''
序列的相加和相乘操作:
相关操作函数：
1、x in s :如果x是s的元素，结果为true,不是则为false
2、x not in s:与上一个相反
3、len(s):计算序列s中元素个数
4、max(s):索引序列s中元素的最大值
5、min(s):最小值
6、s.index(x):序列s中第一次出现元素x的位置
7、s.count(x):序列s中出现x的总次数
'''
s='hello'
v='ningbo'
print(s+v)#helloningbo
print('---------------------------------------')
#序列的相乘操作
print(s*3)#s字符串乘3
print('----------------------------------')
#序列相关函数操作
u='ningbodaxue'
print('o在u中存在吗',('o'in u ))#True 存在为真，不存在为假
print('f在u中存在吗',('f'in u ))#False
print('f在u中存在吗',('f'not in u ))#True  不存在为真，存在为假
print('--------------------------------------')
print(len(u))
print(max(u))#x
print(min(u))#a
print(u.index('g'))#检索g在序列u中的编号 3
print(u.count('n'))#检索n在序列u的出现次数 251q

