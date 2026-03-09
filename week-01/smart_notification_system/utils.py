import random

def generate_message():
    messages = [
        "Email...",
        "SMS...",
        "Push..."
    ]
    return random.choice(messages)