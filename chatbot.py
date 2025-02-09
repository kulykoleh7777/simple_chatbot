def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(user_input.lower(), "I'm not sure how to respond to that.")

print(chatbot_response("hello"))
