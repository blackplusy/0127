#coding=utf-8
#字符集相当于翻译官
#中文字符集 GBK2312
#1.直接输出
#字符串  '123' '扣你齐瓦'
print('123')
print(100)

#2.变量输出
#变量:可以变化的量
a='告诉你妈妈今天晚上不回家，我给你看我写的代码！'
#a就是变量的名字，等号后面是变量的值
print(a)
a=123
print(a)
#变量操作后输出
a=100
b=20
print(a+b)
a='100'
b='20'
print(a+b)
#函数输出
#abs()  绝对值
#len()  长度、元素个数
print(abs(-10))
a='塞朗黑有'
print(len(a))
#格式化输出
'''
%s 接受变量传来的字符类型数据
%d 接受变量传来的数值类型数据
如果传入的变量不止一个，一定要加括号
'''
name='heygor'
num=1
print('%s is %d'%(name,num))

name='lilei'
print('my name is %s' % name)









