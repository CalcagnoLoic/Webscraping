#Write a Python program to find the title tags from a given html document

import requests
from bs4 import BeautifulSoup

def getIntoHtml(url):
    res = requests.get(url)
    return res.text

soup = BeautifulSoup(getIntoHtml('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'), 'html.parser')
print(soup.find("title"))