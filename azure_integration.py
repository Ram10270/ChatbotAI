from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os

# Initialize Azure AI Services (Sentiment Analysis only)

# Azure Text Analytics API (Sentiment Analysis)
def analyze_sentiment(text):
    # Load Azure credentials from environment variables
    endpoint = os.getenv("AZURE_ENDPOINT")
    api_key = os.getenv("AZURE_KEY")
    
    # Initialize the Text Analytics Client
    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))
    
    try:
        # Perform sentiment analysis
        response = client.analyze_sentiment(documents=[text])[0]
        return response.sentiment, response.confidence_scores
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return "error", {}

# Example usage of the function
if __name__ == "__main__":
    # Sample text for sentiment analysis
    user_input = "I'm feeling very happy today!"
    
    # Analyze sentiment of the user input
    sentiment, confidence_scores = analyze_sentiment(user_input)
    
    # Print results
    print(f"Sentiment: {sentiment}")
    print(f"Confidence Scores: {confidence_scores}")
