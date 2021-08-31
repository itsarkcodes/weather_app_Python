import tkinter as tk
from tkinter.messagebox import showinfo
import requests
import json


def get_weather_data():
    API_KEY = "d56c8f69033661adb7ab6298b3df2444"
    # Get city name by user and find it through API 
    city = city_entry.get()
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    res = requests.get(URL)
    json_data = json.loads(res.text)
    # Show Data
    weather = json_data["weather"][0]["description"]
    temprature = json_data["main"]["temp"]
    humidity = json_data["main"]["humidity"]
    wind_speed = json_data["wind"]["speed"]

    showinfo(f'{city.title()} Weather',
             f' Weather: {weather} \n Temprature: {temprature} \n Humidity: {humidity} \n Wind Speed: {wind_speed}')


win = tk.Tk()
win.title('Weather App')
win.geometry('300x300')

app_label = tk.Label(win, text="Weather App", font=('Times', 20, 'bold'))
app_label.grid(row=0, column=2, columnspan=3)

city_label = tk.Label(win, text='Enter city name: ')
city_label.grid(row=1, column=0, pady=20)

city_entry = tk.Entry(win, width=30)
city_entry.grid(row=1, column=2, pady=10)

btn = tk.Button(win, text='Get Weather', bd=1, command=get_weather_data)
btn.grid(row=2, column=2, columnspan=1, pady=10)

win.mainloop()