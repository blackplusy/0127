#coding=utf-8
#索引
name='im your papa'
print(name[0])
print(name[3])
print(name[-2])

#切片
name='im your papa'
print(name[0:4])
print(name[:4])
print(name[2:5])
print(name[3:-1])

#字符串的拼接
a='lady'
b='gaga'
print(a+b)
print(a+b[0])
'''
tel='0452-8869504'
print(tel[:5])
print(tel[5:])
print(tel[:5]+'6'+tel[5:])
'''
#字符串遍历
'''
name='im your papa'
for i in name:
    print(i)
'''
#去空格
''' 
strip()     去掉两边空格
lstrip()    去掉左边空格
rstrip()    去掉右边空格
'''
str1='   python   '
print(str1)
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())

#计算长度
str1='   python   '
print(len(str1))










