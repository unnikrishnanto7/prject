import requests
from datetime import datetime


city = input("Enter city name: ")
api_key= "eb5ef05a1f20ab85b9ff23ff53bd617f"
url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

res = requests.get(url)
#print(res.json())
res = res.json()
temp_city = ((res['main']['temp']) - 273.15)
weather_desc = res['weather'][0]['description']
hmdt = res['main']['humidity']
wind_spd = res['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(city.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print (" speed    :",wind_spd ,'kmph')

with open('file2.txt', 'w')as f:
        
      f.write(f"""-------------------------------------------------------------
               Weather Stats for - {city.upper()}  || {date_time}
              -------------------------------------------------------------

               Current temperature is: {temp_city} deg C
               Current weather desc  :{weather_desc}
               Current Humidity      :{hmdt}% 
               speed    :{wind_spd} kmph
              """)
      f.close()