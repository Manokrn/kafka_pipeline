# consumer.py
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'click-events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='click-group'
)

print("Listening for click events...")

for message in consumer:
    print(f"👆 Click received: {message.value}")
