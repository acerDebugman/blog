#django使用   
一对多:
```
goods = models.ForeignKey(Goods, name="goods", relatived_name="abc", db_column="goods_id")
```
related_name是用在1拿取多个相关对象对的时候
例如刚才的对象时写在Campagn model里的,在goods的model里用:goods.abc.all()就可以拉到所有的campaigns

所以OneToMany只用设置到many的一端,one的一端也可以通过related_name获取到many的对象:
```
class User(models.Model):
    pass
class Reports(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE,related_name="reports",db_column="creator_id")
```

用法:
```
u=Reports.objects.filter(id=9).first()
u.reports   #这个reports是related_name, 并且返回的是objects, 即
```

#django问题  
QuerySet 的理解
1. 执行流程?

u = User.object.all()
u.save()
u.delete()

u.name="joe zhang"
u.save()  #equals to update

查看测试用例来进行学习 __in 等操作了!
reference:
https://github.com/django/django/blob/master/tests/or_lookups/tests.py


# model转为dict, 可以使用方法model_to_dict
在类里:
```
from django.forms.models import model_to_dict

user_dic = model_to_dict(user, fields=["id", "name", "email"])  # 转为了dict
```

查看该用法可以看到chain的使用! 多看看别人怎么转的


# 

