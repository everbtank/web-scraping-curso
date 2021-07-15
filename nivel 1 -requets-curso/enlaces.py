import requests
from bs4 import BeautifulSoup

page = requests.get('https://muliier.com/')

soup = BeautifulSoup(page.content, 'html.parser')

all_links=[]

links=soup.select('a')

for a in links:
    text = a.text
    text = text.strip() if text is not None else ''
    
    href= a.get('href')
    href = href.strip() if href is not None else ''
    
    all_links =({"href":href,"text":text})
    
    
print(links)