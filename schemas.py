from marshmallow import Schema, fields


class PlainStoreSchema(Schema):
    name = fields.Str(required=True) # required = To pass in request payload
    store_id = fields.Str(dump_only=True)


class PlainItemSchema(Schema):
    name = fields.Str(required=True)
    # store_id = fields.Str(required=True)
    price = fields.Float(required=True)
    id = fields.Str(dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema(), dump_only=True))


class ItemSchema(PlainItemSchema):
    store_id = fields.Str(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)