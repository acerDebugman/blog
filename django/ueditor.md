# 下载uditor

# 下载并且安装该django app
```
https://github.com/twz915/DjangoUeditor3
```

安装方法:
```
* 方法一：将github整个源码包下载回家，在命令行运行：
	python setup.py install
* 方法二：使用pip工具在命令行运行(推荐)：
    pip install DjangoUeditor
```

配置setting 文件
将这个DangoUeditor3中的DjangoUeditor这个app内容copy到自己的项目下新建的app中,然后修改自己项目setting.py文件,
加入:
```
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static").replace('\\','/')
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media").replace('\\','/')
```
全局urls.py中加入:
```
from django.conf.urls import url,include
from django.contrib import admin
from .settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include("ueditor.urls")),
    url(r'^media/(?P<path>.*)$',serve, {'document_root': MEDIA_ROOT}),
]
```

期间遇到返回的jsonp问题,需要在python端加代码:
```
return HttpResponse("(" + json_data + ")", content_type="application/javascript")

原来的是:
return HttpResponse(json_data, content_type="application/javascript")
```





