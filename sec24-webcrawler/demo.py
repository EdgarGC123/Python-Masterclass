from urllib.request import urlopen

import requests

from bs4 import BeautifulSoup

html = urlopen("https://www.google.com")
print(html.read())


# html2 = requests.get("http://www.wikipedia.org")
# print(html2.text)


# bsobject = BeautifulSoup(html.read(), "html.parser")
# print(bsobject.title) #bsobject.h1