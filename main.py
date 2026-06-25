import os
from dotenv import load_dotenv
from google import genai
from google.genai import types #better config yayy
import time
#importing weather.py
from weather import get_weather

print("starting...")
#so it can see .env
load_dotenv()

print("fetching for gemini key..")
#'starting' gemini here
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error!! Gemini api key (GEMINI_API_KEY) not found, please check .env!!")
    exit(1) #exiting with 1, so we know what happened :3

client = genai.Client(api_key=api_key)
print("Successfully connected to Gemini API...\n")

# mainstuffs here
def start_chatbot():
    print("\nWelcome to the Weather Assistant!")
    print("Type 'exit', 'quit' or 'end' at any time to close the chat.\n")
    
    my_tools = [get_weather]
    
    config = types.GenerateContentConfig(
        tools=my_tools,
        system_instruction= "You are a Weather Assistant for Cisco alongside a regular chatbot, you have access to a RTS Weather tool. If the user input contains a weather or temperature query, call the provided tool for live data."
    )
    
    while True:
        #input here
        uinput = input("You: ")

        # if exit/quit
        if uinput.strip().lower() in ['exit','quit', 'end']:
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
                        contents=uinput,
                        config=config
                    )
                    break
                except Exception as e:
                    if "503" in str(e) and attempt < retries - 1:
                        print(f"Error: Gemini's servers are busy, retrying in {delay}s...") # this works now
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