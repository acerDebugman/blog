# 
#opencv 常用API
imread(img_path)    //图片读取
imwrite(img_path, img)  //图片保存
imshow(name, img)   //显示图片
waitKey(time_ms)    //传入时间是表示delay多少秒返回，可以用来等待输入，也可以用来控制视频图片播放的速度
```
ret, frame = capture.read()
frame = cv.flip(frame, 1)
cv.imshow("video", frame)
c = cv.waitKey(30) //30ms 返回，可以用来控制视频播放的速度，如24帧每秒是正常的播放速度，那么1000/24=41.6，41ms/帧 设置delay(41)视频播放正常
if c == 27:
            break
```

VideoCapture(video_path_or_device_num)      //参数是video的路径或者摄像头路径

flip(frame, flipCode) //
eg:
```
frame = cv.flip(frame, 1)
```
