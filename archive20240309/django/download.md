# 使用django下载

思路: 
django后台输出使用StreamingHttpResponse(),直接读取文件,产生一个generator然后传给StreamingHttpResponse()就行!

参考可以使用

reference:
https://blog.csdn.net/u014686399/article/details/78198306
