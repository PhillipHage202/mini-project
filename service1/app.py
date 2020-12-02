from flask import Flask, render_template 
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    #gets a rating
    rating = requests.get("http://localhost:5001/rating")
    #gets element
    element = requests.get("http://localhost:5002/element")
    #gets character name
    character = str(rating.text) + "," + str(element.text)
    name = requests.post("http://localhost:5003/name", data=character)


    return render_template('index.html', rating=rating.text, element=element.text, name=name.text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')