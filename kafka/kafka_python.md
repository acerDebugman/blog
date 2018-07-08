#kafka with python

kafka的python客户端:
```
pip install kafka-python
```





#kafka



# kafka消费的时候注意的问题
1. kafka本身是会删除日志的,当过期的日志被删除的时候,客户端消费的时候如果制定的offset日志被删除了,consumer会自动更新到最新的offset来,这样就可能会造成堵塞,需要去设置consumer的消费超时时长
2. next()也去迭代的时候也是会堵塞的!
3. 分清楚问题的消费消息的时候知道做到了哪一步,kafka的offset可以自己记录,也可以使用commit方法同步到server,让服务器给你记住你这个consumer的offset是多少! 两种方法都可以的!
自己记住和使用服务器的方式都可以的!


# kafka 的使用低级api自己记录offset如何保证多个consumer同时运行?
多个consumer的消费同一个topic和partition时候,使用 (topic, partition) 作为key,value是offset;    
(topic, partition), offset 的键值对放到redis里,但是如果让多个consumer去并发消费一个partition里的消息呢?  
思考:  
1.同一时刻只有一个consumer消费? 
2.同时有多个consumer消费?





