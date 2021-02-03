#coding=utf-8
#创建元组
tup=(1)
print(tup)
print(type(tup))


tup=(2,)
print(tup)
print(type(tup))

#访问元组
a=(1,2,3)
print(a)

for i in a:
    print(i)

if 1 in a:
    print('yes')

#元组的切片和索引
tup=(1,2,3,4,5)
print(tup)
print(tup[0])
print(tup[-2])
print(tup[3:])

#删除元组
tup=(1,2,3,4,5)
del tup
#print(tup)

#补充
tup=(1,2,3,4,5,3,3,3,3,3,3,3,3,3)
print(len(tup))
print(max(tup))
print(min(tup))
print(tup.index(5))
print(tup.count(3))








