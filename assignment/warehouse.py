# this applies to one specific warehouse

def get_location_for_new_item(item):
    # create a new unique location for the order

    id = item["id"]
    return str(id) + '-location';


def get_human_readable_location(location, item):
    # convert the location to a human readable format

    id = location.replace('-location', '')

    return 'Item ' + item['description'] + 'with id ' + id + ' is located at ' + location

