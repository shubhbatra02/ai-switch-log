import json
import requests
url="https://api.open-meteo.com/v1/forecast"
params={"latitude": 28.45,"longitude": 77.02, "current_weather": True}
response= requests.get(url,params=params,timeout=10)
response.raise_for_status()
try:
    if response.status_code==200:
     data=response.json()
     print(type(data))
     print (data)

     for key,value in data.items():
      print(key, "-->",type(value).__name__ )
      print(data["current_weather"]["temperature"])
      print(data["current_weather"]["windspeed"])
      #with open("weather.json","w",encoding="utf-8") as f:
      # json.dump(data,f,indent=2)

      #with open ("weather_txt.txt","w",encoding='utf-8') as f:
      #f.write(str(data))
      #####loadinga nd reading the json file
     with open("weather.json") as f:
       loaded=json.load(f)

       print(loaded["current_weather"])

      #loading and reading text file to see how it will behave
      #with open("weather_txt.txt") as f:
      # loaded=json.load(f)
      # print(loaded["current_weather"])
    else:
     print(f"Error: {response.status_code}")
 

except requests.RequestException as e:
  print(f"Network error: {e}" )


   
  