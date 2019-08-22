import json
import pandas as pd
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

data = pd.read_json('test_events.json', lines=True)

if __name__ == "__main__":
    while True:
        producer.send('test', data.to_dict())
