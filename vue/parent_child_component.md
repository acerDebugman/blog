#parent and child

<router-view />
如果是通过router-view切换的页面,router-view就是其他组件的父组件!!
```
<router-view v-on:updateBreadcrumbs="recieveChildMsg" />
```


## router-link的使用
router-link使用的时候,里面的name不是path路径,是在router的index.js里的组件的名称:
```
{path: "/goodsCampaign", component: GoodsCampaign, name: "GoodsCampaign", props:true},
```
router-link使用:
```
<template slot-scope="scope">
    <router-link :to="{name:'GoodsCampaign', params:{goods_id:'joe'}}">{{scope.row.goods_name}}</router-link>
</template>
```


reference:
https://www.jianshu.com/p/bff82b3e47a5
http://www.cnblogs.com/penghuwan/p/7473375.html#_label1
