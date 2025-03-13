import requests
import matplotlib.pyplot as plt
from datetime import datetime, timezone, timedelta

# Prompt user to enter the city name
city_name = input("Enter city name: ")

# Define API key and endpoint URL
API_Key = 'ff5395904ab7f5c7352c6271cf9e5836'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric"

# Send API request and fetch response
display_chart = False
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Extract essential weather information
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    
    # Convert sunrise and sunset time from UTC to IST (Indian Standard Time)
    utc_sunrise = datetime.fromtimestamp(data['sys']['sunrise'], tz=timezone.utc)
    utc_sunset = datetime.fromtimestamp(data['sys']['sunset'], tz=timezone.utc)
    
    ist_offset = timedelta(hours=5, minutes=30)  # IST is UTC +5:30
    ist_sunrise = utc_sunrise + ist_offset
    ist_sunset = utc_sunset + ist_offset

    # Display the weather details
    print(f"\nWeather in {city_name}: {weather_description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Sunrise (IST): {ist_sunrise.strftime('%H:%M:%S')}")
    print(f"Sunset (IST): {ist_sunset.strftime('%H:%M:%S')}")
    
    # Prepare data for visualization
    labels = ['Temperature (°C)', 'Humidity (%)', 'Sunrise (IST)', 'Sunset (IST)']
    values = [temperature, humidity, ist_sunrise.hour + ist_sunrise.minute / 60, ist_sunset.hour + ist_sunset.minute / 60]

    # Generate a bar chart for weather parameters
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['blue', 'orange', 'green', 'red'])
    plt.xlabel("Weather Parameters")
    plt.ylabel("Values")
    plt.title(f"Weather Data for {city_name}")
    plt.show()

else:
    # Print an error message if the API request fails
    print(f"API request failed! Status Code: {response.status_code}")
    print(f"Response: {response.text}")
