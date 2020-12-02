from flask import Flask, render_template 
import requests
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')
db = SQLAlchemy(app)

db.drop_all()
db.create_all()

class Char(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wep = db.Column(db.String(10))
    element = db.Column(db.String(200)) 
    name = db.Column(db.String(200)) 

@app.route('/', methods=['GET'])
def index():
    #gets a wep
    wep = requests.get("http://localhost:5001/wep")
    #gets element
    element = requests.get("http://localhost:5002/element")
    #gets character name
    character = str(wep.text) + "," + str(element.text)
    name = requests.post("http://localhost:5003/name", data=character)

    add_char = Char(wep=wep.text, element=element.text, name=name.text)
    db.session.add(add_char)
    db.session.commit()


    return render_template('index.html', wep=wep.text, element=element.text, name=name.text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')