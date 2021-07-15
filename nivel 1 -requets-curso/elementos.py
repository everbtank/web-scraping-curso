import requests
from bs4 import BeautifulSoup

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

soup = BeautifulSoup(page.content, 'html.parser')

items=[]

productos= soup.select('div.thumbnail')

for elem in productos:
    title=elem.select('h4> a.title')[0].text
    price=elem.select('h4.price')[0].text
    info ={
        "title":title.strip(),
        "price":price.strip(),
    }
    items.append(info)

print(items)
    
