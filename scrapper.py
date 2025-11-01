import requests
from bs4 import BeautifulSoup

url = 'https://commeventshub.onrender.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

events = soup.find_all('div', class_='col')


print(len(events))
