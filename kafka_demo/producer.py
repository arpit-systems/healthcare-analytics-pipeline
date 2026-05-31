from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

message = b'Patient_ID=101, Disease=Diabetes'

producer.send('healthcare_topic', message)
producer.flush()

print("Message sent successfully!")