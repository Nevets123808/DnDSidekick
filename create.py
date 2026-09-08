
from application import app, db
from application.models import *

with app.app_context():
    db.drop_all()
    db.create_all()

    #Create Skills
    skillnames = [
        "Acrobatics",
        "Animal Handling",
        "Arcana",
        "Athletics",
        "Deception",
        "History",
        "Insight",
        "Intimidation",
        "Investigation",
        "Medicine",
        "Nature",
        "Perception",
        "Performance",
        "Persusasion",
        "Religion",
        "Sleight of Hand",
        "Stealth",
        "Survival"
    ]
    char = Character(
        charname = "Elathon"
    )
    db.session.add(char)
    db.session.commit()

    chars = db.session.execute(db.select(Character.charname).order_by(Character.charname))

    print([char for char in chars])