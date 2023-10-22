from flask import Flask, request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
import uuid
from typing import Tuple, Optional
from helper import (check_create_store_payload, check_create_item_payload,
                    check_delete_item_payload, check_patch_item_payload)
from collections import OrderedDict
import json
from db import stores

# define a blueprint for stores Api action
bp = Blueprint("stores", __name__, description="Store's API actions")


# connect to /stores endpoint
@bp.route("/stores")
class Store(MethodView):
    def get(self) -> Tuple[dict, int]:
        print(f"TTHERE YOU GOOOOO Stores:{stores}")
        return stores, 200

    def post(self) -> Tuple[dict, int]:
        store_id = uuid.uuid4().hex
        store_data = request.get_json()
        store_data_check = check_create_store_payload(**store_data)
        if store_data_check:
            store = {**store_data, "store_id": store_id}
            stores[store_id] = store_data
            return stores, 200
        else:
            abort(400, message="missing required field store name.")


@bp.route("/stores/<string:store_id>")
class Store(MethodView):
    def delete(self, store_id):
        try:
            del stores[store_id]
            return stores
        except KeyError:
            abort(404, message="store does not exist.")

