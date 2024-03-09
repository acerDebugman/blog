#如何判断从客户端判断链接是客户端断开还是服务器断开?
应该根据客户端端口的状态,是4次挥手的哪一个状态?

#客户端如何判断链接是没连上,还是连接以后用户名密码等错误被拒接了


#链接超时是上层状态,也有可能是服务器检查链接太多,代码中控制直接断开了!



#如何控制链接数的方法:
客户端可以判断目前有多少个链接了,直接就不创建新的链接了!


参考:
https://blog.csdn.net/Swartz2015/article/details/61196159

#telnet 原理
执行一条telnet命令:
```
algo@algo-PC:~/PycharmProjects/blog/socket$ telnet dmp-api.cn.miaozhen.com 445
Trying 140.143.202.233...
Trying 140.143.199.25...
Trying 140.143.202.134...
Trying 140.143.202.186...
Trying 140.143.198.82...
telnet: Unable to connect to remote host: Connection timed out
```
