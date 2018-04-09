# druid 规则  


# bitmap位图索引技术 
FastBit位图索引技术


# segment过大的话,可以分partition
partition的话,配置partitionSpec参数就可以



# realtime实时消费kafaka
1. 在realtime节点的realtime.properties里配置
druid.plaintextPort=8084
druid.realtime.specFile=/home/data/applications/druid-online/conf/druid/realtime/kafka.json
2. 配置kafka.json文件,可以配置多个启动实例,内部都是kafka插件
kafka.json文件里是一个[]数组类型,配置了多少个实例,就会启动多少个kafka consumer去消费kafka

3. kafka插件,realtime节点的插件,启动的时候直接启动realtime节点,插件被启动去消费kafka数据


# 

reference:
https://blog.csdn.net/njpjsoftdev/article/details/52955638
