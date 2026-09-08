
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
    skills = [Skill(skillname = skillname) for skillname in skillnames]
    db.session.add_all(skills)
    db.session.commit()

    #Create senses
    sensenames = [
        "darkvision",
        "tremorsense",
        "blindsight"
    ]
    senses = [Sense(sensename = sensename) for sensename in sensenames]

    db.session.add_all(senses)
    db.session.commit()

    #Create Languages
    languagenames = [
        "common",
        "dwarvish",
        "elvish",
        "gnomish",
        "giant"
    ]

    languages = [Language(languagename = languagename) for languagename in languagenames]

    db.session.add_all(languages)
    db.session.commit()

    char = Character(
        charname = "Elathon",
        profbonus= 2,
        armorclass = 10,
        hitpoints = 10,
        hitdice = "1d6",
        str = 10,
        dex = 10,
        con = 10,
        int = 10,
        wis = 10,
        cha = 10,
    )
    db.session.add(char)
    db.session.commit()

    chars = db.session.execute(db.select(Character.charname).order_by(Character.charname))

    print([char for char in chars])