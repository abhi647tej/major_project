from flask import Flask, jsonify
from telethon import TelegramClient, events
import os
from bs4 import BeautifulSoup
import pandas as pd
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import json

# Initialize Flask app
app = Flask(__name__)

# Existing Telethon code setup...
api_id = 20966780
api_hash = '28399beb77594d96b266364a7e194eb6'
phone_number = '+918275889130'

client = TelegramClient('session', api_id, api_hash)
client.start(phone=phone_number)

output_dir = 'telegram_chat_exports'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

media_dir = os.path.join(output_dir, 'media')
if not os.path.exists(media_dir):
    os.makedirs(media_dir)

sia = SentimentIntensityAnalyzer()

# Store messages and user metadata in-memory for demo purposes
messages_data = []

@app.route('/api/messages', methods=['GET'])
def get_messages():
    # Serve the message data as JSON
    return jsonify(messages_data)

async def download_media(message, media_dir):
    if message.media:
        media_path = await message.download_media(file=media_dir)
        return media_path
    return None

def analyze_chat(message_text):
    # Sentiment analysis and drug-related content detection
    cleaned_message = re.sub(r'[^a-zA-Z\s]', '', message_text).lower()
    sentiment_score = sia.polarity_scores(message_text)['compound']
    drug_keywords = ['cocaine', 'marijuana', 'heroin', 'opioid', 'drug', 'narcotic', 'amphetamine']
    is_drug_related = any(keyword in cleaned_message for keyword in drug_keywords)
    return {"sentiment_score": sentiment_score, "is_drug_related": is_drug_related}

@client.on(events.NewMessage)
async def handler(event):
    message_text = event.message.text
    user = await client.get_entity(event.sender_id)
    
    user_data = {
        "user_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone_number": user.phone,
        "bio": user.bot,
        "status": str(user.status),
        "is_bot": user.bot,
        "language": user.lang_code,
        "message_text": message_text,
    }

    # Append sentiment and drug-related info to message
    analysis = analyze_chat(message_text)
    user_data.update(analysis)

    # Add message to messages_data
    messages_data.append(user_data)

# Start both Flask and Telethon
if __name__ == '__main__':
    client.loop.run_until_complete(client.connect())
    app.run(debug=True)



























