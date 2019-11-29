#!/usr/bin/env bash
# 一键启动spark 与 kafka 集群
cd ../cluster/kafka
docker-compose -f docker-compose-single-broker.yml up -d

cd ../spark
docker-compose up -d

# 数据发送模拟程序
cd ..
cd ..
cd ./real-time-stock-trader
cd ./stock_price_receiver/
python data_monitor.py &

# spark 处理程序
cd ../data_buffer/
python model_v1.py
