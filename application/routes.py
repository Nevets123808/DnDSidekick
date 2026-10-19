from flask import redirect, request, url_for, render_template
from application.models import *
from application.forms import *
from application import app, db


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/characters')
def char_list():
    chars = Character.query.all()
    return render_template('lists/charlist.html', chars = chars)


@app.route('/characters/create', methods=["GET", "POST"])
def char_create():
    form = NewCharacterForm()
    skills = [skill.skillname for skill in Skill.query.all()]
    form.skillprofs.choices = skills

    if form.validate_on_submit():
        charname = form.name.data
        profbonus = form.profbonus.data
        ac = form.armorclass.data
        hp = form.hitpoints.data
        hitdice = form.hitdice.data
        str = form.str.data
        dex = form.dex.data
        con = form.con.data
        int = form.int.data
        wis = form.wis.data
        cha = form.cha.data
        skillprofs = form.skillprofs.data
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ {skillprofs}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        character = Character(charname = charname, profbonus = profbonus, armorclass = ac, hitpoints=hp, hitdice = hitdice, str = str, dex = dex, con = con, int = int, wis = wis, cha = cha)
        db.session.add(character)
        db.session.commit()
        return redirect(url_for('char_list'))
    return render_template('news/newchar.html', form = form, mode = "New")


@app.route('/characters/<int:char_id>', methods=["GET", "POST"])
def char_update(char_id):
    character = Character.query.get(char_id)
    form = UpdateCharacterForm(obj = character)
    form.populate_obj(character)
    form.name.data = character.charname
    if form.validate_on_submit():
        character.charname = form.name.data
        character.profbonus = form.profbonus.data
        character.ac = form.armorclass.data
        character.hp = form.hitpoints.data
        character.hitdice = form.hitdice.data
        character.str = form.str.data
        character.dex = form.dex.data
        character.con = form.con.data
        character.int = form.int.data
        character.wis = form.wis.data
        character.cha = form.cha.data
        db.session.commit()
        return redirect(url_for('lists/char_list'))
    return render_template('news/newchar.html', form = form, char = character, mode="Update")

@app.route('/senses')
def sense_list():
    senses = Sense.query.all()
    return render_template('lists/senselist.html', senses = senses)

@app.route('/senses/create', methods = ['GET','POST'])
def sense_create():
    form = NewSenseForm()

    if form.validate_on_submit():
        sense_name = form.name.data
        sense = Sense(sensename= sense_name)
        db.session.add(sense)
        db.session.commit()
        return redirect(url_for('sense_list'))
    return render_template('news/newsense.html', form = form, mode = "New")

@app.route('/senses/<int:sense_id>', methods=["GET", "POST"])
def sense_update(sense_id):
    sense = Sense.query.get(sense_id)
    form = UpdateSenseForm(obj = sense)
    form.populate_obj(sense)
    form.name.data = sense.sensename
    if form.validate_on_submit():
        sense.sensename = form.name.data
        db.session.commit()
        return redirect(url_for('sense_list'))
    return render_template('news/newsense.html', form = form, sense = sense, mode = "Update")

@app.route('/languages')
def language_list():
    languages = Language.query.all()
    return render_template('lists/languagelist.html', languages = languages)

@app.route('/languages/create')
def language_create():
    pass

@app.route('/languages/update')
def language_update():
    pass

@app.route('/actions')
def action_list():
    actions = Action.query.all()
    return render_template('lists/actionlist.html', actions = actions)

@app.route('/actions/create')
def action_create():
    pass

@app.route('/actions/update')
def action_update():
    pass

@app.route('/features')
def feature_list():
    features = Feature.query.all()
    return render_template('lists/featurelist.html', features = features)

@app.route('/features/create')
def feature_create():
    pass

@app.route('/features/update')
def feature_update():
    pass

@app.route('/spells')
def spell_list():
    spells = Spell.query.all()
    return render_template('lists/spelllist.html', spells = spells)

@app.route('/spells/create')
def spell_create():
    pass

@app.route('/spells/update')
def spell_update():
    senses = Sense.query.all()
    return render_template('lists/senselist.html', senses = senses)