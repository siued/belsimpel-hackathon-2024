def get_location_for_new_order(item):
    # create a new unique location for the order

    id = item["id"]
    return str(id) + '-location';


def get_human_readable_location(location, item):
    # convert the location to a human readable format

    id = location.replace('-location', '')

    return 'Item ' + item['description'] + 'with id ' + id + ' is located at ' + location


item = {
        "id": "3526",
        "description": "Google Pixel 8 128GB Black",
        "IMEI": "331065863440734",
        "EAN": "840244706692",
        "price": "450.00"
    }
print(get_human_readable_location(get_location_for_new_order(item), item))