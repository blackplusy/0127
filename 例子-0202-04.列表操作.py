#coding=utf-8
#直接访问
l1=[1,2,3,4]
print(l1)
#遍历访问
l1=['kobe','rose','james']
for i in l1:
    print(i)
#成员访问
l1=['kobe','rose','james']
if 'kobe' in l1:
    print('yes')
#索引和切片
l=['张飞','马超','云云','黄忠','2爷']
print(l[3])
print(l[-4])
print(l[2:4])
print(l[:-1])

#列表的拼接
l=[1,2,3]
m=['a','b']
print(l+m)

#列表的修改
l=[1,2,3]
print(l)
l[2]='柳岩'
print(l)
l[-1]='刘亦菲'
print(l)

#列表的删除

l=[1,2,3]
print(l)
del l[2]
print(l)










