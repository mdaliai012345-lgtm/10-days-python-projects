import requests
api_key = "0d47ea9dd86fd2e636262afcd9b98395"
city = input("Enter city name ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()
if data["cod"] == 200:
    print("City",data["name"])
    print("Temperature",data["main"]["temp"],"C")
    print("Weather:",data["weather"][0]["description"])
else:
    print("city not found")
