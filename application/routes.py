from flask import redirect, request, url_for, render_template
from application.models import Character
from application import app, db


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/characters')
def char_list():
    chars = Character.query.all()
    return render_template('charlist.html', chars = chars)


@app.route('/create', methods=["POST"])
def char_create():
    char = Character(
        charname = "Elathon"
    )
    db.session.add(char)
    db.session.commit()

