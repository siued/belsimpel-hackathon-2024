import stock_manager


def add_items(items):
    for item in items:
        stock_manager.add_new_item_to_database(item)
