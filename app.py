from flask import Flask, request, jsonify, render_template
from caesar_cipher import caesar_cipher
from morse_code import encode_morse, decode_morse
from vigenere_cipher import vigenere_cipher

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar/encode', methods=['POST'])
def caesar_encode():
    data = request.get_json()
    text = data['text']
    try:
        shift = int(data.get('key', 3)) if data.get('key') else 3
    except ValueError:
        shift = 3
    result = caesar_cipher(text, shift)
    return jsonify({'result': result})

@app.route('/caesar/decode', methods=['POST'])
def caesar_decode():
    data = request.get_json()
    text = data['text']
    try:
        shift = int(data.get('key', 3)) if data.get('key') else 3
    except ValueError:
        shift = 3
    result = caesar_cipher(text, shift, decode=True)
    return jsonify({'result': result})

@app.route('/morse/encode', methods=['POST'])
def morse_encode():
    data = request.get_json()
    text = data['text']
    result = encode_morse(text)
    return jsonify({'result': result})

@app.route('/morse/decode', methods=['POST'])
def morse_decode():
    data = request.get_json()
    text = data['text']
    result = decode_morse(text)
    return jsonify({'result': result})

@app.route('/vigenere/encode', methods=['POST'])
def vigenere_encode():
    data = request.get_json()
    text = data['text']
    key = data.get('key', 'KEY')  # Provide a default key if none is provided
    result = vigenere_cipher(text, key)
    return jsonify({'result': result})

@app.route('/vigenere/decode', methods=['POST'])
def vigenere_decode():
    data = request.get_json()
    text = data['text']
    key = data.get('key', 'KEY')  # Provide a default key if none is provided
    result = vigenere_cipher(text, key, decode=True)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
