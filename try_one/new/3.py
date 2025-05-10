from bs4 import BeautifulSoup
import pandas as pd
import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Load the HTML file
with open("C:\\Users\\RUSHIKESH\\Downloads\\Telegram Desktop\\ChatExport_2024-11-07 (1)\\messages.html", 'r', encoding='utf-8') as file:
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

# Preprocessing: Lowercase conversion and removing non-alphabetic characters
df['cleaned_message'] = df['message'].apply(lambda x: re.sub(r'[^a-zA-Z\\s]', '', x).lower())

# Initialize VADER SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Apply sentiment analysis to each message
df['sentiment_score'] = df['message'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Display sentiment scores for all messages
print("Sentiment scores for all messages:")
print(df[['user', 'message', 'sentiment_score']])

# Detecting drug-related content
drug_keywords = ['cocaine', 'marijuana', 'heroin', 'opioid', 'drug', 'narcotic', 'amphetamine']

df['is_drug_related'] = df['cleaned_message'].apply(
    lambda x: any(keyword in x for keyword in drug_keywords)
)

# Check if any message is drug-related and print the result
if df['is_drug_related'].any():
    print("Suspicious: The chat contains messages that may be related to illicit drugs.")
else:
    print("Normal chat: No suspicious messages detected.")

# Visualize the sentiment distribution
sns.histplot(df['sentiment_score'], kde=True)
plt.title('Sentiment Distribution of Messages')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()
