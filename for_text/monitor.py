# from telethon import TelegramClient, events
# import os
# from bs4 import BeautifulSoup
# import torch
# from transformers import BertTokenizer, BertForSequenceClassification

# # Replace with your credentials
# api_id = 20966780
# api_hash = '28399beb77594d96b266364a7e194eb6'
# phone_number = '+918275889130'

# # === Load your trained model and tokenizer ===
# model_path = "./final_chat_classifier"
# tokenizer = BertTokenizer.from_pretrained(model_path)
# model = BertForSequenceClassification.from_pretrained(model_path)
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model.to(device)
# model.eval()

# # === Telethon client setup ===
# client = TelegramClient('session_name', api_id, api_hash)
# client.start(phone=phone_number)

# # === Setup folders ===
# output_dir = 'telegram_chat_exports'
# media_dir = os.path.join(output_dir, 'media')
# os.makedirs(output_dir, exist_ok=True)
# os.makedirs(media_dir, exist_ok=True)

# # === Download media if present ===
# async def download_media(message, media_dir):
#     if message.media:
#         media_path = await message.download_media(file=media_dir)
#         return media_path
#     return None

# # === Predict combined chat label ===
# def predict_combined(chat_history):
#     combined_text = " ".join(chat_history)
#     encoding = tokenizer(
#         combined_text,
#         max_length=512,
#         padding="max_length",
#         truncation=True,
#         return_tensors="pt"
#     )
#     input_ids = encoding["input_ids"].to(device)
#     attention_mask = encoding["attention_mask"].to(device)

#     with torch.no_grad():
#         outputs = model(input_ids, attention_mask=attention_mask)
#         logits = outputs.logits
#         prediction = torch.argmax(logits, dim=1).item()

#     return "Suspicious" if prediction == 1 else "Normal"

# # === Analyze HTML chat file ===
# def analyze_chat_with_model(html_file):
#     with open(html_file, 'r', encoding='utf-8') as file:
#         soup = BeautifulSoup(file, 'html.parser')

#     chat_history = []
#     for message in soup.find_all('div', class_='message'):
#         text_tag = message.find('div', class_='text')
#         if text_tag:
#             chat_history.append(text_tag.text.strip())

#     if not chat_history:
#         print("No messages found for analysis.")
#         return

#     prediction = predict_combined(chat_history)
#     print(f"🕵️ Chat Analysis Result: {prediction}")

# # === New message handler for private chats ===
# @client.on(events.NewMessage)
# async def handler(event):
#     if not event.is_private:
#         return

#     try:
#         user = await client.get_entity(event.sender_id)
#         if user.bot:
#             return

#         user_id = user.id
#         username = user.username or ""
#         first_name = getattr(user, 'first_name', '') or ""
#         safe_name = ''.join(c if c.isalnum() else '_' for c in (username or first_name or 'unknown'))
#         output_file = os.path.join(output_dir, f"{safe_name}_{user_id}.html")

#         # First time fetch full history
#         if not os.path.exists(output_file):
#             print(f"Fetching full chat history with {username or first_name}...")
#             with open(output_file, 'w', encoding='utf-8') as f:
#                 f.write("<html><body>\n")
#                 async for msg in client.iter_messages(event.sender_id, reverse=True):
#                     f.write("<div class='message'>\n")
#                     f.write(f"<div class='from_name'>{msg.sender_id}</div>\n")
#                     if msg.media:
#                         media_path = await download_media(msg, media_dir)
#                         media_link = os.path.relpath(media_path, output_dir)
#                         f.write(f"<div class='text'>[Media: <a href='{media_link}'>{os.path.basename(media_path)}</a>]</div>\n")
#                     elif msg.text:
#                         f.write(f"<div class='text'>{msg.text}</div>\n")
#                     f.write("</div>\n")
#                 f.write("</body></html>\n")
#             print(f"Chat saved to {output_file}")

#         # Append latest message
#         with open(output_file, 'a', encoding='utf-8') as f:
#             f.write("<div class='message'>\n")
#             f.write(f"<div class='from_name'>{first_name or username}</div>\n")
#             if event.message.media:
#                 media_path = await download_media(event.message, media_dir)
#                 media_link = os.path.relpath(media_path, output_dir)
#                 f.write(f"<div class='text'>[Media: <a href='{media_link}'>{os.path.basename(media_path)}</a>]</div>\n")
#             else:
#                 f.write(f"<div class='text'>{event.message.text}</div>\n")
#             f.write("</div>\n")

#         print(f"New message appended to {output_file}")
#         analyze_chat_with_model(output_file)

#     except Exception as e:
#         print(f"⚠️ Error: {e}")

# # === Run bot ===
# print("🚀 Listening for new private messages...")
# client.run_until_disconnected()





# # for english model
# from telethon import TelegramClient, events
# import os
# from bs4 import BeautifulSoup
# import torch
# from transformers import BertTokenizer, BertForSequenceClassification

# # === Telegram API Credentials ===
# api_id = 20966780
# api_hash = '28399beb77594d96b266364a7e194eb6'
# phone_number = '+918275889130'

# # === Load Your Trained English-Only Model ===
# model_path = "./final_chat"
# tokenizer = BertTokenizer.from_pretrained(model_path)
# model = BertForSequenceClassification.from_pretrained(model_path)

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model.to(device)
# model.eval()

# # === Start Telegram Client ===
# client = TelegramClient('session_name', api_id, api_hash)
# client.start(phone=phone_number)

# # === Directories for HTML + Media ===
# output_dir = 'telegram_chat_exports'
# media_dir = os.path.join(output_dir, 'media')
# os.makedirs(output_dir, exist_ok=True)
# os.makedirs(media_dir, exist_ok=True)

# # === Download media helper ===
# async def download_media(message, media_dir):
#     if message.media:
#         media_path = await message.download_media(file=media_dir)
#         return media_path
#     return None

# # === Chat classification function ===
# def predict_combined(chat_history):
#     combined_text = " ".join(chat_history)
#     encoding = tokenizer(
#         combined_text,
#         max_length=512,
#         padding="max_length",
#         truncation=True,
#         return_tensors="pt"
#     )
#     input_ids = encoding["input_ids"].to(device)
#     attention_mask = encoding["attention_mask"].to(device)

#     with torch.no_grad():
#         outputs = model(input_ids, attention_mask=attention_mask)
#         logits = outputs.logits
#         prediction = torch.argmax(logits, dim=1).item()

#     return "Suspicious" if prediction == 1 else "Normal"

# # === Analyze saved HTML chat file ===
# def analyze_chat_with_model(html_file):
#     with open(html_file, 'r', encoding='utf-8') as file:
#         soup = BeautifulSoup(file, 'html.parser')

#     chat_history = []
#     for message in soup.find_all('div', class_='message'):
#         text_tag = message.find('div', class_='text')
#         if text_tag:
#             chat_history.append(text_tag.text.strip())

#     if not chat_history:
#         print("No messages found for analysis.")
#         return

#     prediction = predict_combined(chat_history)
#     print(f"🕵️ Chat Analysis Result: {prediction}")

# # === Event handler for private chats ===
# @client.on(events.NewMessage)
# async def handler(event):
#     if not event.is_private:
#         return

#     try:
#         user = await client.get_entity(event.sender_id)
#         if user.bot:
#             return

#         user_id = user.id
#         username = user.username or ""
#         first_name = getattr(user, 'first_name', '') or ""
#         safe_name = ''.join(c if c.isalnum() else '_' for c in (username or first_name or 'unknown'))
#         output_file = os.path.join(output_dir, f"{safe_name}_{user_id}.html")

#         # If chat not saved yet, export full history
#         if not os.path.exists(output_file):
#             print(f"Fetching full chat history with {username or first_name}...")
#             with open(output_file, 'w', encoding='utf-8') as f:
#                 f.write("<html><body>\n")
#                 async for msg in client.iter_messages(event.sender_id, reverse=True):
#                     f.write("<div class='message'>\n")
#                     f.write(f"<div class='from_name'>{msg.sender_id}</div>\n")
#                     if msg.media:
#                         media_path = await download_media(msg, media_dir)
#                         media_link = os.path.relpath(media_path, output_dir)
#                         f.write(f"<div class='text'>[Media: <a href='{media_link}'>{os.path.basename(media_path)}</a>]</div>\n")
#                     elif msg.text:
#                         f.write(f"<div class='text'>{msg.text}</div>\n")
#                     f.write("</div>\n")
#                 f.write("</body></html>\n")
#             print(f"Chat saved to {output_file}")

#         # Append new message
#         with open(output_file, 'a', encoding='utf-8') as f:
#             f.write("<div class='message'>\n")
#             f.write(f"<div class='from_name'>{first_name or username}</div>\n")
#             if event.message.media:
#                 media_path = await download_media(event.message, media_dir)
#                 media_link = os.path.relpath(media_path, output_dir)
#                 f.write(f"<div class='text'>[Media: <a href='{media_link}'>{os.path.basename(media_path)}</a>]</div>\n")
#             else:
#                 f.write(f"<div class='text'>{event.message.text}</div>\n")
#             f.write("</div>\n")

#         print(f"New message appended to {output_file}")
#         analyze_chat_with_model(output_file)

#     except Exception as e:
#         print(f"⚠️ Error: {e}")

# # === Start Listening ===
# print("🚀 Listening for new private messages...")
# client.run_until_disconnected()



# # logistic regression model
# from telethon import TelegramClient, events
# import os
# from bs4 import BeautifulSoup
# import re
# import joblib
# from nltk.sentiment import SentimentIntensityAnalyzer
# import pandas as pd

# # Load the trained model
# model = joblib.load("suspicious_chat_detector.pkl")

# # Function to preprocess text (same as you did during training)
# def preprocess_text(text):
#     text = text.lower()
#     text = re.sub(r"http\S+|www\S+|https\S+", '', text)
#     text = re.sub(r'[^\w\s]', '', text)
#     text = re.sub(r'\d+', '', text)
#     return text.strip()

# # Replace these with your actual values
# api_id = 20966780
# api_hash = '28399beb77594d96b266364a7e194eb6'
# phone_number = '+918275889130'

# # Initialize the client
# client = TelegramClient('session_name', api_id, api_hash)
# client.start(phone=phone_number)

# # Sentiment analysis tool
# sia = SentimentIntensityAnalyzer()

# # Function to detect suspicious content
# def is_suspicious(message):
#     # Preprocess the message
#     clean_message = preprocess_text(message)
    
#     # Predict using the trained model
#     prediction = model.predict([clean_message])
    
#     # Return whether the message is suspicious (assuming '1' means suspicious)
#     return prediction[0] == 1

# # Function to download media
# async def download_media(message, media_dir):
#     if message.media:
#         media_path = await message.download_media(file=media_dir)
#         return media_path
#     return None

# # Event listener for new messages (One-to-One Chats Only)
# @client.on(events.NewMessage)
# async def handler(event):
#     # Filter: Process only one-to-one chats
#     if not event.is_private:  # Exclude groups and channels
#         return

#     try:
#         user = await client.get_entity(event.sender_id)

#         # Exclude bots
#         if user.bot:
#             return

#         # Fetch user metadata
#         user_id = user.id
#         username = user.username
#         first_name = getattr(user, 'first_name', 'No first name')

#         # Generate a safe filename for the user
#         safe_user_name = ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in (username or first_name or 'Unknown'))
#         output_file = os.path.join('telegram_chat_exports', f"{safe_user_name}_{user_id}.html")

#         # Download media if present
#         media_path = await download_media(event.message, 'telegram_chat_exports/media')

#         # Append the new message to the HTML file
#         with open(output_file, 'a', encoding='utf-8') as f:
#             if os.stat(output_file).st_size == 0:  # If file is empty, start a basic HTML structure
#                 f.write("<html><body>\n")
#             f.write(f"<div class='message'>\n")
#             f.write(f"  <div class='from_name'>{first_name or username}</div>\n")
#             if media_path:
#                 media_link = os.path.relpath(media_path, 'telegram_chat_exports')  # Relative path for HTML
#                 f.write(f"  <div class='text'>[Media: <a href='{media_link}'>{os.path.basename(media_path)}</a>]</div>\n")
#             else:
#                 f.write(f"  <div class='text'>{event.message.text}</div>\n")
#             f.write("</div>\n")
#             f.write("</body></html>\n")

#         print(f"Message (and media, if any) appended to {output_file}")

#         # Check if the message is suspicious
#         if is_suspicious(event.message.text):
#             print("⚠️ Suspicious message detected!")
#         else:
#             print("✅ Normal message.")

#     except Exception as e:
#         print(f"Error processing message: {e}")

# # Start the client and keep it running
# print("Listening for new messages (One-to-One Chats Only)...")
# client.run_until_disconnected()





# # random_forest model
# from telethon import TelegramClient, events
# import os
# import re
# import joblib
# from bs4 import BeautifulSoup
# import pandas as pd
# from nltk.sentiment import SentimentIntensityAnalyzer
# import nltk

# nltk.download('vader_lexicon')

# # Load the trained Random Forest model
# model = joblib.load("suspicious_chat_rf_model.pkl")

# # Text preprocessing (same as training)
# def preprocess_text(text):
#     text = text.lower()
#     text = re.sub(r"http\S+|www\S+|https\S+", '', text)
#     text = re.sub(r'[^\w\s]', '', text)
#     text = re.sub(r'\d+', '', text)
#     return text.strip()

# # Function to check if message is suspicious
# def is_suspicious(message):
#     clean = preprocess_text(message)
#     return model.predict([clean])[0] == 1

# # Telegram credentials
# api_id = 20966780
# api_hash = '28399beb77594d96b266364a7e194eb6'
# phone_number = '+918275889130'

# client = TelegramClient('session_name', api_id, api_hash)
# client.start(phone=phone_number)

# sia = SentimentIntensityAnalyzer()

# # Create directories
# output_dir = 'telegram_chat_exports'
# media_dir = os.path.join(output_dir, 'media')
# os.makedirs(media_dir, exist_ok=True)

# async def download_media(message, media_dir):
#     if message.media:
#         media_path = await message.download_media(file=media_dir)
#         return media_path
#     return None

# @client.on(events.NewMessage)
# async def handler(event):
#     if not event.is_private:
#         return

#     try:
#         user = await client.get_entity(event.sender_id)
#         if user.bot:
#             return

#         user_id = user.id
#         username = user.username
#         first_name = getattr(user, 'first_name', 'Unknown')
#         safe_name = ''.join(c if c.isalnum() else '_' for c in (username or first_name))
#         html_file = os.path.join(output_dir, f"{safe_name}_{user_id}.html")

#         media_path = await download_media(event.message, media_dir)

#         with open(html_file, 'a', encoding='utf-8') as f:
#             if os.stat(html_file).st_size == 0:
#                 f.write("<html><body>\n")
#             f.write(f"<div class='message'>\n")
#             f.write(f"  <div class='from_name'>{first_name}</div>\n")
#             if media_path:
#                 media_link = os.path.relpath(media_path, output_dir)
#                 f.write(f"  <div class='text'>[Media: <a href='{media_link}'>{os.path.basename(media_path)}</a>]</div>\n")
#             else:
#                 f.write(f"  <div class='text'>{event.message.text}</div>\n")
#             f.write("</div>\n")
#             f.write("</body></html>\n")

#         print(f"Message saved to {html_file}")

#         if is_suspicious(event.message.text):
#             print("⚠️ Suspicious message detected!")
#         else:
#             print("✅ Normal message.")

#     except Exception as e:
#         print(f"Error: {e}")

# print("🔍 Listening for new messages...")
# client.run_until_disconnected()



# random forest model with telegram metadata
# from telethon import TelegramClient, events
# import os
# import re
# import joblib
# from bs4 import BeautifulSoup
# import pandas as pd
# from nltk.sentiment import SentimentIntensityAnalyzer
# import nltk


# # Download VADER
# nltk.download('vader_lexicon')

# # Load the trained Random Forest model
# model = joblib.load("suspicious_chat_rf_model.pkl")

# # Text preprocessing for model
# def preprocess_text(text):
#     text = text.lower()
#     text = re.sub(r"http\S+|www\S+|https\S+", '', text)
#     text = re.sub(r'[^\w\s]', '', text)
#     text = re.sub(r'\d+', '', text)
#     return text.strip()

# # Check if message is suspicious
# def is_suspicious(message):
#     clean = preprocess_text(message)
#     return model.predict([clean])[0] == 1

# # Telegram API credentials
# api_id = 20966780
# api_hash = '28399beb77594d96b266364a7e194eb6'
# phone_number = '+918275889130'

# client = TelegramClient('session_name', api_id, api_hash)
# client.start(phone=phone_number)

# # Sentiment analyzer (optional if needed)
# sia = SentimentIntensityAnalyzer()

# # Directories
# output_dir = 'telegram_chat_exports'
# media_dir = os.path.join(output_dir, 'media')
# os.makedirs(media_dir, exist_ok=True)

# # Download media
# async def download_media(message, media_dir):
#     if message.media:
#         media_path = await message.download_media(file=media_dir)
#         return media_path
#     return None

# @client.on(events.NewMessage)
# async def handler(event):
#     if not event.is_private:
#         return

#     try:
#         user = await client.get_entity(event.sender_id)
#         if user.bot:
#             return

#         # Extract user metadata
#         user_id = user.id
#         username = user.username
#         first_name = getattr(user, 'first_name', 'Unknown')
#         last_name = getattr(user, 'last_name', 'Unknown')
#         phone = getattr(user, 'phone', 'No phone number')
#         bio = getattr(user, 'bio', 'No bio available')

#         # Print user metadata
#         print(f"User ID: {user_id}")
#         print(f"Username: {username}")
#         print(f"First Name: {first_name}")
#         print(f"Last Name: {last_name}")
#         print(f"Phone Number: {phone}")
#         print(f"Bio: {bio}")

#         # Safe filename
#         safe_name = ''.join(c if c.isalnum() else '_' for c in (username or first_name))
#         html_file = os.path.join(output_dir, f"{safe_name}_{user_id}.html")

#         # Download media if present
#         media_path = await download_media(event.message, media_dir)

#         # Write message to HTML
#         with open(html_file, 'a', encoding='utf-8') as f:
#             if os.stat(html_file).st_size == 0:
#                 f.write("<html><body>\n")
#             f.write(f"<div class='message'>\n")
#             f.write(f"  <div class='from_name'>{first_name}</div>\n")
#             if media_path:
#                 media_link = os.path.relpath(media_path, output_dir)
#                 f.write(f"  <div class='text'>[Media: <a href='{media_link}'>{os.path.basename(media_path)}</a>]</div>\n")
#             else:
#                 f.write(f"  <div class='text'>{event.message.text}</div>\n")
#             f.write("</div>\n")
#             f.write("</body></html>\n")

#         print(f"Message saved to {html_file}")

#         # Check for suspicious content using Random Forest
#         if is_suspicious(event.message.text):
#             print("⚠️ Suspicious message detected!")
#         else:
#             print("✅ Normal message.")

#     except Exception as e:
#         print(f"Error: {e}")

# print("🔍 Listening for new messages (One-to-One Chats Only)...")
# client.run_until_disconnected()



# from telethon.sync import TelegramClient, events
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer
# import json
# import os
# from datetime import datetime

# # NLTK setup
# nltk.download('vader_lexicon')
# sia = SentimentIntensityAnalyzer()

# # Telegram credentials
# api_id = 20966780
# api_hash = '28399beb77594d96b266364a7e194eb6'
# phone_number = '+918275889130'

# client = TelegramClient('anon', api_id, api_hash)

# # Suspicious keywords
# suspicious_keywords = [
#     "drug", "weed", "marijuana", "cocaine", "lsd", "heroin",
#     "meth", "ecstasy", "mdma", "opium", "hash", "ganja", "acid",
#     "buy drugs", "sell drugs", "narcotics", "illegal substances"
# ]

# def is_suspicious(message):
#     message_lower = message.lower()
#     if any(keyword in message_lower for keyword in suspicious_keywords):
#         return True
#     sentiment_score = sia.polarity_scores(message)['compound']
#     return sentiment_score < -0.5

# def save_suspicious_user(data):
#     file_path = 'suspicious_chats.json'
#     existing_data = []

#     if os.path.exists(file_path):
#         with open(file_path, 'r') as f:
#             try:
#                 existing_data = json.load(f)
#             except json.JSONDecodeError:
#                 pass

#     existing_data.append(data)

#     with open(file_path, 'w') as f:
#         json.dump(existing_data, f, indent=4)

# @client.on(events.NewMessage)
# async def handler(event):
#     if event.is_private and event.sender_id:
#         sender = await event.get_sender()
#         message = event.message.text

#         user_data = {
#             "userId": str(sender.id),
#             "username": f"@{sender.username}" if sender.username else "N/A",
#             "firstName": sender.first_name or "N/A",
#             "lastName": sender.last_name or "N/A",
#             "phone": sender.phone or "N/A",
#             "bio": sender.bot or "No bio available",
#             "status": "Active",
#             "isBot": "Yes" if sender.bot else "No",
#             "language": "en",
#             "message": message,
#             "chatHistory": [],  # Extend this later if needed
#             "messageType": "Suspicious" if is_suspicious(message) else "Normal"
#         }

#         print(f"{'⚠️ Suspicious' if user_data['messageType']=='Suspicious' else '✅ Normal'} message: {message}")
#         save_suspicious_user(user_data)

# with client:
#     print("🚀 Telegram monitor is running...")
#     client.run_until_disconnected()




from telethon.sync import TelegramClient, events
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import json
import os
import requests
from datetime import datetime

# NLTK setup
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Telegram credentials
api_id = 20966780
api_hash = '28399beb77594d96b266364a7e194eb6'
phone_number = '+918275889130'

client = TelegramClient('combined_session', api_id, api_hash)
client.start(phone=phone_number)

# Suspicious keywords
suspicious_keywords = [
    "drug", "weed", "marijuana", "cocaine", "lsd", "heroin",
    "meth", "ecstasy", "mdma", "opium", "hash", "ganja", "acid",
    "buy drugs", "sell drugs", "narcotics", "illegal substances","blaze","goodies","white powder","puff","bhang"
]

def is_suspicious(message):
    message_lower = message.lower()
    if any(keyword in message_lower for keyword in suspicious_keywords):
        return True
    sentiment_score = sia.polarity_scores(message)['compound']
    return sentiment_score < -0.5

def save_suspicious_user(data):
    file_path = 'suspicious_chats.json'
    existing_data = []

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                pass

    existing_data.append(data)

    with open(file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)

# Create directories
output_dir = 'telegram_chat_exports'
media_dir = os.path.join(output_dir, 'media')
os.makedirs(media_dir, exist_ok=True)

# Image classification with YOLO model
def classify_image_with_yolo(image_path):
    url = "http://localhost:5000/predict"
    with open(image_path, "rb") as img_file:
        files = {"image": img_file}
        try:
            response = requests.post(url, files=files)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"YOLO API error: {response.text}"}
        except Exception as e:
            return {"error": str(e)}

@client.on(events.NewMessage)
async def handler(event):
    if event.is_private and event.sender_id:
        sender = await event.get_sender()

        if event.message.text:
            message = event.message.text
            user_data = {
                "userId": str(sender.id),
                "username": f"@{sender.username}" if sender.username else "N/A",
                "firstName": sender.first_name or "N/A",
                "lastName": sender.last_name or "N/A",
                "phone": sender.phone or "N/A",
                "bio": sender.bot or "No bio available",
                "status": "Active",
                "isBot": "Yes" if sender.bot else "No",
                "language": "en",
                "message": message,
                "chatHistory": [],
                "messageType": "Suspicious" if is_suspicious(message) else "Normal"
            }

            print(f"{'⚠️ Suspicious' if user_data['messageType']=='Suspicious' else '✅ Normal'} message: {message}")
            save_suspicious_user(user_data)

        elif event.message.media:
            try:
                if sender.bot:
                    return

                media_path = await event.message.download_media(file=media_dir)
                print(f"📥 Media saved at: {media_path}")

                result = classify_image_with_yolo(media_path)
                yolo_class = result.get("class", "")
                confidence = result.get("confidence", 0)

                is_suspicious_image = yolo_class.lower() != "not a drug" and confidence >= 0.7

                print("\n🧪 YOLO Result:")
                print(f"  Class     : {yolo_class}")
                print(f"  Confidence: {confidence}")
                print(f"  🔍 Image Status: {'⚠️ Suspicious' if is_suspicious_image else '✅ Not Suspicious'}")

                image_data = {
                    "userId": str(sender.id),
                    "username": f"@{sender.username}" if sender.username else "N/A",
                    "firstName": getattr(sender, 'first_name', 'N/A'),
                    "lastName": getattr(sender, 'last_name', 'N/A'),
                    "phone": getattr(sender, 'phone', 'N/A'),
                    "bio": "N/A",
                    "status": "Active",
                    "isBot": "No",
                    "language": "en",
                    "message": f"[Image] {os.path.basename(media_path)}",
                    "chatHistory": [],
                    "messageType": "Suspicious" if is_suspicious_image else "Normal"
                }
                save_suspicious_user(image_data)

            except Exception as e:
                print(f"⚠️ Error processing media: {e}")

print("🚀 Combined Telegram monitor (text + image) is running...")
client.run_until_disconnected()

