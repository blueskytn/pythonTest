from bs4 import BeautifulSoup
from pprint import pprint
import requests
import re

html = requests.get('https://r6.tracker.network/profile/pc/NickName')

soup = BeautifulSoup(html.text, 'html.parser')
name = soup.find('h1', {'class': 'trn-profile-header__name'}).text
name = name.replace('\n', '')
name = name.replace('2 Profile Views', '')
rank = soup.find('div', {'style' :'flex-grow: 1; display: flex; justify-content: space-between; align-items: center;'}).text
rank = rank.strip()
rank = rank.replace('\n', ' / ')


print('Name: '+name)
print('Rank: '+rank)
