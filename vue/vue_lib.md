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
