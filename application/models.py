from application import db

class Character(db.Model):
    __tablename__ = "character"
    char_id = db.Column(db.Integer, primary_key=True)
    charname = db.Column(db.String(50), nullable = False)
    armorclass = db.column(db.Integer)
    hitpoints = db.Column(db.Integer)
    hitdice = db.Column(db.String(10))
    str = db.Column(db.Integer)
    dex = db.Column(db.Integer)
    con = db.Column(db.Integer)
    int = db.Column(db.Integer)
    wis = db.Column(db.Integer)
    cha = db.Column(db.Integer)
    #skillprofs =  {one to many}
    # senses = {one to many}
    #languages = {one to many}
    #features = {one to many}
    #actions = {one to many}
    
class Skill(db.Model):
    skill_id = db.Column(db.Integer, primary_key = True)
    skillname = db.Column(db.String(50))