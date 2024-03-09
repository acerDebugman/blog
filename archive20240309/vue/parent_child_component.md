#parent and child

<router-view />
如果是通过router-view切换的页面,router-view就是其他组件的父组件!!
```
<router-view v-on:updateBreadcrumbs="recieveChildMsg" />
```
子组件通过emit发出事件信息:
```
sendMsg() {
   this.$emit("updateBreadcrumbs", "joezhang")
},
```

#如何调用子组件的方法
在很多时候,都需要去调用子组件的方法,比如第二次切换显示子组件时候,可能需要清楚原先子组件里的数据,这时候需要调用子组件的方法去初始化.比较麻烦的做法是在子组件中监听父组件传过来的变量,根据变量状态判断是否调用初始化方法.
更好的方法是直接调用子组件内部的方法,通过在父组件中的ref=""就可以做到:
```
<CampaignSelectGoods
        ref="CampaignSelectGoods"     //在触发的方法内调用ref的名字,就可以
        v-bind:selectedCampaignItems="multipleSelection"
        @selectGoodsCancel="handleSelectGoodsCancel"
        @selectGoodsSubmit="handleSelectGoodsSubmit"
        @selectGoodsEditRule="handleGoodsEditRule"
        ></CampaignSelectGoods>
```
如果是首次调用,会报错,因为组件还没被初始化,需要先判断是否是空的
```
//show dialog
if (this.$refs.CampaignSelectGoods) {
   console.log("goods: ", this.$refs.CampaignSelectGoods)
   this.$refs.CampaignSelectGoods.initMe()
}
this.outerVisible = true
```
但是这样做的不好是,组件的封装不好!!
比较好的方式是父,子组件同时使用申明使用choosedGoods, 子组件使用watch监视,随时发送this.$emit()更新父组件的值,
父组件使用.sync,
```
<CampaignSelectGoods
        ref="CampaignSelectGoods"
        :selectedCampaignItems="multipleSelection"
        :choosedGoodsProp.sync="choosedGoods"
        @selectGoodsCancel="handleSelectGoodsCancel"
        @selectGoodsSubmit="handleSelectGoodsSubmit"
        @selectGoodsEditRule="handleGoodsEditRule"
        ></CampaignSelectGoods>
```
使用sync等价于:
```
<CampaignSelectGoods
        ref="CampaignSelectGoods"
        :selectedCampaignItems="multipleSelection"
        :choosedGoodsProp="choosedGoods"
	@update:choosedGoodsProp="val => choosedGoods = val"
        @selectGoodsCancel="handleSelectGoodsCancel"
        @selectGoodsSubmit="handleSelectGoodsSubmit"
        @selectGoodsEditRule="handleGoodsEditRule"
        ></CampaignSelectGoods>

```
子组件:
```
choosedGoods: function(val) {
   this.$emit("update:choosedGoodsProp", val) //update:choosedGoodsProp是个父组件里的方法名, .sync修饰符缩短了使用
}
```

总结起来:   
父子组件传数据必须是父组件通过属性传递值,子组件通过事件返回值,但是子组件内部可以通过computed或者watch方法去解耦,实现父子双向通信
```
props: ["selectedCampaignItems", "choosedGoodsProp"],
computed: {
      choosedGoods:{
        get: function() {
          return this.choosedGoodsProp
        },
        set: function(val) {       //这里要设置set方法,这样自组件里修改值的时候,才会调用
          this.$emit("update:choosedGoodsProp", val)
//          this.choosedGoodsProp = val  //这样写是不允许的,会报错, 报错信息参考如下
          return val
        }
      }
}
```

报错信息:
vue.esm.js?efeb:591 [Vue warn]: Avoid mutating a prop directly since the value will be overwritten whenever the parent component re-renders. Instead, use a data or computed property based on the prop's value.  Prop being mutated: "choosedGoodsProp"


使用watch方法同样可以实现同样的双向通信方式,同时监听父组件的传到子组件的prop信息:
```
data() {
   return {
	choosedGoods: ""
   }
},
watch: {
      choosedGoods: function(val) {
        this.$emit("update:choosedGoodsProp", val)
      },
      choosedGoodsProp: function(val) {
        console.log("insumb goodsProp")
        this.choosedGoods = val  //父组件修改则复制给子组件的属性!
      }
},
```

三种方法比较而言,推荐使用第三种方法,通过compute的方式实现!


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
