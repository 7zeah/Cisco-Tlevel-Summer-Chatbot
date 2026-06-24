import os
from dotenv import load_dotenv
from google import genai

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
        
        try:
            #usr gemini (flash), wait for a response
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=uinput
            )
            
            #show gemini's response
            print(f"🌟 Assistant: {response.text}\n")
            
        except Exception as e:
            print(f"There was an error submitting or retrieving your response:\n{e}\n") #this will display the actual error to the user!! waoww!!
            
if __name__ == "__main__":
    start_chatbot()