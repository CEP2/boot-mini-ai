import logging

import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")
args = parser.parse_args()
# Now we can access `args.user_prompt`

def main():
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]



    logger.info('Started...')

    print("Hello from mini-ai-agent!")
    if api_key != None:
        print("\tLoaded Gemini API Key!")
    else:
        raise RuntimeError("api key was not loaded")
    

    client = genai.Client(api_key=api_key)
    logger.info("getting ai response...")
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages,
    )
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    usage_stats = f"""Prompt tokens: {prompt_tokens}\nResponse tokens:{response_tokens}"""
    original_prompt = f"User prompt: {args.user_prompt}"
    logger.info(f"tokens used\n\tPrompt tokens: {prompt_tokens}\n\tResponse tokens: {response_tokens}")
    if args.verbose:
        print(original_prompt)
        print(usage_stats)
    print(response.text)

    # client.close()

    



if __name__ == "__main__":
    main()
