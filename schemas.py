from marshmallow import Schema, fields


class StoreSchema(Schema):
    name = fields.Str(required=True) # required = To pass in request payload
    store_id = fields.Str(dump_only=True)


class ItemSchema(Schema):
    name = fields.Str(required=True)
    store_id = fields.Str(required=True)
    price = fields.Int(required=True)
    id = fields.Str()

