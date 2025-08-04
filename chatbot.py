import nltk
from nltk.chat.util import Chat, reflections

# Define possible user messages and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hey there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created by Madhuri!", "You can call me CodBot."]
    ],
    [
        r"how are you?",
        ["I'm good, thank you! How about you?", "Doing great!"]
    ],
    [
        r"what can you do?",
        ["I can answer your basic questions. Try asking me about weather, time, or general stuff!"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "Bye! Take care."]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Can you rephrase it?"]
    ]
]

# Start the chatbot
def chatbot():
    print("Hi, I'm CodBot! (Type 'quit' to exit)\n")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__=="__main__":
    chatbot()