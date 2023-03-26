import tkinter as tk
import requests
import json

root = tk.Tk()
root.title("Weather App")

# Create a label for the city input
city_label = tk.Label(root, text="Enter a city:")
city_label.pack()

# Create an entry box for the city input
city_entry = tk.Entry(root)
city_entry.pack()

# get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate the x and y positions to place the window in the center
x_pos = int(screen_width / 2 - 400 / 2)
y_pos = int(screen_height / 2 - 300 / 2)

# set the window size and position
root.geometry(f"400x300+{x_pos}+{y_pos}")

# Create a button to retrieve the weather data
def get_weather():
    city = city_entry.get()
    api_key = 'Your API Key HERE'
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(weather_url)
    weather_data = json.loads(response.text)
    weather_label.config(text=f"Temperature: {weather_data['main']['temp']}°F\nHumidity: {weather_data['main']['humidity']}%")

weather_button = tk.Button(root, text="Get Weather", command=get_weather)
weather_button.pack()

# Create a label to display the weather data
weather_label = tk.Label(root)
weather_label.pack()

root.mainloop()
