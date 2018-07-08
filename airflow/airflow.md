# airflow 是否可以汇集?
在某个截断可以join操作!

# 在使用Variable的时候,最好自己设置string作为value
因为使用variable本质上是保存在数据库,如果直接存储对象,airfllow自己会序列化你转为string, 但是如果是对象很可能会导致转换的时候字符串过长无法插入!!

# airflow中使用多个流程
如果产生多个数据流程如:   
```
A --> B --> E --> F --> G --> H
      C --> D --> 
```

如果使用airflow原有的方法是不行的:   
```
A >> B >> E >> F
A >> C >> D >> F
F >> G >> H
```
这样的流程是不行的,最后 F,G,H会执行两次,实际只需要执行一次就行!   
并且isov的数据推到druid, 数据是直接放到hdfs上的,只需要将数据推送到hdfs的目录就行,提交给druid的时候使用hadoop_index的方式提交   

解决这个问题可以使用SubDag的方式!
airflow如果需要真正的多个并行,只要多个task只设置dag就行,不需要设置task之间的上下流关系


# 使用bash参数
```
compute_mz_impression = BashOperator(
        task_id="compute_mz_impression",
        bash_command="echo 'test_1_task:' {{params.joe}}",
        params={"joe": "joe param test"},
        dag=main_dag
    )
```

# 使用airflow的时候,可以kill掉对应的taskid进程
```
```
每个任务都应该是相对独立的,相对独立的就可以直接Kill掉






