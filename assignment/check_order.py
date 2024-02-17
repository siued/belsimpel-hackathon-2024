import db_connection as database

def check_order():
    while True:     
        order_id = input("Input the order ID, type exit to exit: ")
        match order_id:
            case "exit":
                print("Stopped searching for order")
                break
            case "":
                print("Must have a correct order ID")
            case _:
                items = database.get_order()
                if items is None:
                    print("There is no order attached to that ID.")
                else:
                    print(items)
    return