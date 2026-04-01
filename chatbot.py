def chatbot():
    print("🤖 Hello! I'm BobBot. Type 'bye' to exit.")

    while True:
        message = input("You: ").lower()

        if message == "hello":
            print("BobBot: Hi! How are you?")

        elif message == "how are you":
            print("BobBot: I'm great! Ready to help you study Python.")

        elif message == "what is qa":
            print("BobBot: QA means Quality Assurance. It ensures software quality.")

        elif message == "bye":
            print("BobBot: Bye! See you next time.")
            break

        else:
            print("BobBot: Sorry, I don't understand that yet.")


chatbot()