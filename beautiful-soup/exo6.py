#Write a Python program to find the text of the first <a> tag of a given html text

import requests
from bs4 import BeautifulSoup

def getIntoHtml(url):
    res = requests.get(url)
    return res.text

soup = BeautifulSoup(getIntoHtml('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'), 'html.parser')
print(soup.find_all('a')[0].text)