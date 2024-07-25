class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            "hello": "Hello! How can I assist you today?",
            "hi": "Hi there! How can I help you?",
            "how are you": "I'm a bot, so I don't have feelings, but thank you for asking!",
            "what is your name": "I am a rule-based chatbot created to assist you.",
            "bye": "Goodbye! Have a great day!",
            "thank you": "You're welcome! If you have any other questions, feel free to ask."
        }
    
    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.rules:
            if key in user_input:
                return self.rules[key]
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Create an instance of the chatbot
chatbot = RuleBasedChatbot()

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! Have a great day!")
        break
    response = chatbot.get_response(user_input)
    print(f"Bot: {response}")
