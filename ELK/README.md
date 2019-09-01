## ELK

ELK = Elasticsearch + Logstash + Kibana

ELK Stack 是实时日志处理领域开源界第一选择。

### Elasticsearch

响应极其快速的分布式搜索引擎中间件。在ELK架构中充当了一个数据库的角色。

```bash
# 启动一个elasticsearch 容器，默认会映射9200端口
docker run elasticsearch:5.0
```

推荐在Chrome 浏览器中安装插件：ElasticSearch Head. 可以方便的进行交互操作。安装插件后可以自动连接默认配置下的Elastic 服务。


### Logstash

Logstash 是一个开源日志收集处理框架
```bash
# 启动一个logstash 容器
docker run logstash
```

```bash
# 进入container
docker exec -it CONTAINER_ID /bin/bash
```
此步骤也可以使用vs code 中的docker插件实现快捷操作，点击containers 中的具体容器，右键选择*Attach Shell*即可连接该容器的shell。
```bash
bin/logstash -e 'input { stdin { } } output { stdout {} }' --path.data='./data_test/'

# 运行命令后可以在Shell 中输入字符，回车后可以看到如下显示
...
[2019-09-01T09:22:26,411][INFO ][logstash.agent           ] Successfully started Logstash API endpoint {:port=>9601}
hello world
/usr/share/logstash/vendor/bundle/jruby/2.5.0/gems/awesome_print-1.7.0/lib/awesome_print/formatters/base_formatter.rb:31: warning: constant ::Fixnum is deprecated
{
      "@version" => "1",
    "@timestamp" => 2019-09-01T09:22:31.257Z,
          "host" => "66fa5e8dcd97",
       "message" => "hello world"
}
```
**注意：** 必须设置--path.data 参数，以避免和container 本身运行的logstash instance 所使用的./data 文件夹冲突。

### Kibana
Kibana 是一款开源的数据分析和可视化平台。

```bash
# 启动一个kibana容器，默认映射端口5601
docker run kibana
```



--- 
参考资料
1. http://docs.flycloud.me/docs/ELKStack/index.html
2. ELK Stack 权威指南
