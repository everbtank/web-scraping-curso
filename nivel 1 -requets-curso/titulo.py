import requests
from bs4 import BeautifulSoup

page = requests.get('https://sumaktec.com')
soup = BeautifulSoup(page.content,'html.parser')
title = soup.title.text
print(title)