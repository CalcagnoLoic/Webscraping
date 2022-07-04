#Write a Python program to find the length of the text of the first <h2> tag of a given html document

import requests
from bs4 import BeautifulSoup

def getIntoHtml(url):
    res = requests.get(url)
    return res.text

soup = BeautifulSoup(getIntoHtml('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'), 'html.parser')
print(len(soup.find_all('h2')[0].text))