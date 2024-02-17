import stock_manager
import verify_ean

EAN = "EAN"

def process_order(order):
    eans = []
    for i in order[1]:
        eans.append[i][EAN]
    
    print("Customer: " + order[0] + " ordered the following items:")
    print(eans)

    items = 0
    while items < len(order):
        item = input("Scan the item (EAN tag), type exit to exit: ")
        if item == "exit":
            print("Stopped processing order")
            return
        if verify_ean.ean_verified(item, eans):
            print("Item scanned.")
            items += 1
        else:
            print("Invalid EAN tag. Please scan again.")
    print("All correct items scanned. Processing the order.")

    stock_manager.remove_from_stock()
    return
        
