# component的使用
全局注册:
```
<div id="example">
  <my-component></my-component>
</div>
// 注册
Vue.component('my-component', {
  template: '<div>A custom component!</div>'
})

// 创建根实例
new Vue({
  el: '#example'
})
```

# 局部注册
使用 component 关键字对应组件名称就行  
```
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
```
或者:
```
  import ElCol from "element-ui/packages/col/src/col";
  import joeTest from './JoeTest.vue'

  export default {
    components: {
      ElCol,
      joeTest
    },
    name: "CampaignNotMatch"
  }
```

也可以研究类似使用js写组件,


## 局部组件的通信
[media通信](./media/props-events.png)
父组件:
```
<template>
  <el-row>
    CampaignNotMatch
    <joeTest msg="hello msg"></joeTest>  <!-- props传属性要这么传才行! -->
    <el-col></el-col>
  </el-row>
</template>
<script>
  import ElCol from "element-ui/packages/col/src/col";
  import joeTest from './JoeTest'

  export default {
    components: {
      ElCol,
      joeTest
    },
    name: "CampaignNotMatch"
  }
</script>
<style>
</style>
```

子组件:
```
<template>
  <el-row>
    <div>joe test : {{ msg }}</div>
  </el-row>
</template>
<script>

  export default {
    name: "joeTest",
    props: ["msg"]
  }
</script>
<style>

</style>
```

# 字面量语法 vs 动态语法
字面量语法:
```
<!-- 传递了一个字符串 "1" -->
<comp some-prop="1"></comp>
```
动态语法:
```
<!-- 传递真正的数值 -->
<comp v-bind:some-prop="1"></comp>
```


## this 使用的区别 ?!
以下两个用不用this是有区别的
```
<CampaignSelectGoods v-bind:selectedCampaignItems="multipleSelection" ></CampaignSelectGoods>
```
和
```
<CampaignSelectGoods v-bind:selectedCampaignItems="this.multipleSelection" ></CampaignSelectGoods>
```
正确的应该是使用第一个




