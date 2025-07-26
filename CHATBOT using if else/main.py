
import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the Python developer go broke? Because he couldn’t ‘C’ his income.",
    "Why was the computer cold? It left its Windows open!",
    "I told my computer I needed a break, and it said 'No problem, I’ll go to sleep.'",
    "What do you call a lazy Python programmer? A slacker.py!"
]

print("Welcome to BH Chatbot! Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi there! How can I help you?")
    elif user_input == "how are you":
        print("Bot: I'm just a bot, but I'm doing fine. Thank you!")
    elif user_input == "what is your name":
        print("Bot: I'm BH Chatbot, your Python intern assistant.")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    elif user_input == "help":
        print("Bot: Try saying 'hello', 'how are you', 'joke', or 'bye'.")
    elif user_input == "who created you":
        print("Bot: I was created by an intern using Python and if-else.")
    elif user_input == "joke":
        print("Bot:", random.choice(jokes))
    elif user_input == "exit":
        print("Bot: Exiting the chat. Bye!")
        break
    else:
        print("Bot: I'm sorry, I don't understand that.")

