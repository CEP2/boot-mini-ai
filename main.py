import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    print("Hello from mini-ai-agent!")
    if api_key != None:
        print("\tLoaded Gemini API Key!")
    else:
        raise RuntimeError("api key was not loaded")
    
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    )
    print(response.text)

    # client.close()

    



if __name__ == "__main__":
    main()
