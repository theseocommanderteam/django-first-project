import requests
from bs4 import BeautifulSoup as bs

def get_weather_data(city):
    city = city.replace(' ','+')
    url = f'https://www.google.com/search?q=weather+of+{city}'
    USER_AGENT= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    LANGUAGE="en-US,en;q=0.9"
    session= requests.Session()
    session.headers['user-agent']= USER_AGENT
    session.headers['accept-language']= LANGUAGE
    r = session.get(url)
    soup = bs(r.text,'html.parser')
    # Extract Region
    results={}
    results['region'] = soup.find('div', attrs={'id' : 'wob_loc'}).text
    results['daytime'] = soup.find('div', attrs={'id' : 'wob_dts'}).text
    results['weather'] = soup.find('span', attrs={'id' : 'wob_dc'}).text
    results['temp'] = soup.find('span', attrs={'id' : 'wob_tm'}).text
    return results
get_weather_data('new york')
