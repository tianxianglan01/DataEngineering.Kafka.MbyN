from random import randint, choice, random, uniform
from kafka import KafkaProducer
from time  import sleep



def entree_order_generator():
    order = ''
    entrees = ['Chicken Fries', 'Mozzarella Sticks', 'Cheeto Dust', 'Whopper', 'Jr Whopper']
    drinks = ['Dom Perignon', 'Lagavulin 16', 'Lil\' Sip of Sunshine', 'Hibiki', 'Diet Coke (for health)', 'Grand Marnier']
    tip_amount = [0.20, 0.18, 0.15]
    # send values in bytes
    
    order = choice(entrees) + ':' + choice(drinks) + ':' + str(choice(tip_amount))
    return bytes(order, encoding = 'utf-8')
    
def send_batch_order():
    producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
    id = [1, 2, 3, 4, 5]
    while True:
        waiter_id = bytes(str(choice(id)), encoding = 'utf-8')
        producer.send('streams-intro', key = waiter_id, value = entree_order_generator())
        print('order made')
        sleep(10)


if __name__ == '__main__':
    send_batch_order()






# would it make sense to have concurrent generators that have the same grouping (key or id)?