from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField, IntegerField, SubmitField
from wtforms.widgets import CheckboxInput, ListWidget
from wtforms.validators import data_required

class SelectMultipleCheckboxesField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

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
    skillprofs = SelectMultipleCheckboxesField("Skill Profs", choices = [])
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
    skillprofs = SelectMultipleCheckboxesField("Skill Profs", choices = [])
    submit = SubmitField("Update Character")

class NewActionForm(FlaskForm):
    name = StringField("Name: ")# validators=[data_required()])
    source = StringField("Source: ")
    description = StringField("Description: ")
    submit = SubmitField("Create Action")

class UpdateActionForm(FlaskForm):
    name = StringField("Name: ")# validators=[data_required()])
    source = StringField("Source: ")
    description = StringField("Description: ")
    submit = SubmitField("Update Action")

class NewFeatureForm(FlaskForm):
    name = StringField("Name: ")# validators=[data_required()])
    source = StringField("Source: ")
    description = StringField("Description: ")
    submit = SubmitField("Update Action")

class UpdateFeatureForm(FlaskForm):
    name = StringField("Name: ")# validators=[data_required()])
    source = StringField("Source: ")
    description = StringField("Description: ")
    submit = SubmitField("Update Action")

class NewSpellForm(FlaskForm):
    name = StringField("Name: ")# validators=[data_required()])
    spelllevel = StringField("Spell Level: ")
    school = StringField("School: ")
    description = StringField("Description: ")
    submit = SubmitField("Update Action")

class UpdateSpellForm(FlaskForm):
    name = StringField("Name: ")# validators=[data_required()])
    spelllevel = StringField("Spell Level: ")
    school = StringField("School: ")
    description = StringField("Description: ")
    submit = SubmitField("Update Action")

class NewSenseForm(FlaskForm):
    name = StringField("Name: ")# validators=[data_required()])
    submit = SubmitField("Update Action")

class UpdateSenseForm(FlaskForm):
    name = StringField("Name: ")# validators=[data_required()])
    submit = SubmitField("Update Action")