print("Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    # Exit condition
    if user == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break

    # Greetings
    elif "hello" in user or "hi" in user:
        print("Chatbot: Hello! How can I help you today?")

    # Asking health
    elif "how are you" in user:
        print("Chatbot: I'm functioning perfectly! Thanks for asking.")

    # Asking name
    elif "your name" in user:
        print("Chatbot: I am ChatPy, your Python chatbot.")

    # Time
    elif "time" in user:
        from datetime import datetime
        print("Chatbot: Current time is:", datetime.now().strftime("%H:%M:%S"))

    # Date
    elif "date" in user:
        from datetime import datetime
        print("Chatbot: Today's date is:", datetime.now().strftime("%Y-%m-%d"))

    # About
    elif "who created you" in user:
        print("Chatbot: I was created by a Python developer for learning purposes.")

    # Anything else
    else:
        print("Chatbot: Sorry, I didn’t understand that.")
