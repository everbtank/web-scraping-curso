import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

soup = BeautifulSoup(page.content, 'html.parser')

all_productos=[]
productos= soup.select('div.thumbnail')

for product in productos:
    name = product.select('h4 > a')[0].text.strip()
    descripcion = product.select('p.description')[0].text.strip()
    price = product.select('h4.price')[0].text.strip()
    views = product.select('div.ratings')[0].text.strip()
    image = product.select('img')[0].text.strip()

    all_productos.append({
        "name": name,
        "description": descripcion,
        "price": price,
        "views": views,
        "image": image
    })

keys = all_productos[0].keys()

with open('products.csv','w',newline='') as output_file:
    writer = csv.DictWriter(output_file,keys)
    writer.writeheader()
    writer.writerows(all_productos)


  
