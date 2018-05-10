#git 使用问题列表
### 1. 在修改了一个文件以后,如何切换到其他的分之?  
修改了以后,如果切换到其他的分之,会导致的问题是,提交不了? 如何可以先隐藏或者缓存已经修改的内容,等到切回来以后再唤醒提交?
可以使用git stash命令:
```
git stash
git stash pop
git stash list //列出多个stash内容
git stash pop stash@{id}  //stash@{id} 比如 stash@{0}, stash@{1}等,用list的时候可以列出来
git stash apply stash@{id}  //apply与pop区别就是不会删除list的内容
git stash drop stash@{id} //删除对应的stash@{id}记录
```


### 2. 如何回撤本地已经提交的commit,但是提交的内容不丢失,还可以重新提交?
head的指向是.git/refs/heads/master或者其他的分支,但是head指向的文件的内容是最新的commit的hash id,使用reset就是修改最新的hash id为历史的某一个版本.之后的历史版本信息就没有了.
git reset的三种方式
--hard
--mixed
--soft  //建议最好用--soft,这样修改的内容不会丢失
```
algo@algo-PC:~/IdeaProjects/isov/isov_admin_front$ cat ../.git/refs/heads/master 
fe05999c0625de3c6473cdba3b0892eec8e1b906
algo@algo-PC:~/IdeaProjects/isov/isov_admin_front$ cat ../.git/refs/heads/dev-2.0-joe 
5570d19f8037dc1f70ad62503a0c2f210457a6b7
```

但是push的时候需要强制push:
```
git push --force
```

git reset的使用:
```
git reflog    //会列出HEAD@{id}的list,使用reset去设置位置!
git reset --hard HEAD@{4}
git reset --soft HEAD@{4} //会保留回退的修改
```
再查看head指向,就发现commit的hash id已经修改了
```
algo@algo-PC:~/IdeaProjects/isov/isov_admin_front$ cat ../.git/refs/heads/dev-2.0-joe 
0716b09e8b713a5c133dc9e8e20f535bec5f576b
```




