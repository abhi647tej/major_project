# From telethon import TelegramClient, events, sync from telethon.sessions 
# import StringSession
# api_id = 1209667
# api_hash= '28399beb77594d96b266364a7e194eb6'
# string = input('session code or press enter: ")
# with TelegramClient(StringSession(string), api_id, api_hash) as client:
# print('------------')
# print("this is session code ")
# print('- -\n')
# print(client.session.save())
# print(- -)
# print("this is otp code ")
# print('- -\n')
# async def main():

from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession

api_id = 1209667
api_hash = '28399beb77594d96b266364a7e194eb6'

# Corrected the string input line
string = input('session code or press enter: ')

with TelegramClient(StringSession(string), api_id, api_hash) as client:
    print('------------')
    print("This is the session code")
    print('------------\n')
    print(client.session.save())
    print('------------')
    print("Listening for OTP or any incoming messages")
    print('------------\n')

    @client.on(events.NewMessage)
    async def handler(event):
        print(f"New message received: {event.text}")

    # Run the client until disconnected
    client.run_until_disconnected()
