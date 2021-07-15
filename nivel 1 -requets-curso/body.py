import requests
from bs4 import BeautifulSoup

page = requests.get('https://sumaktec.com')
soup = BeautifulSoup(page.content,'html.parser')

page_title=soup.title.text

page_head=soup.head.text

page_body=soup.body.text

#print(page_title, page_head, page_body)

print(page_body)