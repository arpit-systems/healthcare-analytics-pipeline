from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'healthcare_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

print("Waiting for messages...")

for message in consumer:
    print("Received:", message.value.decode())