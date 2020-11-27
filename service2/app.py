from flask import Flask, Response

import random
app = Flask(__name__)


@app.route('/animal')
def animal():
    animals = ["cow","dog","cat"]
    return Response(random.choices(animals), mimetype="text/plain")

@app.route('/noise', methods=['POST'])
def noise ():
    animal = request.data.decode('utf-8')
    if animal == "cow":
        noise = "moo"
    elif animal == "dog":
        noise = "woof"
    else:
        noise = "meow"
    return Response (noise, mimetype= "text/plain")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 