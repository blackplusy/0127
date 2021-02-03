#coding=utf-8


dic1={'heygor':'123','keyao':'456','zhi':'123'}
while 1:
    name=input('请输入用户名:')
    if name in dic1.keys():
        print('yes')
        while 1:
            passwd=input('请输入密码:')
            if dic1[name]==passwd:
                print('登录成功')
                break
            else:
                print('您的密码有误~')
        break
            
    else:
        print('用户名输入错误，请重新输入')
