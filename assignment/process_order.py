import stock_manager
import verify_ean

EAN = "EAN"

def process_order(order):
    eans = []
    for i in order[1]:
        eans.append[i][EAN]
    
    print(eans)

    items = 1
    while items < len(order):
        item = input("Scan the item (EAN tag): ")
        if item == "exit":
            print("Stopped processing order")
            return
        if verify_ean.ean_verified(item, eans):
            print("Item scanned.")
            items += 1
            eans.pop(eans.index(item))
        else:
            print("Invalid EAN tag. Please scan again.")
    print("All correct items scanned. Processing the order.")

    stock_manager.remove_from_stock(order[1])
    return
        
    
    