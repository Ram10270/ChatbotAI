import os

class Config:
    ENDPOINT = "https://mst6languageservice.cognitiveservices.azure.com/"
    API_KEY = "BB63rZGgJy9RC26tKPhtMrR0DmYFjpOhLGevAt08o4vwo13wDV3vJQQJ99AKACYeBjFXJ3w3AAAaACOG0O84"  # Replace with actual API key for testing purposes


# Debugging statement to check if API_KEY is None
if Config.API_KEY is None:
    print("API Key not found! Make sure the MicrosoftAIServiceKey environment variable is set.")
