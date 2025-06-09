from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Khởi tạo các thuật toán mã hóa
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()

# Các route cho trang chủ
@app.route("/")
def home():
    return render_template('index.html')

# Các route cho Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return render_template('caesar.html', outputCipherText=encrypted_text, inputPlainText=text, inputKeyPlain=key)

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return render_template('caesar.html', outputDecryptedText=decrypted_text, inputCipherText=text, inputKeyCipher=key)

# Các route cho Vigenere Cipher
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return render_template('vigenere.html', outputCipherText=encrypted_text, inputPlainText=plain_text, inputKeyPlain=key)

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return render_template('vigenere.html', outputDecryptedText=decrypted_text, inputCipherText=cipher_text, inputKeyCipher=key)

# Các route cho Rail Fence Cipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return render_template('railfence.html', outputCipherText=encrypted_text, inputPlainText=plain_text, inputKeyPlain=key)

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return render_template('railfence.html', outputDecryptedText=decrypted_text, inputCipherText=cipher_text, inputKeyCipher=key)

# Các route cho Playfair Cipher
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    # You might want to display the matrix as well, but for now, just the text
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return render_template('playfair.html', outputCipherText=encrypted_text, inputPlainText=plain_text, inputKeyPlain=key)

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return render_template('playfair.html', outputDecryptedText=decrypted_text, inputCipherText=cipher_text, inputKeyCipher=key)

# Các route cho Transposition Cipher
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return render_template('transposition.html', outputCipherText=encrypted_text, inputPlainText=plain_text, inputKeyPlain=key)

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return render_template('transposition.html', outputDecryptedText=decrypted_text, inputCipherText=cipher_text, inputKeyCipher=key)

# Hàm main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)