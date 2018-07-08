常见的python基础题:

# builtin 函数
python3.6.5 的 builtins函数共有68个!!
常用的内建函数:
str()
all()
any()
max()
min()

map()

以下5个函数是用来进行python反射使用的:
```
setattr(object, name, val)
getattr(object, name)
delattr(object, name)
hasattr(object, name)
__import__("modules_name", fromlist=True) #fromlist 指定可以使用.符号
```

# is 和 == 区别
为提高效率[-5, 256]会进行缓存,类似java对数字缓存
is是通过id()判断对象id是否唯一,id(object)返回的内存地址
== 值判断对象的value是否相等
python万物皆对象,重要的3个属性: id, type, value   

所以is的效率高于==, 知道了缘由,可以考虑使用is替换==, 但是不推荐,因为可读性第一


# generator 是否支持slice操作?
不支持

#pep8变量命名规范
总结:
变量:
1. 前带_的变量:  标明是一个私有变量, 只用于标明, 外部类还是可以访问到这个变量
2. 前带两个_ ,后带两个_ 的变量:  标明是内置变量,
3. 大写加下划线的变量:  标明是 不会发生改变的全局变量
函数:
1. 前带_的变量: 标明是一个私有函数, 只用于标明,
2. 前带两个_ ,后带两个_ 的函数:  标明是特殊函数

Python 的代码风格由 PEP 8 描述。这个文档描述了 Python 编程风格的方方面面。在遵守这个文档的条件下，不同程序员编写的 Python 代码可以保持最大程度的相似风格。这样就易于阅读，易于在程序员之间交流。

# python 为什么不支持函数重载
函数重载是如果是功能不同,就直接取不同名字;如果功能相同,
1. 参数类型不同
2. 参数个数不同

python语言很灵活,参数类型不同,python直接支持;python函数可以接受任意类型的参数
参数个数不同,python支持可变参数和默认值参数 *args, **kwargs, 因为假定功能相同,缺省的参数肯定是需要的!
如果真要做,也是可以实现的,具体可以去搜索!


#os 和 sys 模块区别
os模块负责与操作系统交互的,提供了访问操作系统底层的接口
sys模块负责程序与python解释器的交互,提供了api和变量,用于控制运行时环境



# * 和 ** 区别
1. 用在函数签名上,相当于*是positional argument, **是key-value形式的参数
函数参数实际上是
2. 用在函数执行传参数的时候,如果执行的函数可以接受**kwargs形式的参数, **可以将传入的dict转为key-value形式的参数形式,比如:
```
def two(**x):
    print(x)

k={"a":1,"b":2} #dict的Key必须是string类型
two(**k) #**将k转为kw字典形式:"a"=1,"b"=2, 但是**将k转为tuple传入: 
```

# 装饰器有哪些类型?有什么用途?对装饰器的理解?
2中类型的装饰器:
第一种函数装饰器,第二种类装饰器   
函数装饰类:
```
def registerattr(*args,**kwargs): #第三层是自己的decorator的参数, eg: @decoreator_eg(1,2,3...)
    def _registerattr(func):     #第二层传入的是实际的函数名做参数,类似求一层导,函数式编程
        def _real_fn(*args1, **kwargs1):   #实际就是实际要执行的函数传入的参数
            print(args,kwargs)
            print(args1,kwargs1)
            print("before")
            rs = func(args1, kwargs1)
            print("after")
            return rs
        return _real_fn
    return _registerattr
```

修饰类的装饰器,主要用于给类添加属性
```
def func_name():
    pass

def register_dict(kclass):
    setattr(kclass, "list_all", lambda self: {x:y for x,y in vars(self).items() if y})
    kclass.todict =  func_name  #这里也可以直接等于函数名,函数式编程
    return kclass   #这里要返回class
```

```
def register(fn):
    def _register(self, **kwargs):
        for x,y in kwargs.items():
            setattr(self, x, y)
    return _register

def list_all_members(self):
        return {x:y for x,y in vars(self).items() if y}

def test_cls(kclass):
    kclass.todict_func = list_all_members
    kclass.todict = lambda self: {x:y for x,y in vars(self).items() if y}
    setattr(kclass, "list_all", lambda self: {x:y for x,y in vars(self).items() if y})
    return kclass

@test_cls
class tt():
    @register
    def __init__(self, **kwargs):
        pass

def main():
    a = tt(a=1, b=2, c=None)
    print(a.todict())
    print(a.list_all())
    pass
```

decorator的顺序问题,是从上往下的:
```
@decorator1   #先执行
@decorator2   #第二个执行
def func():
    pass
```

#python中是否存在类似c中的循环引用的问题?
存在! 两个文件相互引用,是会报错的!

#如何生成hash值
```
import hashlib
m = hashlib.md5()
m.update(raw_msg1.encode("utf-8"))
m.update(raw_msg2.encode("utf-8"))  #只能对二进制数据流进行md5
m.hexdigest()  #16进制hash值
m.digest() #10进制hash值
```

#如何开启多进程,多线程执行
```

```





