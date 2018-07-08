#延迟执行的库

```
npm i --save lodash
```

使用时候使用require引入
```
var _ = require('lodash');

export default {
methods: {
 clickMe: _.debounce(function() {
		...
	}, 500)
}
}
```

reference:
https://lodash.com/

# vue-cookie使用
```
npm install vue-cookie --save
import VueCookie from 'vue-cookie'
Vue.use(VueCookie)
```

外部js引用
```
import $cookie from 'vue-cookie'
$cookie.set('userName', 'aaa111') // 设置 cookie
console.log($cookie.get('userName')) // 读取 cookie
```
