from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import Config

# Initialize Text Analytics Client
text_analytics_client = TextAnalyticsClient(
    endpoint=Config.ENDPOINT,
    credential=AzureKeyCredential(Config.API_KEY)
)

def analyze_sentiment(text):
    response = text_analytics_client.analyze_sentiment(documents=[text])[0]
    return response.sentiment  # Returns "positive", "neutral", or "negative"

def chatbot_response(user_input):
    # Analyze sentiment of the input
    sentiment = analyze_sentiment(user_input)

    # Generate a response based on sentiment
    if sentiment == "positive":
        return "I'm glad you're feeling positive! 😊 How can I help?"
    elif sentiment == "neutral":
        return "Thank you for sharing! Let me know if there's anything else."
    else:
        return "I'm here for you if you need support. 🌸"

# Example usage
user_message = input("You: ")
print("Bot:", chatbot_response(user_message))
