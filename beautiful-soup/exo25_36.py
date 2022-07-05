import requests
from bs4 import BeautifulSoup

def getIntoHtml(url):
    res = requests.get(url)
    return res.text

# Write a Python program to find tags by CSS class in a given html document

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


# Write a Python program to change the tag's contents and replace with the given string

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


# Write a Python program to add to a tag's contents in a given html document

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


# Write a Python program to insert a new text within a url in a specified position

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


# Write a Python program to insert tags or strings immediately before specified tags or strings

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


# Write a Python program to insert tags or strings immediately after specified tags or strings

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


# Write a Python program to extract a tag or string from a given tree of html document

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


# Write a Python program to remove a tag from a given tree of html document and destroy it and its contents

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


# Write a Python program to find tags by CSS class in a given html document

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


# Write a Python program to remove a tag or string from a given tree of html document and replace it with the given tag or string

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


# Write a Python program to wrap an element in the specified tag and create the new wrapper

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


# Write a Python program to replace a given tag with whatever's inside a given tag

soup = BeautifulSoup(getIntoHtml('https://www.python.org/'), 'html.parser')

print("============================================================================================================")


