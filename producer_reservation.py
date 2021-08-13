from kafka import KafkaProducer
from random import randint, choice, random, uniform
from time import sleep

def random_res():
    reservation = ''
    days = ['Tuesday', 'Wednesday', 'Thursday', 'Friday']
    times = ['11:30', '12:00', '12:30', '1:00', '5:30', '6:00', '6:30', '7:00', '7:30', '8:00', '8:30']

    reservation = choice(days) + ':' + choice(times)
    return bytes(reservation, encoding= 'utf-8')

# producer_reservation.py

def send_res():
    producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
    id = [6, 7, 8, 9, 10]
    while True:
        res_id = bytes(str(choice(id)), encoding = 'utf-8')
        producer.send('Reservations', key = res_id, value = random_res())
        print('reservation made')
        sleep(5)

if __name__ == '__main__':
    send_res()