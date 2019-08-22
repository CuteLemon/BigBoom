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