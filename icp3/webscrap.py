import requests
import soup as soup
from bs4 import BeautifulSoup
import os
url="https://en.wikipedia.org/wiki/Deep_learning"
scode= requests.get(url)
ptext= scode.text
soup= BeautifulSoup(ptext,"html.parser")
title= soup.title
print("The title of the page is", title)
links= []
for link in soup.find_all('a'):
   links.append(link.get('href'))
print (links)



