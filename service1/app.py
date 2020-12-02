from flask import Flask, render_template 
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    #gets a wep
    wep = requests.get("http://localhost:5001/wep")
    #gets element
    element = requests.get("http://localhost:5002/element")
    #gets character name
    character = str(wep.text) + "," + str(element.text)
    name = requests.post("http://localhost:5003/name", data=character)


    return render_template('index.html', wep=wep.text, element=element.text, name=name.text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')