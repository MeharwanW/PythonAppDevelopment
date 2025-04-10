from tkinter import *
from tkinter import ttk
import requests

def get_weather():
    city = com.get()
    if city:
        try:
            url = f"https://wttr.in/{city}?format=3"
            response = requests.get(url)
            if response.status_code == 200:
                weather_result.config(text=response.text)
            else:
                weather_result.config(text="Couldn't fetch weather info.")
        except Exception as e:
            weather_result.config(text=f"Error: {e}")
    else:
        weather_result.config(text="Please select a city.")

# GUI setup
win = Tk()
win.title("Weather App")
win.config(bg="grey")
win.geometry("500x400")

# Title Label
Label(win, text="Weather Checker", font=("Helvetica", 16, "bold"), bg="grey").pack(pady=20)

# Combo Box for City Selection
list_value = ["Karachi", "Jhatpat", "Jacobabad", "Sukkur", "Lahore", "Multan", "Peshawar", "Quetta", "Gwadar", "Sibi", "Muchh"]
com = ttk.Combobox(win, values=list_value, font=("Helvetica", 12))
com.set("Select a city")
com.pack(pady=10)

# Button to Fetch Weather
Button(win, text="Get Weather", font=("Comic Sans MS", 14, "bold"), command=get_weather).pack(pady=20)

# Label to Display Weather Info
weather_result = Label(win, text="", font=("Comic Sans MS", 12), bg="grey", wraplength=400, justify="center")
weather_result.pack(pady=20)

win.mainloop()
