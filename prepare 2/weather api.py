import requests
import json


def weather_api(city):
    api_key = 'eea4df88719a1833bbe8fe08085f6de4'
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    r=requests.get(url)
    data=json.loads(r.text)
    results={}
    results['lon']=data['coord']['lon']
    results['lat']=data['coord']['lat']
    results['name']=data['name']
    results['temp']=data['main']['temp']
    results['temp_min']=data['main']['temp_min']
    results['temp_max']=data['main']['temp_max']
    results['humidity']=data['main']['humidity']
    results['wind']=data['wind']['speed']
    results['clouds']=data['clouds']['all']
    results['country']=data['sys']['country']
    results['sunrise']=data['sys']['sunrise']
    results['sunset']=data['sys']['sunset']
    return results

print(weather_api('Dhaka'))