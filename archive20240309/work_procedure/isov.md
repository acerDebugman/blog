## isov 二次开发的流程
elt ---> 获取dataplus mz数据 ---> 计算权重  | ---> 计算mz曝光         ---> 曝光流程
    ---> admaster爬虫                       | ---> 计算admaster曝光   ---> 曝光流程
    ---> gs数据                             | ---> 计算gs曝光         ---> 曝光流程
    ---> 剧目流程：

剧目流程：
    mz:获取活动id,spotid ---> 剧目爬虫内容 ---> 得到caid和剧目content信息
    ---> 将caid换为brand, media信息(caid和brand,media的信息来源是抽取etl以后的结果)
    ---> 出统计的报表
    ad:直接将admaster爬虫后的数据给康乐 ---> 剧目爬虫内容
    ---> 得到caid和剧目content信息
    ---> 将caid换为brand, media信息(caid和brand,media的信息来源是抽取etl以后的结果)
    ---> 出统计的报表

曝光流程：
   所有的曝光合起来,出总的统计报表数据,

etl注意的点:
0. 媒体同意使用mm的媒体作为标准媒体
1. 新思的日志数据中的媒体替换为mm的媒体的统一的媒体
2. 新思日志中的城市名称不用替换,是一致的,新思的数据要再多处理下
3. 如果是从admonitor出的数据,就要提取a,b字段的信息
4. 当使用admonitor的曝光数据的对应的关系表的,要有website对应的mm媒体的关系表
5.

新思的文件关系表:
1.