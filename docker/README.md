## 简介
分别实现两个独立提供服务的容器 redis 与 flask , 并通过docker-compose 将两个服务打包在一起共同对外提供网页访问计数器的服务。

### Dockerfile 介绍
Dockerfile 是描述如何打包软件的一系列指令。
```FROM``` 选择基础镜像（image），这使得我们构建服务可以站在巨人的肩膀上而不必从零开始。DockerHub 中包含了许多常用的服务镜像。

```ADD``` 将宿主机的文件一次性地复制到容器中，宿主机之后对文件的修改并不会影响容器中的文件。

```WORKDIR``` 指定容器运行的工作目录

```CMD``` 在容器中执行命令行

### redis 服务
启动redis 为falsk提供可持久化存储的计数服务。

```./redis/Dockerfile``` 功能解释
从Docker Hub 远程仓库拉取 redis 镜像，并将当前文件下的```redis.conf```拷贝到容器中。并切换容器的工作目录为```/data```。

### web 服务
启动flask, 每次被访问时都从redis服务中取出计数值并加一，并作为结果显示在网页中。

### docker-compose.yml 文件
TODO

## 启动集群

```docker-compose up``` 该命令会同时启动 **redis** 与 **web** 容器。打开宿主机浏览器输入```localhost```并回车，可以在浏览器中看到```PV is 1```字样。刷新页面该数据会自增。即便使用```ctrl + c```关闭容器集群后在重新开启集群，我们可以看到计数器仍然延续集群关闭前的数值，而并不会因为Redis是内存数据库而丢失数据。原因是redis 对数据库做了一个本地文件的备份，文件名为 ```dump.rdb```。启动 redis 服务后，redis 会自动读取该文件中的数据。