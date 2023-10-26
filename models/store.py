from db import db

class StoreModel(db.Model):
    __tablename__= "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    # List of nested item objects
    items = db.relationship("ItemModel", back_populate="store", lazy="dynamic")

