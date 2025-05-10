from telethon import TelegramClient, sync
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

# Iterate over all dialogs (chats, groups, channels)
for dialog in client.iter_dialogs():
    chat_name = dialog.name or 'Unknown'
    chat_id = dialog.id

    # Replace special characters in chat names for safe filenames
    safe_chat_name = ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in chat_name)
    output_file = os.path.join(output_dir, f"{safe_chat_name}_{chat_id}.html")

    print(f"Exporting chat: {chat_name} (ID: {chat_id})")

    # Collect messages
    messages = []
    for message in client.iter_messages(chat_id, limit=None):  # Use limit=None for no limit
        if message.text:
            messages.append({
                'date': message.date,
                'sender_id': message.sender_id,
                'message': message.text
            })

    # Save messages to an HTML file
    if messages:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("<html><body>\n")
            f.write(f"<h1>Chat History: {chat_name}</h1>\n")
            for msg in messages:
                f.write(f"<p><strong>{msg['date']} - {msg['sender_id']}</strong>: {msg['message']}</p>\n")
            f.write("</body></html>")
        
        print(f"Chat history exported to {output_file}")
    else:
        print(f"No messages found in {chat_name}")

# Stop the client
client.disconnect()

print("All chat histories have been exported.")
