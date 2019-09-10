## 实时数据接收器

v0.01
使用本地下载的数据写入到消息中间件中。

kafaka / rabbitmq 分别实现一次。


### RabbitMQ

```Dockerfile
rabbitmq:
   image: rabbitmq:3-management
   ports:
    - "8081:15672"
```

```python
# pika 库作为RabbitMQ Client
import pika

param = pika.ConnectionParameters(host = ,
                                          connection_attempts = ,
                                          retry_delay = )
connection = pika.BlockingConnetion(param)

channel = connection.channel()
channel.exchage_declare(exchange = ,exchange_type = 'fanout')
                

```