# major_project
I was working on a Telegram monitoring tool to detect suspicious messages in real-time using Python. The goal was to identify messages containing keywords related to illegal activities and log both user information and message content for further analysis. While building this, I faced a challenge: I needed to monitor not just text messages, but also detect suspicious content in images shared in the chat.

At the time, I had two separate Python scripts — one for text-based analysis using NLP (with NLTK's VADER sentiment analysis and keyword filtering), and another for image-based detection using a pre-trained YOLOv5 model. The problem was integrating both into a single workflow without missing real-time message events or causing performance issues.

To solve this, I broke the problem into steps:

Understanding the Telegram Client Flow: I explored Telethon's asynchronous message handling to figure out how to hook into both text and media message events.

Combining Logic Safely: I merged both scripts into a single async event handler. For text messages, I ran my NLP filter; for media, I downloaded the image temporarily, ran the YOLO model, and deleted the file after processing.

Testing & Optimization: I tested the integration with dummy chats and optimized the image processing to run in a non-blocking thread to maintain real-time performance.

Final Touches: I structured the outputs into a single suspicious_chats.json file that logged user details and the nature of the suspicious message.

In the end, I successfully created a unified script that monitors both text and image content for suspicious activity, all in real-time. This experience not only improved my understanding of async programming in Python, but also helped me sharpen my debugging and problem-solving skills.
