#django使用   
一对多:
```
goods = models.ForeignKey(Goods, name="goods", relatived_name="abc", db_column="goods_id")
```
related_name是用在1拿取多个相关对象对的时候
例如刚才的对象时写在Campagn model里的,在goods的model里用:goods.abc.all()就可以拉到所有的campaigns
#django问题  



