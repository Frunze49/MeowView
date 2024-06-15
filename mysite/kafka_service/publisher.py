from kafka import KafkaProducer
import json

def send_to_kafka(post_id: int, user_id: int, action: str):
    json_data = {
        'user_id': user_id,
        'action': action,
        'post_id': post_id,
    }

    producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    producer.send('views', value=json_data)

    producer.close()