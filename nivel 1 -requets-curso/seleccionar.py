import requests
from bs4 import BeautifulSoup

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

soup = BeautifulSoup(page.content, 'html.parser')

all_h1=[]
for element in soup.select('h1'):
    all_h1.append(element.text)
all_p=[]

for element in soup.select('p'):
    all_p.append(element.text)  


print(all_p)
print()
print(all_h1)

