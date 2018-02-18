# android安装  
deepin android安装，使用deepin的时候，真是舒服多了，直接在商店里安装android studio就可以了  
android 安装后，需要升级一下，升级到最新版本，直接以root身份执行脚本：
```
sudo sh /opt/android-studio/bin/studio.sh
```
启动后会显示一个小框，在event里选择升级，然后关掉以普通用户启动在启动就行


# adb 找不到手机问题
android已经开启了developer 模式　　
adb 需要手动启动，但是手动启动后，还是没发现连接的android实体机器, 
执行命令：
```
algo@algo-PC:~$ adb devices
List of devices attached

```
即使重启adb后也无反应：
```
algo@algo-PC:~$ adb kill-server
algo@algo-PC:~$ adb start-server
algo@algo-PC:~$ adb devices
List of devices attached

```
最后换了数据线，重启动adb就好了,查看到
```
algo@algo-PC:~$ adb devices
List of devices attached
92703380	unauthorized

```
在android stadio里就可以看到：  
![show-devices](./media/adb-device.png) 



reference:
http://blog.csdn.net/encourage2011/article/details/53525297
https://www.cnblogs.com/lswsqhy/p/7004530.html
https://www.linuxidc.com/Linux/2014-01/94931.htm
http://bbs.csdn.net/topics/392029387
https://www.jianshu.com/p/c9ab9f8b99e4
