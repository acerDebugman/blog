# PyFrameObject
```
typedef struct _frame{
    PyObject_VAR_HEAD //"运行时栈"的大小是不确定的
    struct _frame *f_back; //执行环境链上的前一个frame，很多个PyFrameObject连接起来形成执行环境链表
    PyCodeObject *f_code; //PyCodeObject 对象，这个frame就是这个PyCodeObject对象的上下文环境
    PyObject *f_builtins; //builtin名字空间
    PyObject *f_globals;  //global名字空间
    PyObject *f_locals;   //local名字空间
    PyObject **f_valuestack; //"运行时栈"的栈底位置
    PyObject **f_stacktop;   //"运行时栈"的栈顶位置
    //...
    int f_lasti;  //上一条字节码指令在f_code中的偏移位置
    int f_lineno; //当前字节码对应的源代码行
    //...

    //动态内存，维护(局部变量+cell对象集合+free对象集合+运行时栈)所需要的空间
    PyObject *f_localsplus[1];
} PyFrameObject;
```
PyFrameObject的是python代码块的表示类,函数,{},表示

每一个 PyFrameObject对象都维护了一个 PyCodeObject对象，这表明每一个 PyFrameObject中的动态内存空间对象都和源代码中的一段Code相对应。
# PyCodeObject
typedef struct {
    PyObject_HEAD
    int co_argcount;        /* 位置参数个数 */
    int co_nlocals;         /* 局部变量个数 */
    int co_stacksize;       /* 栈大小 */
    int co_flags;
    PyObject *co_code;      /* 字节码指令序列 */
    PyObject *co_consts;    /* 所有常量集合 */
    PyObject *co_names;     /* 所有符号名称集合 */
    PyObject *co_varnames;  /* 局部变量名称集合 */
    PyObject *co_freevars;  /* 闭包用的变量名集合 */
    PyObject *co_cellvars;  /* 内部嵌套函数引用的变量名集合 */
    /* The rest doesn’t count for hash/cmp */
    PyObject *co_filename;  /* 代码所在文件名 */
    PyObject *co_name;      /* 模块名|函数名|类名 */
    int co_firstlineno;     /* 代码块在文件中的起始行号 */
    PyObject *co_lnotab;    /* 字节码指令和行号的对应关系 */
    void *co_zombieframe;   /* for optimization only (see frameobject.c) */
} PyCodeObject;
```

