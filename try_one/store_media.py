from telethon import TelegramClient, events
import os
from bs4 import BeautifulSoup
import pandas as pd
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Replace these with your actual values
api_id = 20966780
api_hash = '28399beb77594d96b266364a7e194eb6'
phone_number = '+918275889130'

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)
client.start(phone=phone_number)

# Create a directory to store chat exports if not already present
output_dir = 'telegram_chat_exports'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a directory for media files
media_dir = os.path.join(output_dir, 'media')
if not os.path.exists(media_dir):
    os.makedirs(media_dir)

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to download media and return the file path
async def download_media(message, media_dir):
    if message.media:
        media_path = await message.download_media(file=media_dir)
        return media_path
    return None

# Function to perform sentiment analysis on the entire chat history
def analyze_chat(html_file):
    # Load the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Extract all messages
    messages = []
    for message in soup.find_all('div', class_='message'):
        user_tag = message.find('div', class_='from_name')
        text_tag = message.find('div', class_='text')

        if text_tag:
            user_text = user_tag.text.strip() if user_tag else 'Unknown'
            message_text = text_tag.text.strip()
            messages.append({'user': user_text, 'message': message_text})

    # Create a DataFrame
    df = pd.DataFrame(messages)

    if df.empty:
        print("No messages found for analysis.")
        return

    # Preprocessing: Lowercase conversion and removing non-alphabetic characters
    df['cleaned_message'] = df['message'].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x).lower())

    # Apply sentiment analysis to each message
    df['sentiment_score'] = df['message'].apply(lambda x: sia.polarity_scores(x)['compound'])

    # Detecting drug-related content
    drug_keywords = ['cocaine', 'marijuana', 'heroin', 'opioid', 'drug', 'narcotic', 'amphetamine']
    df['is_drug_related'] = df['cleaned_message'].apply(
        lambda x: any(keyword in x for keyword in drug_keywords)
    )

    # Check if any message is drug-related
    if df['is_drug_related'].any():
        print("Suspicious: The chat contains messages that may be related to illicit drugs.")
    else:
        print("Normal chat: No suspicious messages detected.")

    # Visualize the sentiment distribution
    sns.histplot(df['sentiment_score'], kde=True)
    plt.title(f'Sentiment Distribution of Messages in {os.path.basename(html_file)}')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.show()

# Event listener for new messages
@client.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()
    chat_name = chat.title if hasattr(chat, 'title') else (chat.first_name or chat.username or 'Unknown')
    chat_id = event.chat_id

    # Replace special characters in chat names for safe filenames
    safe_chat_name = ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in chat_name)
    output_file = os.path.join(output_dir, f"{safe_chat_name}_{chat_id}.html")

    # Download media if present
    media_path = await download_media(event.message, media_dir)

    # Append the new message to the HTML file
    with open(output_file, 'a', encoding='utf-8') as f:
        if os.stat(output_file).st_size == 0:  # If file is empty, start a basic HTML structure
            f.write("<html><body>\n")
        f.write(f"<div class='message'>\n")
        f.write(f"  <div class='from_name'>{event.message.sender_id}</div>\n")
        if media_path:
            media_link = os.path.relpath(media_path, output_dir)  # Relative path for HTML
            f.write(f"  <div class='text'>[Media: <a href='{media_link}'>{os.path.basename(media_path)}</a>]</div>\n")
        else:
            f.write(f"  <div class='text'>{event.message.text}</div>\n")
        f.write("</div>\n")
        f.write("</body></html>\n")

    print(f"Message (and media, if any) appended to {output_file}")

    # Perform analysis on the updated chat file
    analyze_chat(output_file)

# Start the client and keep it running
print("Listening for new messages...")
client.run_until_disconnected()
