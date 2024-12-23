from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Simple data storage (replace with database later)
DATA_FILE = 'data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            'music': {'user1': {}, 'user2': {}},
            'dinner': {'selected': ''},
            'moods': {'user1': {}, 'user2': {}}
        }

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/update/music', methods=['POST'])
def update_music():
    data = load_data()
    user = request.form.get('user')
    song = request.form.get('song')
    artist = request.form.get('artist')
    
    data['music'][user] = {
        'song': song,
        'artist': artist,
        'timestamp': datetime.now().isoformat()
    }
    save_data(data)
    return jsonify({'status': 'success'})

@app.route('/update/mood', methods=['POST'])
def update_mood():
    data = load_data()
    user = request.form.get('user')
    mood = request.form.get('mood')
    
    data['moods'][user] = {
        'mood': mood,
        'timestamp': datetime.now().isoformat()
    }
    save_data(data)
    return jsonify({'status': 'success'})

@app.route('/update/dinner', methods=['POST'])
def update_dinner():
    data = load_data()
    dinner = request.form.get('dinner')
    data['dinner']['selected'] = dinner
    save_data(data)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True) 