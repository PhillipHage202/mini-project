from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/wep', methods=['GET'])
def wep():
    wep = ["Axe", "Hammer", "Long Sword", "Dual Guns", "Staff"]
    return Response(random.choices(wep), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)