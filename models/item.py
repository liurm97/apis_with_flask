from db import db

class ItemModel(db.Model):
    __tablename__= "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=True)
    # Nested Store obj
    store = db.relationship("StoreModel", back_populates="items")