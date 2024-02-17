import warehouse

# in the future, this extends to multiple warehouses

def create_new_item_location(item, warehouse_name):
    if warehouse_name == 'warehouse1':
        db_location = warehouse.get_location_for_new_item(item)
        user_location = warehouse.get_human_readable_location(db_location, item)
        return db_location, user_location


def convert_db_location_to_human_readable(db_location, item):
    if warehouse == 'warehouse1':
        user_location = warehouse.get_human_readable_location(db_location, item)
        return user_location