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
from telethon import TelegramClient, events
import os
import re
import joblib
from bs4 import BeautifulSoup
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER
nltk.download('vader_lexicon')

# Load the trained Random Forest model
model = joblib.load("suspicious_chat_rf_model.pkl")

# Text preprocessing for model
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    return text.strip()

# Check if message is suspicious
def is_suspicious(message):
    clean = preprocess_text(message)
    return model.predict([clean])[0] == 1

# Telegram API credentials
api_id = 20966780
api_hash = '28399beb77594d96b266364a7e194eb6'
phone_number = '+918275889130'

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone=phone_number)

# Sentiment analyzer (optional if needed)
sia = SentimentIntensityAnalyzer()

# Directories
output_dir = 'telegram_chat_exports'
media_dir = os.path.join(output_dir, 'media')
os.makedirs(media_dir, exist_ok=True)

# Download media
async def download_media(message, media_dir):
    if message.media:
        media_path = await message.download_media(file=media_dir)
        return media_path
    return None

@client.on(events.NewMessage)
async def handler(event):
    if not event.is_private:
        return

    try:
        user = await client.get_entity(event.sender_id)
        if user.bot:
            return

        # Extract user metadata
        user_id = user.id
        username = user.username
        first_name = getattr(user, 'first_name', 'Unknown')
        last_name = getattr(user, 'last_name', 'Unknown')
        phone = getattr(user, 'phone', 'No phone number')
        bio = getattr(user, 'bio', 'No bio available')

        # Print user metadata
        print(f"User ID: {user_id}")
        print(f"Username: {username}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Phone Number: {phone}")
        print(f"Bio: {bio}")

        # Safe filename
        safe_name = ''.join(c if c.isalnum() else '_' for c in (username or first_name))
        html_file = os.path.join(output_dir, f"{safe_name}_{user_id}.html")

        # Download media if present
        media_path = await download_media(event.message, media_dir)

        # Write message to HTML
        with open(html_file, 'a', encoding='utf-8') as f:
            if os.stat(html_file).st_size == 0:
                f.write("<html><body>\n")
            f.write(f"<div class='message'>\n")
            f.write(f"  <div class='from_name'>{first_name}</div>\n")
            if media_path:
                media_link = os.path.relpath(media_path, output_dir)
                f.write(f"  <div class='text'>[Media: <a href='{media_link}'>{os.path.basename(media_path)}</a>]</div>\n")
            else:
                f.write(f"  <div class='text'>{event.message.text}</div>\n")
            f.write("</div>\n")
            f.write("</body></html>\n")

        print(f"Message saved to {html_file}")

        # Check for suspicious content using Random Forest
        if is_suspicious(event.message.text):
            print("⚠️ Suspicious message detected!")
        else:
            print("✅ Normal message.")

    except Exception as e:
        print(f"Error: {e}")

print("🔍 Listening for new messages (One-to-One Chats Only)...")
client.run_until_disconnected()
