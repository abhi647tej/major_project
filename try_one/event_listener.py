from telethon import TelegramClient, events
import os

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

# Event listener for new messages
@client.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()
    # Use title for groups/channels, and first_name/username for private chats
    if hasattr(chat, 'title') and chat.title:
        chat_name = chat.title
    else:
        chat_name = chat.first_name or chat.username or 'Unknown'
        
    chat_id = event.chat_id

    # Replace special characters in chat names for safe filenames
    safe_chat_name = ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in chat_name)
    output_file = os.path.join(output_dir, f"{safe_chat_name}_{chat_id}.html")

    # Export the new message
    print(f"New message received in chat: {chat_name} (ID: {chat_id})")
    
    message = {
        'date': event.message.date,
        'sender_id': event.message.sender_id,
        'message': event.message.text
    }

    # Append the message to the HTML file
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write("<html><body>\n")
        f.write(f"<p><strong>{message['date']} - {message['sender_id']}</strong>: {message['message']}</p>\n")
        f.write("</body></html>")

    print(f"Message appended to {output_file}")

# Start the client and keep it running
print("Listening for new messages...")
client.run_until_disconnected()
