import os 
import google.generativeai as genai 
import time
import json 


API_KEY = "Your API key"
MODEL_NAME = "gemini-2.0-flash" 

try:
    genai.configure(api_key=API_KEY)
    print("Gemini API configured successfully.!")
except Exception as e:
    print(f"Error configuring Gemini API: {e}")    
    print("Please ensure your API_KEY is correct and has access to the Gemini API.")
    exit()

    

MODEL = "gemini-2.0-flash"
model = genai.GenerativeModel(MODEL)
print(f"Model {MODEL} initialized successfully.")

SYSTEM_INSTRUCTION = "You are a friendly, enthusiastic, and slightly silly chatbot named 'Sparky'. You love to use emojis and encourage the user. Always end your responses with a positive remark."
print(f"Chatbot personality set: '{SYSTEM_INSTRUCTION}'")

chat_history = []


print("\n--- Sparky the Friendly Chatbot ---")
print("Type your message and press Enter. Type 'exit' to quit.")


while True:
    user_message = input("\nYou: ")

    if user_message.lower() == 'exit':
        print("Sparky: Goodbye, friend! Stay awesome! 👋😊")
        break

    try:
        chat_history.append({"role": "user", "parts": [{"text": user_message}]})
        response = model.generate_content(
            contents=chat_history
        )
        ai_response_text = response.text
        chat_history.append({"role": "model", "parts": [{"text": ai_response_text}]})

        print(f"Sparky: {ai_response_text}")
    except Exception as e:
        print(f"Sparky Error: Oh no! Something went wrong while I was thinking: {e}")
        print("Please try again or check your API key and model configuration. Keep shining! ✨")
