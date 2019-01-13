import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"
appId = "Your App ID"

cityName = input("Enter a city name: ")
end_point_url = api_url+"?appid="+appId+"&q="+cityName

json_data = requests.get(end_point_url).json()
#print the complete json response
print(json_data)
print("---------------------------------------------------")

#print just the weather
current_weather = json_data['weather'][0]['main']
print("The current Weather of "+ cityName+ " : "+current_weather)
