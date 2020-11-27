from flask import Flask,  request

import requests

app = Flask(__name__)
@app.route('/', methods =['GET'])
def index():            
    # get animal
    animal = requests.get("http://34.105.151.78:5001/animal")
    # get noise
    noise = requests.post("http://34.105.151.78:5001/noise", data=animal.text)

    return render_template ('index.html', animal=animal.text, noise=noise.text )

if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0', port=5000)