from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, SubmitField

from wtforms.validators import data_required

class NewCharacterForm(FlaskForm):
    name = StringField("Name: ")# validators=[data_required()])
    profbonus = IntegerField("Prof Bonus: ")
    armorclass = IntegerField("Armor Class: ")
    hitpoints = IntegerField("Hit Points: ")
    hitdice = StringField("Hit Dice: ")
    str = IntegerField("Str: ")
    dex = IntegerField("Dex: ")
    con = IntegerField("Con: ")
    int = IntegerField("Int: ")
    wis = IntegerField("Wis: ")
    cha = IntegerField("Cha: ")
    submit = SubmitField("Create Character")

class UpdateCharacterForm(FlaskForm):
    name = StringField("Name: ")# validators=[data_required()])
    profbonus = IntegerField("Prof Bonus: ")
    armorclass = IntegerField("Armor Class: ")
    hitpoints = IntegerField("Hit Points: ")
    hitdice = StringField("Hit Dice: ")
    str = IntegerField("Str: ")
    dex = IntegerField("Dex: ")
    con = IntegerField("Con: ")
    int = IntegerField("Int: ")
    wis = IntegerField("Wis: ")
    cha = IntegerField("Cha: ")
    submit = SubmitField("Update Character")