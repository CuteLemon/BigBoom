from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.subscribe(['test'])

if __name__ == "__main__":
    for x in consumer:
        print(x)
