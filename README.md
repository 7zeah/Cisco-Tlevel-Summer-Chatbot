Welcome to the Cisco Weather Assistant + general chatbot!
Currently the chatbot is able to answer simple, general queries, and is able to use an external tool if questions related to the weather are asked
----------------------------------

Setup Instructions here!

**After downloading everything as a .zip file, and moving the main folder somewhere accessible,**

1) open the program folder in your terminal

2) run the following:
    `python -m venv venv`
    This creates a virtual environment for the program to run inside.
    `.\venv\scripts\activate`
    note: the second command will need to be run each time that you want to use the program.

3) run the following:
`pip install -r requirements`
    This will install all required environment variables, within the virtual environment

4) within the folder, in a code editor create your .env file.
    The file should contain your API keys for both (<[Gemini](https://aistudio.google.com/api-keys?project=gen-lang-client-0072754352)>) and (<[OpenWeather](https://openweathermap.org/api)>).
    The file should be formatted in the following
    `GEMINI_API_KEY=YOUR KEY HERE`
    `WEATHER_API_KEY=YOUR KEY HERE`

Note: both keys are free, but are not bundled with the program for security reasons, but can be acquired for *free* by following the links.
    These keys should not be committed to GitHub and are advised to be included in .gitignore if any forks are made!

5) you're all set up! run `python main.py` to run the program!
----------------------------------
Examples for the chatbot:
You: What's the temperature in London right now?
You: Is it raining in Berlin?
You: What is the Cisco DNA center?
You: What is a network switch?




