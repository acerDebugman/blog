### scala 国内源配置
创建.sbt/repositories
```
[repositories]
local
aliyun: http://maven.aliyun.com/nexus/content/groups/public/
central: http://repo1.maven.org/maven2/
typesafe: http://repo.typesafe.com/typesafe/ivy-releases/, [organization]/[module]/(scala_[scalaVersion]/)(sbt_[sbtVersion]/)[revision]/[type]s/[artifact](-[classifier]).[ext], bootOnly
sonatype-oss-releases
maven-central
sonatype-oss-snapshots
```

### 如何查看spark使用的scala版本
spark-shell 执行后，图标下的第一行内容就是scala的输出


### sbt
执行sbt后，可以执行console命令，进入scala模式



