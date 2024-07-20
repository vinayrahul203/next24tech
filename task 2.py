import nltk
from nltk.chat.util import Chat, reflections
from introduction import introduction_convo  # Import pairs from the separate file
from science import science_convo
from sports import sports_convo
from trivia import trivia_convo

# Create a chatbot instance
data = trivia_convo + science_convo + sports_convo + introduction_convo

chatbot = Chat(data, reflections) 

# Start the conversation
print("HELLO THERE")
print("My name is Chatbot")
print("How may i be of assistance to you?")
print("Type 'quit' if you want to exit")
chatbot.converse()

