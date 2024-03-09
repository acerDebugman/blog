### scala 经典写法
1. 随机排序
```
import java.util.Random
val random = new Random()
val seq = List(3,4,2,1)
seq.map(t=>(random.nextDouble(),t)).sortBy(_._1).map(_._2)
```
