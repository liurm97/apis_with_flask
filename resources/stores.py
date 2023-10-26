from flask import Flask, request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
import uuid
from typing import Tuple, Optional
from helper import (check_create_store_payload, check_create_item_payload,
                    check_delete_item_payload, check_patch_item_payload)
from collections import OrderedDict
import json
# from db import stores
import pandas as pd
from schemas import PlainItemSchema, PlainStoreSchema, StoreSchema, ItemSchema

# define a blueprint for stores Api action
bp = Blueprint("stores", __name__, description="Store's API actions")


# connect to /stores endpoint
@bp.route("/stores")
class Store(MethodView):
    @bp.response(200, PlainStoreSchema(many=True)) # [List] returns many instances of StoreSchema
    def get(self) -> Tuple[dict, int]:
        return stores["results"], 200

    @bp.arguments(StoreSchema) # Validates request body
    def post(self, store_data) -> Tuple[dict, int]:
        # store_data = request.get_json()
        print(f"After passing through Schema: {store_data}")
        store_id = uuid.uuid4().hex
        store = {**store_data, "store_id": store_id}
        stores["results"].append(store)
        return stores, 200


@bp.route("/stores/<string:store_id>")
class Store(MethodView):
    def delete(self, store_id):
        try:
            del stores[store_id]
            return stores
        except KeyError:
            abort(404, message="store does not exist.")

