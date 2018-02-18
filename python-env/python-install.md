# python 安装
当下载完安装包后，建议直接就按照系统路径装，
否则在安装一些其他的依赖如opencv的时候不好指定python参数
```
tar xvf Python-3.6.4.tar.xz
cd Python-3.6.4
configure
make
make install
```
接着用刚才的安装执行命令python3.6执行get-pip.py安装pip,
这样pip才能够将要安装的文件安装到指定python lib的site-package里
```
python3.6 get-pip.py
```


