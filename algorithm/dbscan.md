# 概念

### 核心对象


### 密度直达


### 密度可达


#如何确定 Eps 半径
### k距离 和 MinPts确定
1. DBSCAN聚类使用到一个k-距离的概念，k-距离是指：给定数据集P={p(i); i=0,1,…n}，对于任意点P(i)，
计算点P(i)到集合D的子集S={p(1), p(2), …, p(i-1), p(i+1), …, p(n)}中所有点之间的距离，
距离按照从小到大的顺序排序，假设排序后的距离集合为D={d(1), d(2), …, d(k-1), d(k), d(k+1), …,d(n)}，
则d(k)就被称为k-距离。也就是说，k-距离是点p(i)到所有点（除了p(i)点）之间距离第k近的距离。
对待聚类集合中每个点p(i)都计算k-距离，最后得到所有点的k-距离集合E={e(1), e(2), …, e(n)}。

2. 根据经验计算半径Eps：根据得到的所有点的k-距离集合E，对集合E进行升序排序后得到k-距离集合E’，
需要拟合一条排序后的E’集合中k-距离的变化曲线图，然后绘出曲线，通过观察，
将急剧发生变化的位置所对应的k-距离的值，确定为半径Eps的值。

3. MinPts 最少点确定，确定k的值就是确定了 MinPts, MinPts = k






reference:
https://www.jianshu.com/p/e8dd62bec026



