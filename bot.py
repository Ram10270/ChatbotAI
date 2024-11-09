# bot.py

import os
from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
from azure_integration import analyze_sentiment, recognize_intent  # Import the functions

# Define the bot adapter settings
adapter_settings = BotFrameworkAdapterSettings(
    app_id=os.getenv("MICROSOFT_APP_ID"),
    app_password=os.getenv("MICROSOFT_APP_PASSWORD")
)
adapter = BotFrameworkAdapter(adapter_settings)

# Simple dictionary-based response handler
RESPONSES = {
    "hello": "Hello! How can I assist you today?",
    "help": "I am a simple chatbot. You can say 'hello', 'help', or type any question!",
    "goodbye": "Goodbye! Have a great day!",
}

# Helper function to process user input and determine the response
def handle_user_input(user_input):
    """
    Process user input and return an appropriate response.
    """
    normalized_input = user_input.lower().strip()

    # First, check sentiment and LUIS intent
    sentiment, sentiment_scores = analyze_sentiment(user_input)
    intent_result = recognize_intent(user_input)

    # Handle sentiment and intent-based responses
    if intent_result:
        intent = intent_result.top_intent()
        if intent == "Greeting":
            return "Hello! How can I help you?"
        elif intent == "Goodbye":
            return "Goodbye! Have a nice day!"
        else:
            return f"Intent detected: {intent}. How can I assist you further?"

    # If no specific intent or sentiment analysis:
    if sentiment == "positive":
        return f"Your message seems positive! Sentiment score: {sentiment_scores.positive}"
    elif sentiment == "negative":
        return f"Your message seems negative! Sentiment score: {sentiment_scores.negative}"
    else:
        return f"Neutral sentiment detected. Score: {sentiment_scores.neutral}"

# Main message handler function
async def messages(req: web.Request) -> web.Response:
    # Read the incoming message from the user
    body = await req.json()
    activity = Activity().deserialize(body)

    # Define the response handler for the TurnContext
    async def message_handler(turn_context: TurnContext):
        response_text = handle_user_input(turn_context.activity.text)
        await turn_context.send_activity(response_text)

    # Process the activity using process_activity, not send_activity
    await adapter.process_activity(activity, "", message_handler)
    return web.Response(status=200)

# Set up the web server and route
app = web.Application()
app.router.add_post("/api/messages", messages)

# Run the app on localhost port 3978
if __name__ == "__main__":
    web.run_app(app, host="localhost", port=3978)
