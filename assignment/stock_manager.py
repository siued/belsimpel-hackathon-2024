#import database_controller as database  # Database Controller class that implements getters and setters
import location_manager

# import order retrieval
# import new item retreival


def add_new_item_to_database(item, warehouse="warehouse1"):
    db_location, _ = location_manager.create_new_item_location(item, warehouse)

    print(item, db_location)
    database.add_item(item)
    database.add_location_to_item(item, db_location)


def add_order_to_database(order):
    database.add_order(order)


def get_item_from_database(item):
    return database.get_item(item)


def get_item_location_from_database(item):
    return database.get_location(item)


def remove_item_from_database(items_to_remove):
    for item in items_to_remove:
        database.remove_item(item)
