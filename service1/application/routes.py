from flask import render_template
from application import app, db
from application.models import Char
import requests

@app.route('/', methods=['GET'])
def home():
    char_data = Char.query.all()
    return render_template('index.html'), chars=char_data)


@app.route('/get_char', methods=['GET'])
def index():
    gets a wep
    wep = requests.get("http://service2:5001/wep")
    #gets element
    element = requests.get("http://:service3/element")
    #gets character name
    character = str(wep.text) + "," + str(element.text)
    name = requests.post("http://service4:5003/name", data=character)

    add_char = Char(wep=wep.text, element=element.text, name=name.text)
    db.session.add(add_char)
    db.session.commit()



    return render_template('index.html', wep=wep.text, element=element.text, name=name.text)
