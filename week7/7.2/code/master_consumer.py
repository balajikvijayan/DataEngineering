import time, json, ast

from kafka.client   import KafkaClient
from kafka.consumer import KafkaConsumer

KAFKA_TOPIC = 'mygram'
n=10
client = KafkaClient("localhost:9092")
consumer = KafkaConsumer(KAFKA_TOPIC,
						 group_id='my_group',
						 bootstrap_servers=['localhost:9092'])
data = []

if __name__ == "__main__":
	for i,message in enumerate(consumer):
		data.append(ast.literal_eval(message.value))
		if i > 0 and i % (n*12) == 0:
			path = "..\\data\\"
			name = "data" + str(i/n) + ".json"
			with open (path+name, 'w') as outfile:
				for vals in data:
					json.dump(vals, outfile)
					outfile.write("\n")
			print name + " written."
			break
		