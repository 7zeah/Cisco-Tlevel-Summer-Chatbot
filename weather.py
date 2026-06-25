import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(location: str) -> str:
    # grabs and returns weather info from OpenWeather API
    print("[SYSTEM]: calling external API...") # to tell user when api is called in main
    #get api
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        return "error: Weather api key (WEATHER_API_KEY) not found, please check .env!"
    
    url = f"https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q" : location,
        "appid" : api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(url, params=params, timeout = 5)
        
        if response.status_code == 404:
            return f"error: Could not find location named '{location}'. Please ensure your entry is spelled correctly."
        elif response.status_code == 403:
            return f"error: weather service auth failed. This means that your API key might be incorrect, or inactive"
        
        # any other errors
        response.raise_for_status()
        
        data = response.json() #what the api returned
        city_name = data.get("name")
        temp = data.get("main", {}).get("temp") #empty dict if no main (no error)
        description = data.get("weather", [{}])[0].get("description", "clear sky") 
        """
        really weird syntax but its grabbing a list of dictionaries, 
        then looking in the first element for "description", then if nothing, returns "clear sky" as a fallback
        """
        # formating results
        return f"the current weather in {city_name} is {temp}ºC with {description}."
    except requests.exceptions.Timeout:
        return "Error: the connection to the weather service has timed out! Please try again later."
    except requests.exceptions.RequestException as e:
        return f"Error: System unable to connect to the weather data streams. Details: {e}"
    
#debugging // testing
if __name__ == "__main__":
    print("manual test..")
    test_result = get_weather("Belfair")
    print(test_result)
#pretty sure this can stay here since we'll only be importing this .py