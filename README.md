Welcome to the Cisco Weather Assistant + general chatbot!
# Currently the chatbot is able to answer simple, general queries, and is able to use an external tool if questions related to the weather are asked
----------------------------------

Setup Instructions here!

**After downloading everything as a .zip file, and moving the main folder somewhere accessible,**

1) open the program folder in your terminal

2) run the following:
 ```python -m venv venv```
This creates a virtual environment for the program to run inside.
 ```.\venv\scripts\activate```
## note: the second command will need to be run each time that you want to use the program.

3) run the following:
```pip install -r requirements.txt```
 This will install all of the dependancies, within the virtual environment

4) within the folder, in a code editor create a new file called .env
The file should contain your API keys for both ([Gemini](https://aistudio.google.com/api-keys?project=gen-lang-client-0072754352)) and ([OpenWeather](https://openweathermap.org/api)).
### The file should be formatted in the following
### ```GEMINI_API_KEY=YOUR KEY HERE```
### ```WEATHER_API_KEY=YOUR KEY HERE```

Note: both keys are free, but are not bundled with the program for security reasons, but can be acquired for *free* by following the links.
# These keys should never be committed to GitHub and are advised to be included in .gitignore if any public forks are made!

5) you're all set up! run `python main.py` to run the program!
----------------------------------
## Interaction Examples for the chatbot
---------------------------------- 

Tool-Routed Queries (External API):

You: "What's the temperature in London right now?"

You: "Is it raining in Berlin?"

Native Knowledge Base Queries:

You: "What is Cisco DNA Center?"

You: "What is a network switch?"



