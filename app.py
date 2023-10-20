from flask import Flask, request
from flask_smorest import abort
import uuid
from typing import Tuple, Optional
from helper import check_create_store_payload, check_create_item_payload
from collections import OrderedDict
import json
from db import stores, items

app = Flask(__name__)


@app.route("/stores", methods=["GET"])
def get_all_stores() -> Tuple[dict, int]:
    return stores, 200


@app.route("/store", methods=["POST"])
def create_store() -> Tuple[dict, int]:
    store_id = uuid.uuid4().hex
    store_data = request.get_json()
    store_data_check = check_create_store_payload(**store_data)
    if store_data_check:
        store = {**store_data, "store_id": store_id}
        stores[store_id] = store
        return store, 200
    else:
        abort(400, message="missing required field store name")

# store name is passed in as parameter data


@app.route("/items", methods=["POST"])
def create_items() -> Optional[Tuple[dict, int] or None]:
    data = request.get_json()
    item_data_check = check_create_item_payload(**data)
    if not item_data_check:
        abort(400, message="required fields are incorrect or missing")
    else:
        item_id = uuid.uuid4().hex
        store_id = data.get("store_id")
        item = {**data, "store_id": store_id, "id": item_id}
        try:
            items["items"].append(item)
        except KeyError:
            items["items"] = [item]
        return item, 200


@app.route("/stores/<string:store_id>/items", methods=["GET"])
def get_items_by_store(store_id) -> [dict]:
    if store_id not in stores:
        return {"message": "store not found"}, 404
    else:
        return items[store_id], 200


@app.route("/items", methods=["GET"])
def get_all_items():
    return list(items.values()), 200


if __name__ == "__main__":
    app.run(port=8000, debug=True)

