# from flask import Flask, jsonify
# from flask_cors import CORS
# import json
# import os

# app = Flask(__name__)
# CORS(app)

# @app.route('/api/suspicious-chats', methods=['GET'])
# def get_suspicious_chats():
#     try:
#         file_path = 'suspicious_chats.json'
#         if not os.path.exists(file_path):
#             return jsonify([])

#         with open(file_path, 'r') as f:
#             data = json.load(f)
#         return jsonify(data)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify
from flask_cors import CORS 
import json
import os
from flask import send_from_directory

app = Flask(__name__)
CORS(app)

@app.route('/api/suspicious-chats', methods=['GET'])
def get_chats():
    file_path = 'suspicious_chats.json'
    if not os.path.exists(file_path):
        return jsonify([])
    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return jsonify([])
    return jsonify(data)

@app.route('/api/chat-stats')
def get_stats():
    with open('suspicious_chats.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_messages = len(data)
    suspicious_messages = sum(1 for chat in data if chat.get("messageType") == "Suspicious")
    normal_messages = sum(1 for chat in data if chat.get("messageType") == "Normal")

    suspicious_users = set()
    for chat in data:
        if chat.get("messageType") == "Suspicious":
            suspicious_users.add(chat.get("userId"))

    total_suspicious_users = len(suspicious_users)

    return jsonify({
        "total_messages": total_messages,
        "suspicious_messages": suspicious_messages,
        "normal_messages": normal_messages,
        "suspicious_users": total_suspicious_users
    })

@app.route('/telegram_chat_exports/media/<filename>')
def serve_media(filename):
    return send_from_directory('telegram_chat_exports/media', filename)

if __name__ == '__main__':
    app.run(debug=True,port=5001)




