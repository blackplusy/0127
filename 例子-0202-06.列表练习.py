#coding=utf-8

a=[1,2,3,4,5,6]
'''
for i in range(1,len(a)+1):
    print(a[-i],end="")    
'''

for  i in range(len(a)):
    print(a[len(a)-i-1],end="")
