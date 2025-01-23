import requests

api_key = "41e706d4032fcadd3155cc572e92f899"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
while(True):
    city_name = input("Enter city name: ").strip()
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]

            temp_kelvin = main["temp"]
            temp_celsius = temp_kelvin - 273.15
            pressure = main["pressure"]
            humidity = main["humidity"]
            description = weather["description"]

            print(f"Temperature: {temp_celsius:.2f}°C")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Weather description: {description.capitalize()}")
            ch = input("If you want to check another city type (y) :")
            if (ch.lower()!="y" ):
                break
        else:
            print("City not found. Please check the city name.")
            city_name = input("Enter city name: ").strip()

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch weather details. {e}")
