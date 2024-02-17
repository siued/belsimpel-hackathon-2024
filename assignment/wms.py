import json

import add_items
import get_order
import process_order

COMMANDS = "add/order/exit"


def wms():
    print("Welcome to the Warehouse Management System")
    print("Your warehosue is now managed!")

    while True:
        command = input("Enter a command:" + COMMANDS + "\n")
        match command:
            case "add":
                print("Adding new items")
                with open("./assignment/full_set.json", "r") as file:
                    items = json.load(file)
                add_items.add_items(items)
            case "order":
                print("Placing a new order")
                order = get_order.get_order()
                process_order.process_order(order)
            case "exit":
                exit()


if __name__ == "__main__":
    wms()
