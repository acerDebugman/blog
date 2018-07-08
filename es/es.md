#document, index 和 shards, replicas
document是es存储数据的基本格式单元
index数据结构是给documents提供indexing,search,update,delete等,使用一个name来标识
index结构推测是和索引等有关系

shards是index分片的, 为了避免单点使用replica作为shard的备份, 但是单元是按index来设置的,
例如一个index有5个primary shard和1个replica, 就意味着有5个主shard和5个备份的replica shard.

分布式方式整体来说和kafka比较类似, kafka是已partition为单位的,每个partition可以有多个replica分布,
比如一个:
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 3 --topic test
创建3分区和每个分区3个副本

#一致性算法是
看起来是和kafka一致的算法,应该是raft, 有一个主,多个从


#常用api
样例eg:
curl -X GET "localhost:9200/_cat/indices?v"

```
GET /_cat/health?v
GET /_cat/nodes?v
GET /_cat/indices?v
```

健康检查:
Recall from our previous discussion that yellow means that some replicas are not (yet) allocated.
The reason this happens for this index is because Elasticsearch by default created one replica for this index. Since we only have one node running at the moment, that one replica cannot yet be allocated (for high availability) until a later point in time when another node joins the cluster. Once that replica gets allocated onto a second node, the health status for this index will turn to green.

按照默认配置replicas的数量是1的时候,但是机器节点数据只有一个,所以没有什么用


创建一个index:
```
curl -X PUT "localhost:9200/customer?pretty"  
```

创建一个doc,就是将文档内容放入es中:  
```
curl -X PUT "localhost:9200/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
  "name": "John Doe"
}
'
或者:
curl -X PUT "localhost:9200/algo/_doc/1?pretty" -H "Content-Type:application/json" -d @sample.json
```
说明:
It is important to note that Elasticsearch does not require you to explicitly create an index first before you can index documents into it. In the previous example, Elasticsearch will automatically create the customer index if it didn’t already exist beforehand.
如果没有customer这个index的话,将会创建! 

PUT操作也可以更新index,index可以作为add/update

使用POST方法,后面不需要指定ID:   
```
curl -X POST "localhost:9200/algo/_doc?pretty" -H "Content-Type:application/json" -d @sample.json
```
返回内容:
```
{
  "_index" : "algo",
  "_type" : "_doc",
  "_id" : "D5SKF2QBoiUX6W1G2Q_7",   # 注意这里返回的id是hash值,并不是数字id
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 1,
  "_primary_term" : 1
}
```


删除一个index:
```
DELETE /customer
```

REST API的格式:
```
<REST Verb> /<Index>/<Type>/<ID>
```

#更多的update方式   
```
curl -X POST "localhost:9200/customer/_doc/1/_update?pretty" -H "Content-Type:application/json" -d @sample.json

sample.json内容:   
{
    "doc": {"name":"joe zhang kkk"}
}
```

使用脚本去修改元素值:   
```
curl -X POST "localhost:9200/customer/_doc/1/_update?pretty" -H "Content-Type:application/json" -d @add-age.json
```

add-age.json 内容:   
```
{
  "script" : "ctx._source.age += 5"
}
```

#批量导入数据  
批量数据导入方式:   
```
curl -H "Content-Type:application/json" -X POST "localhost:9200/bank/_doc/_bulk?pretty&refresh" --data-binary "@accounts.json"
```
curl在导入的时候使用 --data-binary 参数,该参数遇到\n的时候不会断开链接并且会保持会话   
accounts.json内容样例:  
```
{"index":{"_id":"1"}}
{"account_number":1,"balance":39225,"firstname":"Amber","lastname":"Duke","age":32,"gender":"M","address":"880 Holmes Lane","employer":"Pyrami","email":"amberduke@pyrami.com","city":"Brogan","state":"IL"}
{"index":{"_id":"6"}}
{"account_number":6,"balance":5686,"firstname":"Hattie","lastname":"Bond","age":36,"gender":"M","address":"671 Bristol Street","employer":"Netagy","email":"hattiebond@netagy.com","city":"Dante","state":"TN"}
```


### json查询数据
```
curl -X POST "localhost:9200/bank/_search?pretty" -H "Content-Type:application/json" --data-binary @query.json
```
query.json
```
{
    "query":{"match_all":{}},
    "from":10,
    "size":2,
    "sort":{"balance":{"order":"desc"}}
}
```

查询多个fields:   
```
{
  "query": { "match_all": {} },
  "_source": ["account_number", "balance"]
}
```

match查询语法:
```
GET /bank/_search
{
  "query": { "match": { "account_number": 20 } }
}

{
  "query": { "match": { "address": "mill lane" } }  #查询mill or lane
}
```

### bool query:
bool query的关键词有:should, must, must not

```
{
    "query":{
        "bool":{
            "must":[
                {"match":{"address":"mill"}},
                {"match":{"address":"lane"}}
            ]
        }
    }
}
```

### score 是返回的匹配程度
In the previous section, we skipped over a little detail called the document score (_score field in the search results). The score is a numeric value that is a relative measure of how well the document matches the search query that we specified. The higher the score, the more relevant the document is, the lower the score, the less relevant the document is

返回的score越高,说明匹配程度越高
```
{
  "took" : 10,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 216,
    "max_score" : 1.0,  
    "hits" : [
      {
        "_index" : "bank",
        "_type" : "_doc",
        "_id" : "253",
        "_score" : 1.0,
        "_source" : {

....
}
}
}
}
```

### filter query   
filter query的内容:
```
{
  "query": {
    "bool": {
      "must": { "match_all": {} },
      "filter": {
        "range": {
          "balance": {
            "gte": 20000,
            "lte": 30000
          }
        }
      }
    }
  }
}
```
 In the above case, the range query makes perfect sense since documents falling into the range all match "equally", i.e., no document is more relevant than another.

### 聚合操作
样例:
```
{
  "size": 0,
  "aggs": {
    "group_by_state": {
      "terms": {
        "field": "state.keyword"
      }
    }
  }
}
```


### es 的REST api 设计
es的rest api设计确实非常的不错,操作动词一般放到最后一个,前面的都是实体,后续跟查询的参数:
```

```


# 性能调优
index索引:
index只是一个逻辑命名空间,指向的是其空间下的shard分片,
分片才是底层的工作单元,一个分片仅保存数据的一部分,是lucence的操作单元

```
一个主分片最大能够存储 Integer.MAX_VALUE - 128 个文档，但是实际最大值还需要参考你的使用场景：包括你使用的硬件， 文档的大小和复杂程度，索引和查询文档的方式以及你期望的响应时长
```

# prerouter的内容
es的prerouter都是在节点内的吗?每个节点都有自己的router管理器?
```
```


