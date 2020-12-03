from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/wep', methods=['GET'])
def wep():
<<<<<<< HEAD
    wep = ["Axe", "Hammer", "Sword", "Gun", "Staff", "Crossbow", "Fan", "Spear"]
=======
    wep = ["Axe", "Hammer", "Sword", "Gun", "Staff", "Crossbow", "Fan", "Spear"  ]
>>>>>>> developer
    return Response(random.choices(wep), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)