from flask import Flask, request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
import uuid
from typing import Tuple, Optional
from helper import (check_create_store_payload, check_create_item_payload,
                    check_delete_item_payload, check_patch_item_payload)
from collections import OrderedDict
import json
from db import items, stores

# define a blueprint for stores Api action
bp = Blueprint("items", __name__, description="Item's API actions")


# 4 GET ALL ITEMS IN A STORE
@bp.route("/items/<string:store_id>")
class Item(MethodView):
    def get(self,store_id) -> [dict]:
        print(store_id)
        if store_id not in stores:
            return {"message": "store not found"}, 404
        else:
            print(items)
            return items[store_id], 200


# 5 GET ALL ITEMS
@bp.route("/items")
class Item(MethodView):
    def get(self):
        print(items)
        return items, 200

# 6 ADD AN ITEM TO A STORE
    def post(self) -> Optional[Tuple[dict, int] or None]:
        data = request.get_json()
        item_data_check = check_create_item_payload(**data)
        if not item_data_check:
            abort(400, message="required fields are incorrect or missing")
        else:
            item_id = uuid.uuid4().hex
            store_id = data.get("store_id")
            item = {**data, "id": item_id}
            try:
                # append data into an existing list
                data = {"id": item_id, "name": data["name"], "price": data["price"]}
                items[store_id].append(data)
            except KeyError:
                # wrap data into list if there is no list
                items[store_id] = [data]
            return item, 200

# 7 DELETE AN ITEM FROM A STORE
    def delete(self):
        data = request.get_json()
        data_check = check_delete_item_payload(**data)
        if not data_check:
            abort(400, message="required fields are not satisfied.")
        else:
            store_id = data.get("store_id")
            if store_id not in stores:
                abort(404, message="store is not found.")
            else:
                items_in_store = items.get(store_id)
                for i, v in enumerate(items_in_store):
                    if v["id"] == data.get("id"):
                        del items[store_id][i]
                        return {"message": "data has been deleted."}, 200
                abort(404, message="item is not present in store.")


# 8 PATCH AN ITEM FROM A STORE
    def patch(self):
        data = request.get_json()
        data_check = check_patch_item_payload(**data)
        if not data_check:
            abort(400, message="required fields are not satisfied.")
        else:
            store_id = data["store_id"]
            # Check if store exists
            if store_id not in stores:
                abort(404, message="store does not exist.")
            else:
                # if "name" and "price" are both present
                try:
                    new_item = {"price": data["price"], "name": data["name"]}
                    for i, v in enumerate(items[store_id]):
                        if data["id"] == v["id"]:
                            # update the item field
                            v |= new_item
                            return v, 200
                except KeyError:
                    # if only "price" is present
                    new_item = {"price": data["price"]}
                    for i, v in enumerate(items[store_id]):
                        if data["id"] == v["id"]:
                            # update the item field
                            v |= new_item
                        return v, 200
                abort(404, message="item does not exist.")