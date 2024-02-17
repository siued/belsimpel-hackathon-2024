import json
import get_order
import add_items
import process_order

def wms():
    print("Welcome to the Warehouse Management System")
    print("Your warehosue is now managed!")
    command = input("Enter a command: ")

    if command == "add":
        print("Adding new items")
        with open("items.json", "w") as file:
            items = json.read(file)
        add_items.add_items(items)
    elif command == "order":
        print("Placing a new order")
        order = get_order()
        process_order.process_order(order)
    elif command == "exit":
        exit()


if __name__ == "__main__":
    wms()