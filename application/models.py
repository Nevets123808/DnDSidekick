from application import db

class Character(db.Model):
    char_id = db.Column(db.Integer, primary_key=True)
    charname = db.Column(db.String(50), nullable = False)