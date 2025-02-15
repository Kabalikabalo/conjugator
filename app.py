from flask import Flask, jsonify
from flask_cors import CORS
from verbecc import Conjugator

app = Flask(__name__)
CORS(app)  # Enable CORS for the Flask app

@app.route('/conjugate/<lang>/<verb>', methods=['GET'])
def conjugate(lang, verb):
    cg = Conjugator(lang=lang)
    conjugation = cg.conjugate(verb)
    return jsonify(conjugation)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
