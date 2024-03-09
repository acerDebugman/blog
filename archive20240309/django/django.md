## django使用
pip 先安装django

启动项目:
```
django-admin startproject mysite
python manage.py startapp report_module
python manage.py runserver 
```

解决没有找到_sqlite, 找到.sqlite3的.so文件,然后copy到lib-dynload目录中   
```
cp /usr/lib/python3.6/lib-dynload/_sqlite3.cpython-36m-x86_64-linux-gnu.so ~/.pyenv/versions/3.6.4/lib/python3.6/lib-dynload/
```

###安装mysql
安装mysql-connector就可以了!
```
pip install mysql-connector
pip install mysqlclient
```

###django中获取cursor进行sql直接执行

```
with transaction.atomic():
            cursor = connection.cursor()
            cursor.execute("select * from t_test_table")

```




