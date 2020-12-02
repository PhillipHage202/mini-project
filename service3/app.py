from flask import Flask, render_template, Response, request 
import requests
import random

app = Flask(__name__)

@app.route('/element', methods=['GET'])
def element():
    element = ["water", "fire", "lightning"]
    return Response(random.choices(element), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)