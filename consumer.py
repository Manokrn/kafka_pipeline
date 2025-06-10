from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='mano-group',
    value_deserializer=lambda m: m.decode('utf-8')
)

print("📥 Listening for messages...")
for msg in consumer:
    print(f"🔔 Received: {msg.value}")
