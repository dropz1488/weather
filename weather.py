import requests
city = input("Введите название города: ")
if city.strip() == "":
  print("Вы не ввели название города.")
else:
  print(f"Вы выбрали город: {city}")

url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": "dfbdd214a5b8cc18a68b2112835feaa4",
    "units": "metric"
}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    city_name = data["name"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
    print(f"\nПогода в городе {city_name}:")
    print(f"Описание: {description}")
    print(f"Температура: {temp}°C")
    print(f"Ощущается как: {feels_like}°C")
    print(f"Влажность: {humidity}%")
    print(f"Скорость ветра: {wind_speed} м/с")
else:
    print("Ошибка:", response.status_code, response.text)
print("Программа завершена.")
input("\nНажмите Enter для выхода...")

