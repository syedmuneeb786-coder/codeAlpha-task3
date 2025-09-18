def chatbot():
    print("🤖 Simple Chatbot (type 'bye' to exit)")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["hello", "hi"]:
            print("Bot: Hi! 👋")
        elif user_input in ["how are you", "how r u"]:
            print("Bot: I'm fine, thanks! 😊")
        elif user_input == "bye":
            print("Bot: Goodbye! 👋")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
