import database_controller as database
import location_manager
import numpy as np

# import order retrieval
# import new item retreival


class Stock_Manager:
    def __init__(self) -> None:
        self.incoming_order = None  # A cron job?
        self.new_item = None
        self.database = None  # Database Controller class that implements getters and setters
        self.warehouses = tuple(
            "warehouse1", "warehouse2", "warehouse3", "warehouse4"
        )
        self.location_manager = (
            None  # Location manager that generates the location for the item
        )

        self.items_in_warehouse = None  # database.get_all_items()
        self.n_items_in_warehouse = len(self.items_in_warehouse)
        self.location_of_item = str(None)

    def add_new_item_to_database(self, item):
        location = location_manager.create_new_item_location(item, warehouse)
        database.add_location(item, location)

    def add_order_to_database(self, order):
        database.add_order(order)

        pass

    def get_item_from_database(self):
        pass

    def get_item_location_from_database(self, item):
        item_location = database.get_location(item)

        return item_location
