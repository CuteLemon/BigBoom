## 实时股票交易系统

实时数据接收器 -> 交易所数据缓存 -> 数据处理引擎 -> 数据缓存 -> 离线数据存储 / 交易策略实时计算 -> 交易执行模块 -> 实时监控看板

实时数据接收器
    - 使用离线历史数据产生 python pandas
    - 调取实时数据接口

交易所数据缓存
kafaka/rabbitmq

数据处理引擎
spark streaming 
flink
python sklearn
tensorflow

指令数据缓存
redis

离线存储
csv - 交易预测数据，交易指令数据
postgresql
mongodb

交易执行模块
富途牛牛模拟仓API

实时监控模块
ELK 数据看板 - 持仓数据，指令数据，指令结果，价格预测

