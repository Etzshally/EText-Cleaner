from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result", methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        original_text = request.form.get('text')
        puncs = request.form.get('punc', 'off')
        capitalize = request.form.get('capitalize', 'off')
        lines = request.form.get('lines', 'off')
        if puncs == 'on':
            punctuations = '''!()-}{[]:;"\,<>./?@#$%^&*_`~'''
            tempStr = ""
            for char in original_text:
                if char not in punctuations:
                    tempStr += char
            original_text = tempStr
        if capitalize == 'on':
            original_text =  original_text.upper()
        if lines == 'on':
            tempStr = ""
            for char in original_text:
                if char != '\n' and char != '\r':
                    tempStr += char
            original_text = tempStr
    return render_template('result.html', original_text = original_text)


app.run(debug=True)