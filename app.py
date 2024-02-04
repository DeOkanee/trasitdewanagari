from flask import Flask, render_template, request
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ubah', methods=['POST'])
def ubah():
    kalimat_input = request.form['kalimat_input']
    kalimat_dewanagari = transliterate(kalimat_input, sanscript.ITRANS, sanscript.DEVANAGARI)
    return render_template('index.html', kalimat_dewanagari=kalimat_dewanagari)

if __name__ == '__main__':
    app.run(debug=True)
