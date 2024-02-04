'''
A,B两个设备之间的信息传递是靠二进制编码bytes作为介质，即字符串str--->bytes称为编码，
bytes--->str为解码。
编码str--->bytes使用encode() 语法格式：
str.encode(encoding='utf-8',errors='strict/ignore/replace')
解码bytes--->str使用decode() 语法格式：
bytes.decode(encoding='utf-8',errors='strict/ignore/replace')
'''
#编码encode()
s='社会主义核心价值观'
scode_utf=s.encode('utf-8',errors='replace')#默认使用utf-8编码器
print(scode_utf)#转化成二进制是27位，因为用utf-8编码的一个中文占三个字节
scode_gbk=s.encode('gbk',errors='replace')
print(scode_gbk)#同上，二进制是18位，用gbk编码是一个中文占两个字节
#编码中出错的问题
print('-'*60)
s2='耶耶，❤'
#scode=s2.encode('gbk',errors='strict') 出现无法编码的字符串会报错
scode1=s2.encode('gbk',errors='ignore')#b'\xd2\xae\xd2\xae\xa3\xac' 遇到无法编码的字符串会不在编写
scode2=s2.encode('gbk',errors='replace')#b'\xd2\xae\xd2\xae\xa3\xac?' 遇到无法编码的字符串会出?
#print(scode)
print(scode1)
print(scode2)
#解码
print('-'*60)
#解码的编码器要与与之对应的编码的编码器相同
print(bytes.decode(scode_utf,'utf-8'))
print(bytes.decode(scode_gbk,'gbk'))
#社会主义核心价值观
'''
数据验证：数据的验证是指程序对用户输入的数据进行“合法”性验证
str.isdigit() 所有字符都是数字(阿拉伯数字)
str.isnumeric() 所有字符都是数字
str.isalpha() 所有字符都是字母（包含中文字符）
str.isalnum() 所有字符都是数字或字母（包含中文字符）
str.islower() 所有字符都是小写
str.isupper() 所有字符都是大写
str.istitle() 所以字符都是首字母大写
str.isspace() 所有字符都是空白字符
'''
#.isdigit()十进制的阿拉伯数字
print('123'.isdigit())#true
print('一二三'.isdigit())#false
#.isnumeric()
print('一二三'.isnumeric())#True
print('壹贰叁'.isnumeric())#True
print('-'*60)
#判断是否都是空白字符
print('\t'.isspace())#True
print(' '.isspace())#True
print('\n'.isspace())#True

