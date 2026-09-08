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
    return render_template('charlist.html', chars = chars)


@app.route('/create', methods=["GET", "POST"])
def char_create():
    form = NewCharacterForm()

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
        character = Character(charname = charname, profbonus = profbonus, armorclass = ac, hitpoints=hp, hitdice = hitdice, str = str, dex = dex, con = con, int = int, wis = wis, cha = cha)
        db.session.add(character)
        db.session.commit()
        return redirect(url_for('char_list'))
    return render_template('newchar.html', form = form)


@app.route('/<int:char_id>', methods=["GET", "POST"])
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
        return redirect(url_for('char_list'))
    return render_template('newchar.html', form = form, char = character)

