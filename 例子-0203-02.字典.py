#coding=utf-8
dic={'name':'heygor','tel':18028768679}
dic1={'name':'gaga'}
#直接访问

print(dic)
#数据筛选
print(dic['name'])
print(dic['tel'])

#删除字典
dic={'name':'5kong','age':500}
print(dic)

del dic['age']
print(dic)
del dic
#print(dic)

dic={'name':'5kong','age':500}
print(dic)
dic.clear()
print(dic)

#字典的修改
dic={'name':'5kong','age':500}
dic['name']='tangsir'
print(dic)

#keys
dic={'name':'5kong','age':500}
print(dic.keys())
for i in dic.keys():
    print(i)
#values
dic={'name':'5kong','age':500}
print(dic.values())
for i in dic.values():
    print(i)
#items
dic={'name':'5kong','age':500}
print(dic.items())

for key,value in dic.items():
    print(key,value)






