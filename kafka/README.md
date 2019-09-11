## 准备

```bash
git clone https://github.com/wurstmeister/kafka-docker
```

修改文件 ```docker-compose-single-broker.yml```
```KAFKA_ADVERTISED_HOST_NAME: localhost```

启动 docker-container
```bash
cd kafka-docker
docker-compose -f docker-compose-single-broker.yml up
```


安装 kafka python client
```bash
pip install kafka-python
```

## 测试 
Terminal 1

```bash
python kafka_producer.py
```

Terminal 2
```bash
python kafka_consumer.py
```

在 Terminal 2 中可以看到producer 产生的各类数据。

## troubleshoot

问题描述
```docker-compose up``` 
卡在
(12/21) Installing containerd (1.2.7-r0) 
这一步很久没有进度。
[issue](https://github.com/wurstmeister/kafka-docker/issues/529)

解决方案
使用wurstmeister/kafka 替代 dockerfile。
docker-compose.yml LINE 8
``` build: . ``` 
修改为
``` image: wurstmeister/kafka```