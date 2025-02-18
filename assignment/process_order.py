import stock_manager
import verify_ean

EAN = "EAN"
CUSTOMER = "customer"
ORDER_ITEMS = "order_items"


def process_order(order):
    eans = []
    order_items = order[ORDER_ITEMS]
    for item in order_items:
        eans.append(item[EAN])

    print("Customer: " + order[CUSTOMER] + " ordered the following items:")
    print(eans)

    locations = [stock_manager.get_item_location_from_database(item) for item in order_items]
    print("Item locations:")
    for location in locations:
        print(location)

    items = 0
    while items < len(eans):
        item = input("Scan the item (EAN tag), type exit to cancel: ")
        if item == "bypass":
            break

        if item == "exit":
            print("Stopped processing order")
            return

        if verify_ean.ean_verified(item, eans):
            print("Item scanned.")
            items += 1
        else:
            print("Invalid EAN tag. Please scan again.")

    print("All correct items scanned. Processing the order.")

    stock_manager.remove_item_from_database(order[ORDER_ITEMS])
    return
