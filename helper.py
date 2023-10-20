from typing import Optional, List, Tuple

# Check if store name exists

# def store_exists(store_name, list_of_stores: list[dict]) -> Optional[Tuple[bool, int] or None]:
#     store_position = 0
#     while store_position < len(list_of_stores):
#         if store_name == list_of_stores[store_position]['name']:
#             return True, store_position
#         store_position += 1
#     return False, -999

# Check request json payload


def check_create_store_payload(**kwargs: dict) -> bool:
    """
    store payload must have only 1 key:
    1) name
    """
    # retrieve payload
    if "name" not in kwargs or len(kwargs.keys()) > 1:
        return False
    return True


def check_create_item_payload(**kwargs: dict) -> bool:
    """
    items payload must have 3 keys:
    1) store_id: str
    2) name: str
    3) price: float
    """
    if len(kwargs.keys()) > 3:
        return False

    if "store_id" not in kwargs:
        return False

    if "name" not in kwargs:
        return False

    if "price" not in kwargs:
        return False

    if type(kwargs["store_id"]) != str:
        return False

    if type(kwargs["name"]) != str:
        return False

    if type(kwargs["price"]) != float:
        return False

    return True