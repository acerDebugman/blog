# scala 要点  
### 类型
In Scala, all values have a type, including numerical values and functions. 
Any类型, 是所有类型的开始，内部有toString, hashCode, equals等方法
AnyVal 类型，是所有基础数据类型的父类型
AnyRef 类型，是所有的对象类型的父类型

Any is the supertype of all types, also called the top type. 
It defines certain universal methods such as equals, hashCode,
 and toString. Any has two direct subclasses: AnyVal and AnyRef.  

AnyVal represents value types.
 There are nine predefined value types and they are non-nullable: Double, Float, 
 Long, Int, Short, Byte, Char, Unit, and Boolean. 
 Unit is a value type which carries no meaningful information.
  There is exactly one instance of Unit which can be declared literally like so: ().
   All functions must return something so sometimes Unit is a useful return type.  

AnyRef represents reference types. 
All non-value types are defined as reference types. 
Every user-defined type in Scala is a subtype of AnyRef. 
If Scala is used in the context of a Java runtime environment,
 AnyRef corresponds to java.lang.Object.  
 

Unit 类型类似 void 类型
def move(dx:Int, dy:Int) : Unit = 

Nothing and Null:
Nothing is a subtype of all types, also called the bottom type. 

### function and methods   
#### 函数function  
函数表达式是 => 符号！！   
左边是参数tuple, 右边是函数表达式   
和方法是不同的类型   

(x :Int) => x + 1  
=> 匿名函数的符号  

无参匿名函数：  
var getAnster = () => 42  

函数作为参数传入当方法中,函数签名如果只有一个就可以只写一个，如果有多个就写为,Unit作为返回值:
(T1, T2) => Unit  
例子：  
```
def foreach(f: T => Unit): Unit = while(hasNext) f(next())
```

#### method   
def methodName(x: type) : Unit = {  
}  

def关键字，   
methodName  方法名  
参数列表，  
返回值  
=  赋值表达式,表示语句块可以给  
expression body {} 

其中参数列表可以省略  

####  嵌套方法
在方法里可以可以定义方法,但是作用域就限定于一个方法里了，如阶乘：  
```
def factorial(x:Int): Int = {
    def fact(x:Int, accumulator: Int): Int = {
        if (x <= 1) accumulator
        else
            fact(x - 1, accumulator * x)
    }
    fact(x, 1)
}
```


#### high order functions
Higher order functions take other functions as parameters or return a function as a result. 
This is possible because functions are first-class values in Scala.
使用函数作为参数和返回值的函数  

coercing methods into functions   
1. 方法也可以作为参数传入函数中G，originalMethod会被转为 (x1, x2) => originalMethod(x1, x2) 匿名函数
2. method or function 接受function函数作为参数
3. functions that return functions
函数返回函数类型:   
```
def urlBuilder(ssl: Boolean, domainName: String): (String, String) => String = {
    val schema = if (ssl) "https://" else "http://"
    (endpoint: String, query: String) => s"${schema}${domainName}/${endpoint}?${query}"
}
```


4. 



### 类  
创建类实例使用new 关键字
var tlist = Nil
val user = new User()

1. Members are public by default.
成员默认都是public的   

Primary constructor parameters with val and var are public.  
Parameters without val or var are private values, visible only within the class.  

###  case class  
case class 的区别就是，  
 1. 申明的时候可以不需要new 关键字  
 val point = Point()  
 
 2. 可以比较, 默认实现了compare
 3. copy是浅拷贝  
 
 
case class解释：
 Case classes are good for modeling immutable data
 

### traits 特征   
Traits are types containing certain fields and methods. Multiple traits can be combined.  


```
class RichStringIterator extends StringIterator("joe zhang") with RichIterator
```


### object  
相当于是静态方法类工厂，内部的方法都是静态方法  
所以Main方法只能在 object 里！  


### scala 语法糖
只有一个


### 柯里化
currying
什么是柯里化   
将参数变成列表的方式


### pattern matching
正常的pattern matching，用在数值上  
```
val x: Int = Random.nextInt(10)
x match {
    case 0 => println("zero")
    case 1 => println("one")
    case 2 => println("three")
    case _ => println("many")
}
```
case 0 => println("zero") 可以理解为0是匿名函数 =>  的参数，满足match要求就执行 => 后边的表达式语句  
##### pattern matching on case class
scala 的pattern matching是可以作用与case class上的    
```
abstract class Notification
case class SMS(caller: String, content: String) extends Notification
case class Email(sender: String, title: String, body:String) extends Notification
case class VoiceRecord(contactNumber: String) extends Notification

def showNotification(msg: Notification):String = {
    msg match {
        case SMS(caller, content) =>
            s"SMS: ${caller} , content is ${content}"
        case Email(sender, title, _) =>
            s"Email: sender: ${sender}, title: ${title}"
        case VoiceRecord(contactNumber) =>
            s"voiceRecord contact Number is ${contactNumber}"
    }
}
```

##### pattern guard:  
if \<boolean expression>   
```
notification match {
    case SMS(caller, _) if VipInfo.contains(caller) =>
        println(s"get VIP sms msg: ${showNotification(notification)}")
```

##### match on type only 类型匹配  
```
def goIdle(device: Device): String = {
    device match {
        case p : Phone => p.screenOff
        case c : Compute => c.screenOff
    }
}
```

##### sealed class
Traits and classes can be marked sealed which means 
all subtypes must be declared in the same file. This assures that all subtypes are known

所有的子类都必须在一个文件里申请  


### companion object  
1. An object with the same name as a class is called a companion object.
object是个静态工厂类，
```
object Email {
    def fromString(emailString:String): Option[Email] = emailString.split("@") match {
        case Array(a, b) => Some(new Email(a, b))
        case _ => None
    }
}
case class Email(userName: String, domainName:String)
```

### extractor objects 对象提取器
1. An extractor object is an object with an unapply method. 
这样的unapply方法主要用于match的时候，case CustomerID(name)，将一个对象拆解为name这个参数   
由于unapply的存在，使得scala的pattern matching 变得更加的强大！！

2. case class自动实现了unapply


3. object 对象实现了apply方法，就相当于


### convariant ,contravariant 和 invariant
invariant 不变性  
contravariant 逆变性  
convariant 协变  

G[+A]类似一个生产者，提供数据。（大部分情况下称G为容器类型）  
G[-A] 是一个消费者，主要用来消费数据。  
(如上的 Equiv[-A] （其实就是个A => Boolean的函数，即Function1[-A, Boolean]))   
注意这里的生产者，消费者指的是类！  
比如一下的例子：  
```
sealed abstract class Printer[-A] {
    def print(value: A): Unit
}
//animal consumer
class AnimalPrinter extends Printer[Animal] {
    override def print(animal: Animal): Unit =
        println(s"animal print ${animal.name}")
}

//cat consumer
class CatPrinter extends Printer[Cat] {
    override def print(cat: Cat): Unit =
        println(s"cat print ${cat.name}")
}
```
使用的时候：   


### upper bounds 和 lower bounds
An upper type bound T <: A declares that type variable T refers to a subtype of type A
T <: A 指T是A的子类, A 是上界
可以写为：
<T extends A>

The term B >: A expresses that the type parameter B or the abstract type B 
refer to a supertype of type A.
B >: A 指B是A的父类, A是下界
可以写为：
<B super A>


函数都是逆变的contravariant, 因为：
However, this program does not compile because the parameter elem in prepend is of type B,
which we declared covariant. This doesn’t work because functions are contravariant 
in their parameter types and covariant in their result types.
 
函数为什么一定是逆变的呢？
因为函数能够处理父类，肯定是可以处理子类的, 所以函数参数是协变！
但是生产者容器或者方法返回值，肯定是返回具体的类，或者子类，是协变的！


里氏替换原则通俗的来讲就是：子类可以扩展父类的功能，但不能改变父类原有的功能,
先理解里氏替换原则，子类可以实现父类的抽象方法，但是不能够覆盖非抽象方法
如果非要重写父类的方法，比较通用的做法是：
原来的父类和子类都继承一个更通俗的基类，原有的继承关系去掉，采用依赖、聚合，组合等关系代替。


scala参数逆变：正是因为需要符合里氏替换法则，方法中的参数类型声明时必须符合逆变（或不变），
以让子类方法可以接收更大的范围的参数(处理能力增强)；而不能声明为协变，
子类方法可接收的范围是父类中参数类型的子集(处理能力减弱)。
返回值协变：如果结果类型是逆变的，那子类方法的处理能力是减弱的，不符合里氏替换  


类可以是协变的，但是里面的方法应该是逆变的,这样的话方法可以处理的返回就会更广！
容器类是协变的，这样该容器类可以接受更多的类型！！  
```
trait Node[+B] {
    def prepend(elem: B): Node[B]
}
```
应该改为：
```
trait Node[+B] {
    def prepend[T>:B](elem: T): Node[B]
}
```

协变和逆变的配合应用：
```
trait Node[+B] {
    def prepend[U>:B](elem: U): Node[U]
}

case class ListNode[+B](h: B, t: Node[B]) extends Node[B] {
    def prepend[U >: B](elem: U): ListNode[U] = ListNode(elem, this)
    def head: B = h
    def tail: Node[B] = t
}

case class Nil[+B]() extends Node[B] {
    def prepend[U >: B](elem: U): ListNode[U] = ListNode(elem, this)
}

trait Bird
case class AsianSwallow() extends Bird
case class AfricanSwallow() extends Bird

val asianSwallowList = ListNode[AsianSwallow](AsianSwallow(), Nil())
val birdList: Node[Bird] = asianSwallowList
birdList.prepend(new AfricanSwallow)

asianSwallowList.prepend(new AfricanSwallow)
```
注意这里的prepend方法是逆变的:
```
def prepend[U >: B](elem: U): ListNode[U] = ListNode(elem, this)
```
这里相当于prepend接受的是B的父类！相当于扩大了prepend方法的处理范围！ 
所以prepend方法的参数可以是所有的B的父类！！    
这就是为什么scala的List这么强大，可以接受任何的参数append进去！  
因为使用了逆变(contravariant)，所有的数值类型的父类都是Any！！    

弄懂了scala的协变和逆变才是scala的入门！！


里氏替换原则：   
定义1：如果对每一个类型为 T1的对象 o1，都有类型为 T2 的对象o2，
使得以 T1定义的所有程序 P 在所有的对象 o1 都代换成 o2 时，程序 P 的行为没有发生变化，
那么类型 T2 是类型 T1 的子类型。

定义2：所有引用基类的地方必须能透明地使用其子类的对象。

问题由来：有一功能P1，由类A完成。现需要将功能P1进行扩展，扩展后的功能为P，其中P由原有功能P1与新功能P2组成。
新功能P由类A的子类B来完成，则子类B在完成新功能P2的同时，有可能会导致原有功能P1发生故障。

解决方案：当使用继承时，遵循里氏替换原则。类B继承类A时，除添加新的方法完成新增功能P2外，尽量不要重写父类A的方法，
也尽量不要重载父类A的方法。

### implicit 参数列表
1.类型转换，自动寻找类型相同的implicit, 如果有两种相同的implicit类型，编译会报错.
这种类型是Scala编译器对隐式转换的第一选择。 
比如说编译器看到一个类型的X的数据，但是需要一个类型为Y的数据，那么就会去找把X类型转换成Y类型的隐式转换的态射函数。
eg:
```
Error:(36, 16) ambiguous implicit values:
 both value intMonoid in object Main of type => tutorial.testImplicit.Main.Monoid[Int]
 and value intMonoid2 in object Main of type => tutorial.testImplicit.Main.Monoid[Int]
 match expected type tutorial.testImplicit.Main.Monoid[Int]
    println(sum(List(1,2,3,4)))
```
2.scope区域，只能在同一个scope里生效。注意的是： class可以去伴生对象里去寻找implicit内容
3.函数参数中的变量名也可以被定义为: implicit, 但必须主动指明   

https://fangjian0423.github.io/2015/12/20/scala-implicit/

方法隐式转换：
```
class RichFile(val file:File) {
    def read = Source.fromFile(file.getPath()).mkString
}

object Context {
    implicit def file2RichFile(f:File):RichFile = new RichFile(f)
}

import Context._
println(new File("/home/algo/joe.sh").read) //先将new File()对象调用file2RichFile转为RichFile对象，然后
```

隐式转换确实非常的有用！
implicit conversions 发生的条件
```
Implicit conversions are applied in two situations:
1. If an expression e is of type S, and S does not conform to the expression’s expected type T.
2. In a selection e.m with e of type S, if the selector m does not denote a member of S.
```

在scala.preDef 内部，定义了许多的implicit方法，类似int2Integer(x:Int) , autoBoxing和autonboxing

### 函数式编程 in scala  
函数式编程，注重数据结构的变化    
宁可有一种数据结构，100种态射，也不要有10种数据结构，10种态射!  
有太多的数据结构造成的后果就是太多的实体交互!!增加了复杂度!!!  



### 副作用 side effect
副作用就是对世界产生影响的操作，比如打日志等；  
纯函数就是每次传入的参数都是一致的，得到的结果也是一致的！   
所以纯函数的必须有返回值，但是有副作用的函数就必须是Unit的返回值   
纯函数是只有一个返回值：  



### 尾递归
通过尾递归，使 scala 更类似 数学表达式！！
因为可以通过递归来写表达式，编译器可以自动将尾递归转换为非递归模式执行！！
更关键的是，scala可以根据函数的返回值，当做类型推导，这样就可以递归写，也可以使用返回值类型的操作方法，可以自己体会一个：
```
def listOfDuplicates[A](x: A, length: Int) : List[A] = {
    if (length < 1) Nil
    else 
        x :: listOfDuplicates(x, length - 1)
}
```

listOfDuplicates() 返回值是list, 所以递归的时候，调用时候可以直接当做list来调用！
但是效率不高，可能会遇到stackOverflow的情况，所以
转为尾递归：
```
def listOfDuplicates[A](x: A, length: Int) : List[A] = {
    @tailrec
    def listOfDuplicateRec(x: A, length: Int, lastResult: List[A]): List[A] = {
        if (length < 1) lastResult
        else {
            val rs = x :: lastResult
            listOfDuplicateRec(x, length - 1, rs)
        }
    }

    listOfDuplicateRec(x, length, Nil)
}
```

scala常用的做法就是函数内部定义函数，修改传入参数，将本次内部函数的结果当做参数传入计算，来进行尾递归.
先想递归，然后改写为尾递归！  
改为迭代的方式开发成本大，还是不这么做了！   

Scala里尾递归的使用局限很大，因为JVM指令集使实现更加先进的尾递归形式变得很困难。Scala仅优化了直接递归调用使其返回同一个函数。
比如：
```
val funValue = nestedFun _
def nestedFun(x: Int) {
    if (x != 0) { println(x); funValue(x - 1) }
}
nestedFun(30000)
```
改为以下就可以：
```
val funValue = nestedFun _
def nestedFun(x: Int) {
    if (x != 0) { println(x); nestedFun(x - 1) }
}
nestedFun(30000)
```

python同样不支持尾递归，但是可以优化，关于python的尾递归可以参考：
https://www.jianshu.com/p/d36746ad845d
https://www.zhihu.com/question/29717057

### 类型推断
类型推断可以使用：
val obj = null
null类型只有一个null，所以不能在赋值其他的类型。
类型推断只能在定义的时候使用：
```
var a = 10
a = "a"   //会报错！ "a"是字符串，不能赋值给了整数类型
```


### operators
prefix： 前缀    
infix: 中缀   
suffix: 后缀   


### by-name parameters和 by-value parameters
By-name parameters are only evaluated when used. 
They are in contrast to by-value parameters. 
To make a parameter called by-name, simply prepend => to its type.

by-name parameter 如果在函数体中不调用，那就不会被触发执行！并且可以被调用多次！每次调用都是重新执行一次   
非常方便就可以实现AOP切片思想!
一般默认是by-value parameter的调用方式，只会被调用一次！ by-name的调用方式非常有用！
```
@tailrec
def whileloop(condition: => Boolean)(body: => Unit):Unit = {
    if (condition) {
        body
        whileloop(condition)(body)
    }
}

var i = 2
whileloop(i < 10) {
    println(i)
    i+=1
}
```


### Monad
Monad 是一种设计模式，表示将一个运算过程，通过函数拆解为函数相互链接的多个步骤。
只需要提供下一步运算的所需要的函数，整个过程就可以持续下去.

##### Moniod
moniod是一种元素的集合，它需要满足 结合律 和 幺元(identify： 单位元，这种元和其他元素结合的时候，
不会改变其他的元素)
比如：
```
整数类型int： 0是identify单位元,其中的任何数都满足结合律: (a+b)+c=a+(b+c)    
列表类型List: 任何两个列表可以通过：：：连结起来，其中Nil或空列表[]是identity
字符串类型String: ""是identify类型
```
条件和定律：
```
1. 一个抽象类型A
2. 一个二元结合性函数（binary associative function），对传入的两个A类参数进行操作后产生一个A类型结果。
op操作必须是结合性的，即op(x, y) == op(y, x)；op(a,op(b,c)) = op(op(a,b),c)：
这个定律是函数组合（function composition）不可缺的条件
3. 一个恒等值（identity）。二元函数参数中如果有一个是恒等值时操作结果为另一个参数，
即满足op(identity, x) == x
```


### 范畴论

##### 序
有这样一个范畴，它所包含的态射描述的是两个对象之间的关系——小于或等于.

伴随这种关系的集合被称为前序集，因此一个前序集实际上是一个范畴.

也可以有一个更强的关系，它满足一个附加条件，即，如果 a≤b，b≤a，那么 a 肯定等于 b。伴随这种关系的集合，叫偏序集。
最后，如果一个集合中的任意两个元素之间存在偏序关系，那么这种集合就叫做全序集。
前序集所构成的范畴，从任意对象 a 到任意对象 b 的态射最多只有一个。这样的范畴叫瘦范畴。



在一个范畴 C 中，从对象 a 到对象 b 的态射集被称为 hom-集，记为 C(a,b)，有时也这样写 HomC(a,b)

态射规则：
```
1. 对于箭头f:a -> b和箭头g:b -> c，如果有一个箭头h: a -> c，那么就称为它们的组合，写法是：h=g·f
2. 对于每个元素对象，都有一个单元箭头：id:a -> a。对于任何f: a -> b，满足f·id = f；对于任何g: c -> a，
满足id·g = g,  组合符合结合律：f·(g·h) = (f·g)·h 
3. 态射箭头有两种，一种是标号1的组合箭头，还有一种是标号2的单元箭头。
```

幺半群定义：
```
对于某非空集合S，若存在S上的二元运算”*”使得对于任意的a,b∈S,有a*b∈S（运算封闭），则称{S,*}为广群。
广群只是定义一个集合，集合中有元素和操作，操作结果也属于这个集合，这样泛泛的集合称为广群。　
如果广群再加上结合律约束，就会得到半群，因此半群是广群的子集，要求更苛刻些，
而半群如果再加上幺元（identity element）就是幺半群，也就是结合律+幺元=幺半群，
所以，Monid对应的中文是幺半群。
```


reference:
http://www.ruanyifeng.com/blog/2015/07/monad.html

https://segmentfault.com/a/1190000003883257
https://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/



reference:
http://blog.csdn.net/zhengzhb/article/details/7281833
http://deltamaster.is-programmer.com/posts/48772.html

