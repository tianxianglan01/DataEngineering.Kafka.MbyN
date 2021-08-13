from kafka import KafkaConsumer
from time import sleep




def consumer1():
    consumer = KafkaConsumer('streams-intro',  bootstrap_servers = 'localhost:9092')

# <class 'kafka.consumer.fetcher.ConsumerRecord'>
    for msg in consumer:
        # order = msg.split(':')
        # print(msg.key, msg.value)
        print(msg.key, msg.value.decode('utf-8'))
        order = msg.value.decode('utf-8').split(':')
        print(total_cost(order))
        
        sleep(3)

def total_cost(lst):
    meal_price = 0
    entree_prices = {
    'Chicken Fries': 5.00, 'Mozzarella Sticks': 7.50, 'Cheeto Dust': 75.00, 
    'Whopper': 4.00, 'Jr Whopper': 3.50
    }

    drink_price = {
        'Dom Perignon': 40.00, 'Lagavulin 16': 25.00, 'Lil\' Sip of Sunshine': 17.00, 
        'Hibiki': 20.00, 'Diet Coke (for health)': 1.00, 'Grand Marnier': 17.00

    }

    meal_price = entree_prices[lst[0]] + drink_price[lst[1]]
    total_cost = round(meal_price * (1 + float(lst[2])), 2)
    items_ordered = 'Entree: ' + lst[0] + ', $' + str(entree_prices[lst[0]]) + '\nDrink: ' + lst[1] + ', $' + str(drink_price[lst[1]]) + '\n'
    
    
    #round((1 + (float(lst[2])) * (entree_prices[lst[0]] + drink_price[lst[1]])), 2)
    return items_ordered + '\n' + 'Meal cost $' + str(total_cost) + '\n'



# python3 producer.py

if __name__ == '__main__':
    consumer1()


'''
ConsumerRecord(topic='streams-intro', partition=0, 
offset=54, timestamp=1628696069041, timestamp_type=0, key=b'1', 
value=b'Whopper:Grand Marnier:0.2', headers=[], checksum=None, s
erialized_key_size=1, serialized_value_size=25, serialized_header_size=-1)


'''
