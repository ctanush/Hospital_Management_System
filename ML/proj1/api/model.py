from . import db

class pred_data(db.Model):
     id1 = db.Column(db.Integer,primary_key=True)
     name = db.Column(db.String(50));
     gender = db.Column(db.String(10));
     age = db.Column(db.Double);
     value = db.Column(db.String(50));
    