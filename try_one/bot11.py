import re
from collections import deque
from textblob import TextBlob
from telethon import TelegramClient, events

# Telegram API credentials
API_ID = 20966780
API_HASH = '28399beb77594d96b266364a7e194eb6'

# Initialize Telegram client
client = TelegramClient('session_name', API_ID, API_HASH)

# 1. Drug-related keywords, slang, and abbreviations
DRUG_KEYWORDS = [
    "cocaine", "heroin", "meth", "weed", "marijuana", "ecstasy", 
    "lsd", "fentanyl", "oxycodone", "molly", "shrooms"
]

# 2. Common slang/codes for drugs
DRUG_CODES = [
    "snow", "blow", "ice", "green", "xan", "bars", "beans", 
    "kush", "420", "plug", "zip", "eight ball", "gram", "ounce", "pill"
]

# 3. Patterns for quantities and transactions
TRANSACTION_PATTERNS = [
    r"\b\d+\s?(grams?|oz|ounces?|pills?|tabs?|lbs?)\b",  # Quantity
    r"\b\d+\s?\$(\s?|per)?\s?(gram|ounce|pill)?\b",      # Price or payment
    r"cash\s?(app|transfer)?|venmo|paypal"               # Payment methods
]

# 4. Store recent messages (to detect context over time)
recent_messages = deque(maxlen=10)  # Store last 10 messages for context

# 5. Preprocessing function
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    return text

# 6. Function to check for drug-related keywords
def contains_drug_keywords(text):
    for word in DRUG_KEYWORDS + DRUG_CODES:
        if word in text:
            return True, f"Drug term detected: {word}"
    return False, None

# 7. Function to detect patterns of quantities or payments
def contains_transaction_patterns(text):
    for pattern in TRANSACTION_PATTERNS:
        if re.search(pattern, text):
            return True, "Transaction pattern detected"
    return False, None

# 8. Sentiment Analysis to detect urgency or aggression
def is_aggressive_message(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity  # Range: -1 (negative) to +1 (positive)
    return sentiment < -0.4  # Consider suspicious if polarity is too negative

# 9. Contextual Analysis: Monitor chats over time
def monitor_context(new_message):
    recent_messages.append(new_message)  # Add the new message to the queue

    # Check if multiple suspicious terms appear across recent messages
    context_string = " ".join(recent_messages)
    contains_drug, reason = contains_drug_keywords(context_string)
    if contains_drug:
        return True, f"Suspicious context detected: {reason}"
    return False, None

# 10. Main detection function
def detect_drug_trafficking(message):
    try:
        message = preprocess_text(message)
        detection_count = 0  # Initialize count of detected criteria
        reasons = []         # List to accumulate reasons for detection

        # 1. Check for drug-related keywords and slang
        keyword_found, reason = contains_drug_keywords(message)
        if keyword_found:
            detection_count += 1
            reasons.append(reason)

        # 2. Check for transaction-related patterns
        transaction_found, reason = contains_transaction_patterns(message)
        if transaction_found:
            detection_count += 1
            reasons.append(reason)

        # 3. Check for aggressive or urgent sentiment
        if is_aggressive_message(message):
            detection_count += 1
            reasons.append("Aggressive or urgent tone detected")

        # 4. Monitor context for suspicious behavior across messages
        context_flagged, reason = monitor_context(message)
        if context_flagged:
            detection_count += 1
            reasons.append(reason)

        # Flag as suspicious if 3 or more criteria are met
        if detection_count >= 3:
            return True, "; ".join(reasons)
        else:
            return False, "Message seems safe"
    except Exception as e:
        print(f"Error in detect_drug_trafficking: {e}")
        return False, "Error in processing message"

# 11. Function to analyze full chat history
async def analyze_full_chat_history(chat_id):
    print("Analyzing chat history...")
    try:
        message_count = 0  # Counter to keep track of number of messages processed
        async for message in client.iter_messages(chat_id):
            message_count += 1
            message_text = message.message
            if message_text is None:
                continue  # Skip empty messages
            
            # Periodic log to check progress
            if message_count % 100 == 0:
                print(f"Processed {message_count} messages...")

            # Run the detection algorithm on the message
            suspicious, reason = detect_drug_trafficking(message_text)
            
            if suspicious:
                alert_message = (
                    f"⚠️ Suspicious message detected:\n\n"
                    f"User: {message.sender_id}\n"
                    f"Message: '{message_text}'\n"
                    f"Reason: {reason}"
                )
                # Log the suspicious message to the console
                print(alert_message)
    except Exception as e:
        print(f"Error in analyze_full_chat_history: {e}")

# 12. Telegram event handler to start chat history analysis
@client.on(events.NewMessage(pattern='/analyze'))
async def start_analysis(event):
    chat_id = event.chat_id
    await analyze_full_chat_history(chat_id)

# 13. Start the Telegram client
client.start()
print("Bot is running. Send /analyze in a chat to start analysis of chat history...")
client.run_until_disconnected()
