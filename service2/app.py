from flask import Flask
app = Flask(__name__)

animals = {'cow':'moo', 'dog':'woof', 'cat':'meow'}

@app.route('/animal')
def get_animal():
    return jsonify(random.choice(animals).key())

@app.route('/noise/<string:animal>', methods=['POST'])
def get_sound(animal):
    return jsonify(animals.get(animal))

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0/0') 