"""
读取本地数据文件，将数据写入接口
"""
import pandas as pd
import numpy as np
from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                        key_serializer = lambda x: x.encode('utf-8'), 
                        value_serializer=lambda x: x.encode('utf-8'))

data = pd.read_csv('aapl-trading-hour.csv')
data.rename(columns={data.columns[0]:'timestamp'},inplace=True)
# data.set_index('timestamp',inplace=True)

if __name__ == "__main__":
    while True:
        i = 0
        for k,v in data.iterrows():
            producer.send('test',key=str(i),value=v.to_json())
            i+=1
            time.sleep(1)