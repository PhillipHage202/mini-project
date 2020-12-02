from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/rating', methods=['GET'])
def rating():
    ratings = ["1 Star", "2 Star", "3 Star", "4 Star", "5 Star"]
    return Response(random.choices(ratings), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)