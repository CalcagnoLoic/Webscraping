# Write a Python program to find the title tags from a given html document

import requests
from bs4 import BeautifulSoup

def getIntoHtml(url):
    res = requests.get(url)
    return res.text

soup = BeautifulSoup(getIntoHtml('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'), 'html.parser')
print(soup.find("title"))


# Write a Python program to retrieve all the paragraph tags from a given html document

soup = BeautifulSoup(getIntoHtml('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'), 'html.parser')
print(soup.find_all("p"))


# Write a Python program to get the number of paragraph tags of a given html document

soup = BeautifulSoup(getIntoHtml('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'), 'html.parser')
res = soup.find_all("p")
print(len(res))

# Write a Python program to extract the text in the first paragraph tag of a given html document

soup = BeautifulSoup(getIntoHtml('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'), 'html.parser')
print(soup.find_all("p")[0].text)


# Write a Python program to find the length of the text of the first <h2> tag of a given html document

soup = BeautifulSoup(getIntoHtml('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'), 'html.parser')
print(len(soup.find_all('h2')[0].text))


# Write a Python program to find the text of the first <a> tag of a given html text

soup = BeautifulSoup(getIntoHtml('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'), 'html.parser')
print(soup.find_all('a')[0].text)


#Write a Python program to find the href of the first <a> tag of a given html document.

soup = BeautifulSoup(getIntoHtml('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'), 'html.parser')
print(soup.find('a').attrs['href'])