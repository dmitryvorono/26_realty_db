from app import db


class Advertisement(db.Model):
    __tablename__ = 'advertisement'
    id = db.Column(db.Integer, primary_key=True)
    premise_area = db.Column(db.Float)
    rooms_number = db.Column(db.Integer)
    construction_year = db.Column(db.Integer)
    address = db.Column(db.String)
    has_balcony = db.Column(db.Boolean)
    living_area = db.Column(db.Float)
    oblast_district = db.Column(db.String)
    price = db.Column(db.Float)
    description = db.Column(db.String)
    under_construction = db.Column(db.Boolean)
    settlement = db.Column(db.String)
