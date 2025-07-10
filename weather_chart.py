import requests
import matplotlib.pyplot as plt
from datetime import datetime

API_KEY = "b5eafc5c0610d57862d009ad18941092"
CITY = "Moradabad"  

# 📡 API URL to get 5-day forecast
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# 🌐 Step 1: Get data from API
response = requests.get(URL)
data = response.json()

# ✅ Check if request was successful
if data.get("cod") != "200":
    print("Error fetching data:", data.get("message"))
else:
    # 📊 Step 2: Extract required data (date + temperature)
    dates = []
    temperatures = []

    for forecast in data["list"]:
        date_time = forecast["dt_txt"]  # string format
        temp = forecast["main"]["temp"]  # temperature in Celsius
        # Convert to datetime object
        dates.append(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S"))
        temperatures.append(temp)

    # 🎨 Step 3: Plot the data
    plt.figure(figsize=(12, 5))
    plt.plot(dates, temperatures, marker='o', linestyle='-', color='blue')
    plt.title(f"5-Day Temperature Forecast for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
