import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
from datetime import datetime

API_KEY = "0d31791086d9d8dc1d06afbd5e0ee2f6"

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

BG = "#1E1E2E"
CARD = "#2D2D44"
TEXT = "#FFFFFF"
ACCENT = "#4F46E5"


def update_clock():
    now = datetime.now()
    clock_label.config(
        text=now.strftime("%A, %d %B %Y | %I:%M:%S %p")
    )
    root.after(1000, update_clock)


def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": unit_var.get()
        }

        response = requests.get(CURRENT_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            messagebox.showerror(
                "Error",
                data.get("message", "Unable to fetch weather")
            )
            return

        forecast_response = requests.get(
            FORECAST_URL,
            params=params
        )

        forecast_data = forecast_response.json()

        update_weather(data)
        update_forecast(forecast_data)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def update_weather(data):
    city_country.config(
        text=f"{data['name']}, {data['sys']['country']}"
    )

    unit_symbol = "°C" if unit_var.get() == "metric" else "°F"

    temp_label.config(
        text=f"{round(data['main']['temp'])}{unit_symbol}"
    )

    condition_label.config(
        text=data['weather'][0]['description'].title()
    )

    humidity_value.config(
        text=f"{data['main']['humidity']}%"
    )

    wind_value.config(
        text=f"{data['wind']['speed']} m/s"
    )

    pressure_value.config(
        text=f"{data['main']['pressure']} hPa"
    )

    feels_value.config(
        text=f"{round(data['main']['feels_like'])}{unit_symbol}"
    )

    icon_code = data['weather'][0]['icon']
    load_icon(icon_code)


def load_icon(icon_code):
    try:
        icon_url = (
            f"https://openweathermap.org/img/wn/"
            f"{icon_code}@4x.png"
        )

        response = requests.get(icon_url)

        image = Image.open(BytesIO(response.content))
        image = image.resize((140, 140))

        photo = ImageTk.PhotoImage(image)

        icon_label.config(image=photo)
        icon_label.image = photo

    except:
        pass


def update_forecast(data):
    forecast_text.delete("1.0", tk.END)

    unit_symbol = "°C" if unit_var.get() == "metric" else "°F"

    forecast_text.insert(
        tk.END,
        "5-Day Forecast\n\n"
    )

    for item in data["list"][:12]:

        date = item["dt_txt"]
        temp = item["main"]["temp"]
        weather = item["weather"][0]["description"]

        forecast_text.insert(
            tk.END,
            f"{date}\n"
            f"Temperature: {temp}{unit_symbol}\n"
            f"Condition: {weather.title()}\n"
            f"{'-'*45}\n"
        )

root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("1000x780")
root.configure(bg=BG)
root.resizable(False, False)

title = tk.Label(
    root,
    text="☀ Weather Dashboard",
    font=("Segoe UI", 28, "bold"),
    bg=BG,
    fg=TEXT
)
title.pack(pady=10)

clock_label = tk.Label(
    root,
    font=("Segoe UI", 12),
    bg=BG,
    fg="lightgray"
)
clock_label.pack()

update_clock()

search_frame = tk.Frame(root, bg=BG)
search_frame.pack(pady=15)

city_entry = tk.Entry(
    search_frame,
    font=("Segoe UI", 14),
    width=25
)
city_entry.pack(side="left", padx=10)

unit_var = tk.StringVar(value="metric")

unit_menu = tk.OptionMenu(
    search_frame,
    unit_var,
    "metric",
    "imperial"
)
unit_menu.config(
    bg=ACCENT,
    fg="white",
    font=("Segoe UI", 11)
)
unit_menu.pack(side="left", padx=5)

search_btn = tk.Button(
    search_frame,
    text="Search",
    command=get_weather,
    bg=ACCENT,
    fg="white",
    font=("Segoe UI", 12, "bold"),
    width=10
)
search_btn.pack(side="left", padx=5)

weather_card = tk.Frame(
    root,
    bg=CARD,
    width=900,
    height=250
)
weather_card.pack(pady=10)
weather_card.pack_propagate(False)

city_country = tk.Label(
    weather_card,
    text="Enter a City",
    font=("Segoe UI", 20, "bold"),
    bg=CARD,
    fg=TEXT
)
city_country.pack(pady=5)

icon_label = tk.Label(
    weather_card,
    bg=CARD
)
icon_label.pack()

temp_label = tk.Label(
    weather_card,
    text="--°",
    font=("Segoe UI", 42, "bold"),
    bg=CARD,
    fg="white"
)
temp_label.pack()

condition_label = tk.Label(
    weather_card,
    text="Weather Condition",
    font=("Segoe UI", 15),
    bg=CARD,
    fg="lightgray"
)
condition_label.pack()


stats_frame = tk.Frame(root, bg=BG)
stats_frame.pack(pady=15)

cards = []

for i in range(4):
    frame = tk.Frame(
        stats_frame,
        bg=CARD,
        width=200,
        height=100
    )
    frame.pack(side="left", padx=10)
    frame.pack_propagate(False)
    cards.append(frame)

tk.Label(
    cards[0],
    text="Humidity",
    bg=CARD,
    fg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=5)

humidity_value = tk.Label(
    cards[0],
    text="--",
    bg=CARD,
    fg="white",
    font=("Segoe UI", 18)
)
humidity_value.pack()

tk.Label(
    cards[1],
    text="Wind Speed",
    bg=CARD,
    fg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=5)

wind_value = tk.Label(
    cards[1],
    text="--",
    bg=CARD,
    fg="white",
    font=("Segoe UI", 18)
)
wind_value.pack()

tk.Label(
    cards[2],
    text="Pressure",
    bg=CARD,
    fg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=5)

pressure_value = tk.Label(
    cards[2],
    text="--",
    bg=CARD,
    fg="white",
    font=("Segoe UI", 18)
)
pressure_value.pack()


tk.Label(
    cards[3],
    text="Feels Like",
    bg=CARD,
    fg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=5)

feels_value = tk.Label(
    cards[3],
    text="--",
    bg=CARD,
    fg="white",
    font=("Segoe UI", 18)
)
feels_value.pack()

forecast_frame = tk.Frame(
    root,
    bg=CARD
)
forecast_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=15
)

forecast_title = tk.Label(
    forecast_frame,
    text="Forecast",
    font=("Segoe UI", 18, "bold"),
    bg=CARD,
    fg="white"
)
forecast_title.pack(pady=10)

forecast_text = tk.Text(
    forecast_frame,
    height=12,
    bg="#252538",
    fg="white",
    font=("Consolas", 10),
    bd=0
)
forecast_text.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

footer = tk.Label(
    root,
    text="Powered by OpenWeatherMap",
    font=("Segoe UI", 10),
    bg=BG,
    fg="gray"
)
footer.pack(pady=5)

root.mainloop()