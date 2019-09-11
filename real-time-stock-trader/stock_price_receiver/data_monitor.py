"""
读取本地数据文件，将数据写入接口
"""
import pandas as pd
import numpy as np
from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092')

data = pd.read_csv('aapl-trading-hour.csv')

if __name__ == "__main__":
    while True:
        for k,v in data.iterrows():
            producer.send('test',key=k,value=v)