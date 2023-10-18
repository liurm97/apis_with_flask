from flask import Flask, request
from typing import Tuple, Optional
import helper
from collections import OrderedDict
import json

app = Flask(__name__)

stores = {
    "stores": [
        {
            "items": [
                {
                    "name": "chair",
                    "price": 15.99
                }
            ],
            "name": "My Store"
        }
    ]
}


@app.route("/stores", methods=["GET"])
def get_all_stores() -> Optional[Tuple[dict, int] or None]:
    try:
        return stores, 200
    except SyntaxError:
        return "Something wrong happened", 400


@app.route("/store", methods=["POST"])
def create_store() -> Optional[Tuple[dict, int] or None]:
    try:
        #1 get data from requests
        body = request.get_json()
        new_store = {"name": body['name'], "items": []}
        stores['stores'].append(new_store)
        return new_store, 201
    except SyntaxError:
        return {"message":"Something wrong happened"}, 400


# store name is passed in as parameter data
@app.route("/store/<string:store_name>", methods=["POST"])
def create_items(store_name) -> Optional[Tuple[str, int] or None]:
    store_exists, store_position = helper.store_exists(store_name, stores['stores'])
    if store_exists:
        items_data = request.get_json()
        stores['stores'][store_position]['items'].append(items_data)
        return stores, 201
    return {"message": "store not found"}, 400


@app.route("/store/<string:store_name>/items", methods=["GET"])
def get_items_by_store(store_name) -> [dict]:
    store_exists, store_position = helper.store_exists(store_name, stores['stores'])
    if store_exists:
        return {
            "message": "Successful",
            "items": stores['stores'][store_position]['items']}, 200
    else:
        return {"message": "store does not exist"}, 404



if __name__ == "__main__":
    app.run(port=8000, debug=True)
