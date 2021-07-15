import requests
from bs4 import BeautifulSoup

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

soup = BeautifulSoup(page.content, 'html.parser')

image_data=[]
imagenes=soup.select('img')

for img in imagenes:
    src=img.get('src')
    alt=img.get('alt')
    image_data.append({"src":src, "alt":alt})
    
print(image_data)
    


