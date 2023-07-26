import requests
from datetime import datetime

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

def get_closest_weather_data(data, date):
    user_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    closest_diff = None
    closest_data = None
    
    for item in data["list"]:
        api_date = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
        diff = abs(api_date - user_date)
        
        if closest_diff is None or diff < closest_diff:
            closest_diff = diff
            closest_data = item
    
    return closest_data

def main():
    data = get_weather_data()
    if not data:
        return

    while True:
        print("\nSelect an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            closest_data = get_closest_weather_data(data, date)
            if closest_data:
                temperature = closest_data["main"]["temp"]
                print(f"Temperature at {date}: {temperature:.2f} Kelvin")
            else:
                print("Data not found for the specified date.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            closest_data = get_closest_weather_data(data, date)
            if closest_data:
                wind_speed = closest_data["wind"]["speed"]
                print(f"Wind Speed at {date}: {wind_speed:.2f} m/s")
            else:
                print("Data not found for the specified date.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            closest_data = get_closest_weather_data(data, date)
            if closest_data:
                pressure = closest_data["main"]["pressure"]
                print(f"Pressure at {date}: {pressure:.2f} hPa")
            else:
                print("Data not found for the specified date.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
