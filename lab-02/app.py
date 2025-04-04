from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher

app= Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def ceasar_encrypt():
    text = request.form['inputPlaintext']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text,key)
    return f"text: {text} <br/> key: {key} <br/> encrypted_text: {encrypted_text}"
    
@app.route("/decrypt", methods=['POST'])
def ceasar_decrypt():
    text = request.form['inputCiphertext']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text,key)
    return f"text: {text} <br/> key: {key} <br/> decrypted_text: {decrypted_text}"

#main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)