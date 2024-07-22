import requests

def get_weather(city):
    # Replace 'your_api_key' with your actual API key from OpenWeatherMap
    api_key = 'your_api_key'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    # Construct the full API request URL
    url = f'{base_url}?q={city}&appid={api_key}&units=metric'

    # Send a GET request to the API
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        # Extract the relevant information
        temperature = main['temp']
        description = weather['description']

        # Print the weather information
        print(f'Weather in {city}:')
        print(f'Temperature: {temperature}°C')
        print(f'Description: {description.capitalize()}')
    else:
        print('City not found or there was an error with the request.')

# Get weather information for a specific city
city = 'London'
get_weather(city)