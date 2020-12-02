from flask import Flask, render_template, Response, request
import requests
import random

app = Flask(__name__)

@app.route('/name', methods=['POST'])
def name():
    character = request.data.decode('utf-8')
    data = character.split(",")
    level = data[0]
    element = data[1]

    if level == "1 Star" and element == "water":
        name = "Jean"
    elif  level == "2 Star" and element == "water":
        name = "Ola"
    elif  level == "3 Star" and element == "water":
        name = "Reb"
    elif  level == "4 Star" and element == "water":
        name = "Ferg"
    elif  level == "5 Star" and element == "water":
        name = "Rookie"
    
    elif  level == "1 Star" and element == "fire":
        name = "Lilins"
    elif  level == "2 Star" and element == "fire":
        name = "Joola"
    elif  level == "3 Star" and element == "fire":
        name = "Poos"
    elif  level == "4 Star" and element == "fire":
        name = "Lollivan"
    elif  level == "5 Star" and element == "fire":
        name = "Hecka"

    elif  level == "1 Star" and element == "lightning":
        name = "Abanes"
    elif  level == "2 Star" and element == "lightning":
        name = "Rasmas"
    elif  level == "3 Star" and element == "lightning":
        name = "Goompa"
    elif  level == "4 Star" and element == "lightning":
        name = "Marar"
    else:
        name = "Jell"


    return Response(name, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)