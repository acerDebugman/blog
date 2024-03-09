# python 安装
当下载完安装包后，建议直接就按照系统路径装，
否则在安装一些其他的依赖如opencv的时候不好指定python参数
```
mkdir .mypython3  #建议一般放到自己的home目录下,这样安装控制方便类似pyenv,也可以使用pyenv
cd .mypython3 
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

# pyenv 安装


centOs下可以顺序执行以下命令:
```
#!/bin/zsh
# pyenv install for CentOS 6.5 x86_64 
yum -y install git
yum -y install gcc make patch
yum -y install gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

//这部分东西会提示输出，将他们放到.bashrc里
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

python安装是安装在home目录的.pyenv目录中，修改pip源，安装后的配置文件：
```
algo@algo-PC:~/PycharmProjects/mooc$ cat ~/.pip/pip.conf 
[global]
trusted-host =  mirrors.aliyun.com
index-url = https://mirrors.aliyun.com/pypi/simple
#index-url = http://mirrors.aliyun.com/pypi/simple  #如果机器未安装openssl，可以改为使用http协议
```

pyenv的简单使用:
```
安装某一个版本的python:
pyenv install 3.6.4   //代表安装此版本python
pyenv versions
pyenv shell 2.7.6
pyenv global 2.7.6
pyenv versions
pyenv rehash
```
eg:  
[pyenv_media](!media/pyenv.png)


该目录下有一个.python-versions的文件，记录了内部的python版本号！


cd /home/data/application
pyenv local 3.6.2
就是将/home/data/application目录的python环境设置为python 3.6.2,如果是在该目录下执行python默认就会是3.6.2；
如果使用:
pyenv global 3.6.2
那么不论在哪一个目录执行都是3.6.2的python

在crontab -l 里或者在shell脚本里执行，要先的执行 source ~/.bashrc 才可以

reference:
https://gist.github.com/ysaotome/7956676
https://www.jianshu.com/p/05676f0cd0b5

