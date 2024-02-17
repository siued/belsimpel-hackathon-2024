from verify_ean import *

CUSTOMER = 'customer'
ORDER_ITEMS = 'order_items'
EAN = 'EAN'


class Order:
    def __init__(self, order: dict):
        self.customer = order[CUSTOMER]
        self.order_items = order[ORDER_ITEMS]
        self.eans = []
        for item in self.order_items:
            self.eans.append(item[EAN])

    def retrieve_order(self, ean: str):
        if not is_valid_ean(self.eans, ean):
            print("Incorrect EAN/item. Please put the item back on the shelf.")
            exit(1)
        # do something

