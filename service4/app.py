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

    if wep == "Staff" and element == "Water":
        name = "Jean the Mage"
    elif  wep == "Spear" and element == "Water":
        name = "Aqua Warrior"
    elif  wep == "Fan" and element == "Water":
        name = "Reb"
    elif  wep == "Axe" and element == "Water":
        name = "Ferg"
    elif  wep == "Hammer" and element == "Water":
        name = "Rookie"
    
    elif  wep == "Sword" and element == "Fire":
        name = "Lilins"
    elif  wep == "Fan" and element == "Fire":
        name = "Joola"
    elif  wep == "Spear" and element == "Fire":
        name = "Poos"
    elif  wep == "Crossbow" and element == "Fire":
        name = "Lollivan"
    elif  wep == "Gun" and element == "Fire":
        name = "Hecka"
    
    elif  wep == "Sword" and element == "Air":
        name = "Lilly"
    elif  wep == "Axe" and element == "Air":
        name = "Waz"
    elif  wep == "Sword" and element == "Air":
        name = "Ben"
    elif  wep == "Fan" and element == "Air":
        name = "Dan"
    elif  wep == "Hammer" and element == "Air":
        name = "Julia"
    
    elif  wep == "Sword" and element == "Earth":
        name = "Rocky"
    elif  wep == "Fan" and element == "Earth":
        name = "Hoop"
    elif  wep == "Gun" and element == "Earth":
        name = "King"
    elif  wep == "Staff" and element == "Earth":
        name = "Hector"
    elif  wep == "Hammer" and element == "Earth":
        name = "Lee"

    elif  wep == "Crossbow" and element == "Lightning":
        name = "Anook"
    elif  wep == "Gun" and element == "Lightning":
        name = "Vigo"
    elif  wep == "Spear" and element == "Lightning":
        name = "Vino"
    elif  wep == "Hammer" and element == "Lightning":
        name = "Jack"
    else:
        name = "Dara"


    return Response(name, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)