from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
from googletrans import LANGUAGES

app = Flask(__name__)

# List of Indian languages (for the select dropdown)
indian_languages = {
    'en': 'English',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'ta': 'Tamil',
    'te': 'Telugu',
    'mr': 'Marathi',
    'gu': 'Gujarati',
    'kn': 'Kannada',
    'ml': 'Malayalam',
    'or': 'Odia',
    'as': 'Assamese',
    'pa': 'Punjabi'
}

@app.route('/')
def index():
    return render_template('translator.html', languages=indian_languages)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    source_lang = data.get('source_lang', 'en')  # Default to English if not provided
    dest_lang = data.get('dest_lang', 'hi')  # Default to Hindi if not provided

    if not text:
        return jsonify({'error': 'Text to translate is required.'}), 400

    try:
        translated_text = GoogleTranslator(source=source_lang, target=dest_lang).translate(text)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
