fp=open('note.txt','w')
print('人生苦短，我用python',file=fp)
fp.close
#实战二
name=input('请输入你的姓名：')
age=input('请输入你的年龄：')
school=input('请输入你的学校：')
print('-------------自我介绍------------')
print('我的姓名是：',name)
print('我的年龄是：',age)
print('我的学校是：',school)