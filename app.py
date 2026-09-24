import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Error: No API Key found")

client = genai.Client(api_key=api_key)


def chat_with_gemini_agent(prompt):
    try:
        print("Sending request...")

        # Initialize chat session using the available gemini-3.6-flash model
        chat = client.chats.create(model="gemini-3.6-flash")
        
        # Send message via chat to resolve AFC warnings and handle stream cleanly
        response = chat.send_message(prompt)

        print("Gemini API Response:", response.text)
        return response.text

    except Exception as e:
        print("Error occurred while calling Gemini API:", str(e))
        return None


if __name__ == "__main__":
    user_prompt = input("Enter your prompt for Gemini API: ")
    chat_with_gemini_agent(user_prompt)