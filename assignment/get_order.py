import json
import random

input_file = open ('full_set.json')
products = json.load(input_file)

number_of_products = random.randint(1,10)

customer_number = random.randint(1,1000000)
customer = 'Customer ' + str(customer_number)

order = {
    'customer': customer,
    'order_items': random.sample(products, number_of_products)
}

print(order)
