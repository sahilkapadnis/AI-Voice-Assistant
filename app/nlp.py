import random

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I assist?"],
    "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    "unknown": ["I'm not sure how to respond to that."]
}

def process_text(text: str) -> str:
    text = text.lower()
    if "hello" in text or "hi" in text:
        return random.choice(responses["greeting"])
    elif "bye" in text or "goodbye" in text:
        return random.choice(responses["goodbye"])
    else:
        return random.choice(responses["unknown"])
