#coding=utf-8
#栈的方式访问列表
'''
l=[1,2,3,4]
print(l)
l.append(5)
print(l)
l.append(6)
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
'''
#获取列表索引
#index
l=['a','b','c','d']
print(l.index('c'))
#enumerate
l=['a','b','c','d']
for index,value in enumerate(l):
    print(str(index)+':'+str(value))
#排序
#reverse
l=[1,3,2,4]
print(l)
l.reverse()
print(l)
#sort
l=[1,3,5,2,4,6]
print(l)
l.sort()
print(l)
l=[1,3,5,2,4,6]
print(l)
l.sort(reverse=True)
print(l)

#insert和extend
l=['a','b','c']
l.insert(1,'d')
print(l)
l.insert(-1,'f')
print(l)


l=['a','b','c']
l.extend('d')
print(l)
l.extend([1,2,3])
print(l)
















