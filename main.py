import os
from dotenv import load_dotenv
from google import genai
import time

print("4 debugging: script IS running!")
#so it can see .env
load_dotenv()

print("4 debugging: starting gemini also")
#'starting' gemini here
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error!! Gemini api key (GEMINI_API_KEY) not found, please check .env!!")
    exit(1) #exiting with 1, so we know what happened :3

client = genai.Client(api_key=api_key)
print("4 debugging: connected 2 gemini!! yay!!")

# mainstuffs here
def start_chatbot():
    print("\nHello, Hej, 你好! Cisco Weather assistant is here!")
    print("Type 'exit' or 'quit' at any time to close the chat.\n")
    
    while True:
        #input here
        uinput = input("You: ")

        # if exit/quit
        if uinput.strip().lower() in ['exit','quit']:
            print("🌟 Assistant: Byebye!")
            break
        
        # if no input
        if not uinput.strip():
            continue
                
        # logic for re-sending user input if 503!! (server busy)
        response = None
        retries = 3
        delay = 2 #seconds
        
        try:
            for attempt in range(retries):
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=uinput
                    )
                    break
                except Exception as e:
                    if "503" in str(e) and attempt < retries - 1:
                        print(f"Error: Gemini's servers are busy, retrying in {delay}s...") # Fixed printf -> print
                        time.sleep(delay)
                        delay *= 2 #delay will get longer per try
                    else:
                        raise e
                
            #show gemini's response, if no errors
            if response:
                print(f"🌟 Assistant: {response.text}\n")
            
        except Exception as e:
            print(f"There was an error submitting or retrieving your response:\n{e}\n")
            
if __name__ == "__main__":
    start_chatbot()