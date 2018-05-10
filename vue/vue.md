## vue 的seo优化

### seo优化
title 标签也可以添加可以搜索的东西  


### vue的使用
主要是使用<meta> 标签   
简单使用:
<meta name="" content="" />
eg:
<meta name="keywords" content="" />
<meta name="" content="" />

keywords的content内容要限制在36个字。
description的content内容要限制在76个字。

eg:
<meta name="robot" content="all">
<meta name="keywords" content="南非新星国际,新星国际,南非,旅游,签证,南非机票服务,南非机票,南非会计">
<meta name="description" content="南非新星国际,南非注册结婚以及南非外交部公证认证,南非永久居留PR申请，ID 申请,学生,陪伴,退休,商务考察等签证延期,进出关南非有逾期,滞留问题解决">


reference:
https://zhuanlan.zhihu.com/p/29148760


### vue computed 和 watch 的函数
computed 和 watch 是一个解耦的作用,可以将展现的数据和显示的内容结构,尤其是computed属性.  
尤其是v-bind:class和v-bind:style显示样式非常有用.

### todos list的内容
用来做组件的

https://cn.vuejs.org/v2/guide/list.html

### 插槽 



### 写页面的一点心得
1. 不要耦合页面的数据,每个页面,页面绑定的数据就是页面绑定的数据,不要和请求或者跳转的数据耦合,需要的话直接从页面的绑定变量里取数据就行!
例如: 页面多选的checkedbox的变量组不要当做props传入子组件,最好在点击时间发生的时候函数中再去取!

2. 

###computed 属性的使用
computed 属性通过监测函数上下文涉及变量的变动来触发compute函数的,值生效是通过set函数来实现,再该函数内赋值并不会影响数据的使用
```
      handleEdit(idx, row) {
        console.log("before asign: ", this.choosedGoods)  
        this.choosedGoods = row.goods_id
        console.log("after asign: ", this.choosedGoods)   //和before打印出的结果是一致的, 因为赋值是通过比较判断该函数的变化

        this.$emit("selectGoodsEditRule", {
          goodsId: row.goods_id,
//          goodsId: this.choosedGoods,
          goodsName: row.goods_name
        })
      },

     choosedGoods:{
        get: function() {
          return this.choosedGoodsProp
        },
        set: function(val) {
          this.$emit("update:choosedGoodsProp", val)
          console.log("in computed val: ", val)
        }
      }

```
使用nextTrick就可以做到:
```
        let _vm = this
        this.$nextTick(function() {
          console.log("in nexTrick:", _vm.choosedGoods)
        })
        console.log("after asign2: ", this.choosedGoods, row.goods_id)
```
只有computed缓存的属性有这样的性质;是data()返回的属性的话是没有这样的性质的!



###setTimeOut函数使用



### vue里的getter和setter是如何实现的?
使用类似python的decorator吗? 估计是的,或者说是类似的方法!



