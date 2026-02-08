import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "271043de0650914e93fc7d1000f02b6a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()

        result_label.config(
            text=f"🌍 City: {city}\n🌡 Temperature: {temp} °C\n💧 Humidity: {humidity} %\n☁ Condition: {condition}"
        )

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Network error")


# ---------------- GUI SETUP ----------------

app = tk.Tk()
app.title("Weather App")
app.geometry("350x300")
app.resizable(False, False)

# Heading
title_label = tk.Label(app, text="Weather App", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# City input
city_entry = tk.Entry(app, font=("Arial", 12), justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

# Button
get_weather_btn = tk.Button(
    app,
    text="Get Weather",
    font=("Arial", 12),
    bg="blue",
    fg="white",
    command=get_weather
)
get_weather_btn.pack(pady=10)

# Result label
result_label = tk.Label(app, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=15)

# Run app
app.mainloop()
