from kafka import KafkaConsumer
from time import sleep

def consumer_res():
    consumer = KafkaConsumer('Reservations', bootstrap_servers = 'localhost:9092')
    for msg in consumer:
        print(msg)
        sleep(5)


if __name__ == '__main__':
    consumer_res()


