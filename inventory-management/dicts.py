"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    counts = dict()
    for item in items:
        counts[item] = items.count(item)
    return counts


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    items=create_inventory(items)
    updated = {**inventory, **items}
    for key, value in updated.items():
        if key in inventory and key in items:
                updated[key] = value+inventory[key]
    return updated


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    items=create_inventory(items)
    updated = {**inventory, **items}
    for key, value in updated.items():
        if key in inventory and key in items:
                if inventory[key]>value:
                    updated[key] = inventory[key]-value
                else:
                     updated[key]=0
    return updated


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
         inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    list_inv = []
    for key, value in inventory.items():
        if value > 0:
            list_inv.append((key, value))
    return list_inv
         