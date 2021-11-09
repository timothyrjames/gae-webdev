import sldatastorage
from slobjects import ShoppingListItem


def get_list_items():
    return sldatastorage.get_list_items()


def save_list_item(item_id, title, q):
    item = ShoppingListItem(item_id, title, q)
    sldatastorage.save_list_item(item)


def create_list_item(title, q):
    item = ShoppingListItem(None, title, q)
    sldatastorage.create_list_item(item)


def delete_list_item(sli_id):
    sldatastorage.delete_list_item(sli_id)


def get_list_item(item_id):
    return sldatastorage.get_list_item(item_id)
    