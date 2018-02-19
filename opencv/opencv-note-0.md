#opencv 初步认识
opencv是图像处理的一个库，内部内置了非常多的图形和图像处理的算法接库.  
ffmpeg是一个底层的视频处理编解码转换库,读取视频的时候，需要对每一帧图片的编解码进行转换,
转换后opencv才能拿到每一帧的图片，然后才可以利用opencv里的算法库进行处理，
opencv的具体操作依赖ffmpeg的编解码转换.

# opencv 安装
顺序执行以下命令:
```
apt-get install gtk2.0
apt-get install libgtk2.0-dev
apt-get install libv4l-dev
```
```
安装ffmpeg:
https://gist.github.com/xdamman/e4f713c8cd1a389a5917#file-install_ffmpeg_ubuntu-sh
直接执行脚本，如果执行脚本出问题可自己下载ffmpeg源代码安装：
cd ffmpeg/
./configure --enable-shared 
(或者当遇到-pIC的错误的时候, 执行:
./configure --enable-shared --disable-static
)
make
make install
```

安装其他依赖库
```
apt-get update
apt-get upgrade

apt-get install build-essential cmake pkg-config
apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev

apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
apt-get install libxvidcore-dev libx264-dev

apt-get install libgtk-3-dev

apt-get install libatlas-base-dev gfortran
```

```
cmake -D CMAKE_BUILD_TYPE=RELEASE \ 
-D CMAKE_INSTALL_PREFIX=/usr/local \ 
-D PYTHON3_EXECUTABLE=/usr/bin/python3 \ 
-D PYTHON_INCLUDE_DIR=/usr/include/python3.6 \ 
-D PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \ 
-D PYTHON3_NUMPY_INCLUDE_DIRS=/usr/local/lib/python3.6/dist-packages/numpy/core/include \ 
-D INSTALL_PYTHON_EXAMPLES=ON \ 
-D INSTALL_C_EXAMPLES=OFF \ 
-D OPENCV_EXTRA_MODULES_PATH=/home/algo/PycharmProjects/opencv_contrib/modules \ 
-D PYTHON_EXECUTABLE=/usr/lib/python3.6 \ 
-D BUILD_EXAMPLES=ON
```

or put them in one line :
```
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D PYTHON3_EXECUTABLE=/usr/bin/python3 -D PYTHON_INCLUDE_DIR=/usr/include/python3.6 -D PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so -D PYTHON3_NUMPY_INCLUDE_DIRS=/usr/local/lib/python3.6/dist-packages/numpy/core/include -D INSTALL_PYTHON_EXAMPLES=ON -D INSTALL_C_EXAMPLES=OFF -D OPENCV_EXTRA_MODULES_PATH=/home/algo/PycharmProjects/opencv_contrib/modules -D PYTHON_EXECUTABLE=/usr/lib/python3.6 -D BUILD_EXAMPLES=ON ../
```

result:
```
--   Python 3:
--     Interpreter:                 /usr/bin/python3 (ver 3.6.2)
--     Libraries:                   /usr/lib/x86_64-linux-gnu/libpython3.6m.so (ver 3.6.2)
--     numpy:                       /usr/local/lib/python3.6/dist-packages/numpy/core/include (ver 1.14.0)
--     packages path:               lib/python3.6/dist-packages
-- 
--   Python (for build):            /usr/bin/python3
-- 

```

# opencv安装后剩下的问题　
剩下的问题就是
PycharmProject无法识别  
import cv2  
这条语句中的cv2,但是在终端是可以识别的，
但是第二次在自动导入后，就可以了

# adb 安装  
参考android.md里的说明

# 安装摄像头驱动deepin安装摄像头驱动    
这个后续再解决


# 错误解决
在处理抓取摄像头视频的时候报错：
```
cv2.error: /io/opencv/modules/highgui/src/window.cpp:325: error: (-215) size.width>0 && size.height>0 in function imshow
```
这个错误的原因是imshow()没有video frame可以展示


# 安装luvcview (非必须安装，目前安装了也没用)
UVC：USB Video Class
luvcview 可以执行查看摄像头, 非必须安装for openCV
```
 apt-get install luvcview
 luvcview -d /dev/video0 -f jpg -s 640*480
```



# reference
https://www.zhihu.com/question/20822510
https://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html
https://docs.opencv.org/master/d2/de6/tutorial_py_setup_in_ubuntu.html
http://blog.csdn.net/vola9527/article/details/68958018
opencv official website：
https://docs.opencv.org/
opencv　python库:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv