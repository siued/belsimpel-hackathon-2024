import json
import random

def get_order():
    input_file = open ('/Users/matejkucera/Desktop/belsimpel-hackathon-2024/assignment/full_set.json')
    products = json.load(input_file)

    number_of_products = random.randint(1,10)

    customer_number = random.randint(1,1000000)
    customer = 'Customer ' + str(customer_number)

    order = {
        'customer': customer,
        'order_items': random.sample(products, number_of_products)
    }

    return order


if __name__ == "__main__":
    print(get_order())
