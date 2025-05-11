
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "budget" in user_input or "cost" in user_input:
        return "The estimated budget includes the place's entry fee, ₹150 for transport, and about ₹300 for meals."

    elif "recommend" in user_input or "suggest" in user_input:
        return "Sure! Click the 'Suggest Nearby Places' button in the sidebar to see top tourist spots."

    elif "restaurant" in user_input or "food" in user_input:
        return "Nearby restaurants are listed under each place. You can check cuisines and ratings."

    elif "location" in user_input or "how far" in user_input:
        return "We calculate distances from your coordinates. You can set them in the sidebar."

    elif "hello" in user_input or "hi" in user_input:
        return "Hey there! 👋 Ready to explore Bangalore?"

    elif "map" in user_input:
        return "To see a map, check the 'Show map for ___' checkbox under each place."

    elif "help" in user_input:
        return "I'm here to help you explore, plan budgets, and find food spots. Ask away!"

    else:
        return "I'm still learning! Try asking about budget, places, food, or maps."
