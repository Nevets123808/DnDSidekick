from application import db

# Many-to-Many tables for Skills, Senses etc.
character_skills = db.Table(
    "character_skills",
    db.Column("char_id", db.Integer, db.ForeignKey("character.char_id")),
    db.Column("skill_id", db.Integer, db.ForeignKey("skill.skill_id")),
)

character_senses = db.Table(
    "character_senses",
    db.Column("char_id", db.Integer, db.ForeignKey("character.char_id")),
    db.Column("sense_id", db.Integer, db.ForeignKey("sense.sense_id")),
)

character_languages = db.Table(
    "character_languages",
    db.Column("char_id", db.Integer, db.ForeignKey("character.char_id")),
    db.Column("language_id", db.Integer, db.ForeignKey("language.language_id")),
)

character_features = db.Table(
    "character_features",
    db.Column("char_id", db.Integer, db.ForeignKey("character.char_id")),
    db.Column("feature_id", db.Integer, db.ForeignKey("feature.feature_id")),
)

character_actions = db.Table(
    "character_actionss",
    db.Column("char_id", db.Integer, db.ForeignKey("character.char_id")),
    db.Column("action_id", db.Integer, db.ForeignKey("action.action_id")),
)

character_spells = db.Table(
    "character_spells",
    db.Column("char_id", db.Integer, db.ForeignKey("character.char_id")),
    db.Column("spell_id", db.Integer, db.ForeignKey("spell.spell_id")),
)

class Character(db.Model):
    __tablename__ = "character"
    char_id = db.Column(db.Integer, primary_key=True)
    charname = db.Column(db.String(50), nullable = False)
    profbonus= db.Column(db.Integer)
    armorclass = db.Column(db.Integer)
    hitpoints = db.Column(db.Integer)
    hitdice = db.Column(db.String(10))
    str = db.Column(db.Integer)
    dex = db.Column(db.Integer)
    con = db.Column(db.Integer)
    int = db.Column(db.Integer)
    wis = db.Column(db.Integer)
    cha = db.Column(db.Integer)
    skillprofs =  db.relationship("Skill", secondary=character_skills, back_populates="characters")
    senses =  db.relationship("Sense", secondary=character_senses, back_populates="characters")
    languages =  db.relationship("Language", secondary=character_languages, back_populates="characters")
    features =  db.relationship("Feature", secondary=character_features, back_populates="characters")
    actions =  db.relationship("Action", secondary=character_actions, back_populates="characters")
    spells =  db.relationship("Spell", secondary=character_spells, back_populates="characters")
    
class Skill(db.Model):
    skill_id = db.Column(db.Integer, primary_key = True)
    skillname = db.Column(db.String(50), nullable = False)
    characters = db.relationship("Character", secondary=character_skills, back_populates="skillprofs")

class Sense(db.Model):
    sense_id = db.Column(db.Integer, primary_key = True)
    sensename = db.Column(db.String(50), nullable = False)
    characters = db.relationship("Character", secondary=character_senses, back_populates="senses")

class Language(db.Model):
    language_id = db.Column(db.Integer, primary_key = True)
    languagename = db.Column(db.String(50), nullable = False)
    characters = db.relationship("Character", secondary=character_languages, back_populates="languages")

class Feature(db.Model):
    feature_id = db.Column(db.Integer, primary_key = True)
    featurename = db.Column(db.String(50), nullable = False)
    source = db.Column(db.String(50))
    description = db.Column(db.String(50))
    characters = db.relationship("Character", secondary=character_features, back_populates="features")

class Action(db.Model):
    action_id = db.Column(db.Integer, primary_key = True)
    actionname = db.Column(db.String(50), nullable = False)
    source = db.Column(db.String(50))
    description = db.Column(db.String(50))
    characters = db.relationship("Character", secondary=character_actions, back_populates="actions")

class Spell(db.Model):
    spell_id = db.Column(db.Integer, primary_key = True)
    spellname = db.Column(db.String(50), nullable = False)
    spelllevel= db.Column(db.Integer)
    school = db.Column(db.String(50))
    description = db.Column(db.String(50))
    characters = db.relationship("Character", secondary=character_spells, back_populates="spells")