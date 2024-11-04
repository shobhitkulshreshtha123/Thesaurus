import json
import difflib
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
my_data_file = json.load(open("data.json"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    user_input = data.get('word', '').lower()
    
    if user_input in my_data_file:
        definitions = my_data_file[user_input]
        return jsonify({"word": user_input, "definitions": definitions})
    else:
        similar_words = difflib.get_close_matches(user_input, my_data_file.keys(), n=3)
        if similar_words:
            return jsonify({"similar_words": similar_words})
        else:
            return jsonify({"error": "No match found"})

if __name__ == '__main__':
    app.run(debug=True)
