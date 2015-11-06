import time, json

from kafka.client   import KafkaClient
from kafka.producer import SimpleProducer
from generator import Generator

KAFKA_TOPIC = 'mygram'

def generation():
    generator = Generator(1)
    return generator.Generate().next()
    
n=10
client = KafkaClient("localhost:9092")
producer = SimpleProducer(client)
for i in xrange(n):
	data = generation()
	print i
	for vals in data:
		producer.send_messages(KAFKA_TOPIC, str(vals))
	i+=1
	if i == n:
		time.sleep(1)
		break