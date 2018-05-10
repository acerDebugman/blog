# elemeui 修改全局的css只对当前页面生效
eleme自带全局样式要么在app里修改影响全局,要么就是通过 /deep/ 关键字放在单独的页面里,只影响当前页面,注意加scoped
```
<style scoped>
  /deep/ .el-table th, /deep/ .el-table td {
    padding: 0px 0;
  }
</style>
```



