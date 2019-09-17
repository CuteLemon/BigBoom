## 简介
分别实现两个独立提供服务的容器 redis 与 flask , 并通过docker-compose 将两个服务打包在一起共同对外提供网页访问计数器的服务。


## 基础
### docker
docker 容器技术将复杂的环境搭建抽象并且统一为简单的操作。你想学习使用任意的软件都可以简化为三步：
1. APP_NAME + docker 为关键词在Github仓库中搜索

2. 下载该仓库
```bash
git clone APP_DOCKER_URL
```
3. 启动软件
```bash 
docker-compose up
```

如果我需要自定义配置该怎么办？我的回答是：自定义配置往往是与具体的场景与需求联系在一起，换言之，初学阶段用不着自定义配置。只需要专注于开箱即用的统一配置，将精力着重于软件功能与整体的架构设计。

**docker 术语**
- image 描述如何安装软件的图纸
- container 按照图纸打包好的软件

**常见docker 命令**


- ```docker build -t container_name .```
按照当前文件夹下的```Dockerfile``` 打包软件。

- ```docker-compose up```
按照当前文件夹下的```docker-compose.yml``` 文件启动容器集群（多个容器）。

### Dockerfile 介绍
Dockerfile 是描述如何打包软件的一系列指令。
```FROM``` 选择基础镜像（image），这使得我们构建服务可以站在巨人的肩膀上而不必从零开始。DockerHub 中包含了许多常用的服务镜像。

```ADD``` 将宿主机的文件一次性地复制到容器中，宿主机之后对文件的修改并不会影响容器中的文件。

```WORKDIR``` 指定容器运行的工作目录

```RUN``` 执行命令并创建新的镜像层，RUN 经常用于安装软件包。

```CMD``` CMD 设置容器启动后默认执行的命令及其参数，但 CMD 能够被 docker run 后面跟的命令行参数替换。

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

## docker 管理
清理镜像以及容器内部数据。注意风险。[参考链接](https://note.qidong.name/2017/06/26/docker-clean/)