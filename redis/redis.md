# 创建新的redis集群

```
./src/redis-trib.rb create 127.0.0.1:6379 127.0.0.1:6380 127.0.0.1:6381 127.0.0.1:6382 127.0.0.1:6383 127.0.0.1:6384  #创建所有都是主的节点
./src/redis-trib.rb create --replicas 1 127.0.0.1:6379 127.0.0.1:6380 127.0.0.1:6381 127.0.0.1:6382 127.0.0.1:6383 127.0.0.1:6384  #创建有主从的节点,从节点是随机安排的, 主节点必须要有>=3个才能创建集群
./src/redis-trib.rb add-node --slave --master-id f54b256ec33064ebac1aad0600fc2f64da777536 127.0.0.1:6385 127.0.0.1:6382          #增加新的节点,最后一个必须指定已经存在的节点
```
