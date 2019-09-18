# BigBoom
[![CircleCI](https://circleci.com/gh/CuteLemon/BigBoom/tree/master.svg?style=svg)](https://circleci.com/gh/CuteLemon/BigBoom/tree/master)
## 背景
我在学习大数据技术栈时遇到了很多问题，这些问题花费我大量的时间与头发。但我认为这并不是学习技术所必须经历的苦痛，因为其中大部分都是些配置与细节问题。本仓库的目标是为了后来者可以优化学习曲线，可以快速地对工具有一个整体的印象。如果对你的学习有帮助，求个Star !


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

## python 
TODO:
python version
python package version >> requirements.txt
