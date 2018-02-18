# ffmpeg 简介  



# ffmpeg 环境安装  
ffmpeg 安装的库非常的多，最基本的就是直接上官网或者github源码安装  
github address:
```
https://github.com/FFmpeg/FFmpeg
```
安装的ffmpeg的时候，注意指定：
```
./configure --enable-shared 
或者
./configure --enable-shared --disable-static
```
否则后面编译其他的项目的时候可能会遇到需要添加-PIC的错误

也可以直接本目录下的install_ffmpeg_ubuntu.sh脚本，但是不一定成功，不成功建议手动源码安装


