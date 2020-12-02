from flask import Flask, render_template, Response, request
import requests
import random

app = Flask(__name__)

@app.route('/name', methods=['POST'])
def name():
    character = request.data.decode('utf-8')
    data = character.split(",")
    wep = data[0]
    element = data[1]

    if wep == "Staff" and element == "water":
        name = "Jean the Mage"
    elif  wep == "2 Star" and element == "water":
        name = "Ola"
    elif  wep == "3 Star" and element == "water":
        name = "Reb"
    elif  wep == "4 Star" and element == "water":
        name = "Ferg"
    elif  wep == "5 Star" and element == "water":
        name = "Rookie"
    
    elif  wep == "1 Star" and element == "fire":
        name = "Lilins"
    elif  wep == "2 Star" and element == "fire":
        name = "Joola"
    elif  wep == "3 Star" and element == "fire":
        name = "Poos"
    elif  wep == "4 Star" and element == "fire":
        name = "Lollivan"
    elif  wep == "5 Star" and element == "fire":
        name = "Hecka"

    elif  wep == "1 Star" and element == "lightning":
        name = "Abanes"
    elif  wep == "2 Star" and element == "lightning":
        name = "Rasmas"
    elif  wep == "3 Star" and element == "lightning":
        name = "Goompa"
    elif  wep == "4 Star" and element == "lightning":
        name = "Marar"
    else:
        name = "Jell"


    return Response(name, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)