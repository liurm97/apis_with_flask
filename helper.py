from typing import Optional, List, Tuple

# Check if store name exists


def store_exists(store_name, list_of_stores: list[dict]) -> Optional[Tuple[bool, int] or None]:
    store_position = 0
    while store_position < len(list_of_stores):
        if store_name == list_of_stores[store_position]['name']:
            return True, store_position
        store_position += 1
    return False, -999