## scala 集合类
collections 都是慢加载的，只有调用foreach等方法具体去取值的时候，才会触发前面的算子执行！ 
有点类似python的中django的filter等操作！

##flatMap 算子
flatMap算子是flatten 和 map的结合：  
先执行map操作，map()里的内容要是traversable的子类，然后会调用flatten函数 



