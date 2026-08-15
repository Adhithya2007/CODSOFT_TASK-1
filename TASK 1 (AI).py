def chatbot(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"

    elif "how are you" in message:
        return "I'm fine, thank you!"

    elif "your name" in message:
        return "I'm a simple rule-based chatbot."

    elif "python" in message:
        return "Python is a popular programming language."

    elif "ai" in message or "artificial intelligence" in message:
        return "AI allows computers to perform tasks that need human intelligence."

    elif "internship" in message:
        return "This project is created for the CODSOFT AI internship."

    elif "bye" in message:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."


print("===================================")
print("       CODSOFT AI CHATBOT")
print("       TASK 1")
print("===================================")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ")
    reply = chatbot(user)

    print("Bot:", reply)

    if user.lower() == "bye":
        break
