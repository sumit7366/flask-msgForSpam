from flask import Flask, render_template, request, jsonify
import re
from datetime import datetime

app = Flask(__name__)

# Load offensive words from file
def load_offensive_words():
    with open('/Users/sumitkumar/Desktop/ghi/flask_chat_app/offensive_words.txt', 'r') as file:
        return [word.strip().lower() for word in file.readlines()]

offensive_words = load_offensive_words()

# Chat history (in a real app, use a database)
chat_history = []

def contains_offensive_language(message):
    message_lower = message.lower()
    for word in offensive_words:
        # Using regex to match whole words only
        if re.search(r'\b' + re.escape(word) + r'\b', message_lower):
            return True
    return False

@app.route('/')
def home():
    return render_template('chat.html', chat_history=chat_history)

@app.route('/send_message', methods=['POST'])
def send_message():
    username = request.form.get('username', 'Anonymous')
    message = request.form.get('message', '').strip()
    
    if not message:
        return jsonify({'status': 'error', 'message': 'Message cannot be empty'})
    
    # Check for offensive language
    if contains_offensive_language(message):
        warning = "Your message contains offensive language and cannot be posted."
        return jsonify({'status': 'warning', 'message': warning})
    
    # Add message to chat history
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    chat_entry = {
        'username': username,
        'message': message,
        'timestamp': timestamp
    }
    chat_history.append(chat_entry)
    
    # In a real app, you would save to a database here
    
    return jsonify({
        'status': 'success',
        'username': username,
        'message': message,
        'timestamp': timestamp
    })

@app.route('/get_messages')
def get_messages():
    return jsonify({'messages': chat_history})

if __name__ == '__main__':
    app.run(debug=True)