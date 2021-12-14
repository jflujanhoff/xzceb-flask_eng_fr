from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation.translator import english_to_french, french_to_english
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    # render_template('templates/index.html')
    return render_template('index.html')

if __name__ == "__main__": 
        app.run(host="0.0.0.0", port=8088)
