# import database_controller as database  # Database Controller class that implements getters and setters
import location_manager
import db_connection as database

# import order retrieval
# import new item retreival


def add_new_item_to_database(item, warehouse="warehouse1"):
    db_location, _ = location_manager.create_new_item_location(item, warehouse)
    item['location'] = db_location
    item['stock'] = 1


    # here check for stock and either add new item or increase stock
    database.add_item(item)


# def add_order_to_database(order):
#     database.add_order(order)


# def get_item_from_database(item):
#     return database.get_item(item)


def get_item_location_from_database(ean):
    return location_manager.convert_db_location_to_human_readable(database.get_location(ean))


def remove_item_from_database(items_to_remove):
    for item in items_to_remove:
        pass


def get_stock(id):
    item = database.get_item(id)
    return item['stock']
