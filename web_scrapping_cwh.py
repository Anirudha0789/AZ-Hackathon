from turtle import title
from xml.etree.ElementTree import Comment
import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

r = requests.get(url)
html_content = r.content

soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify)

# Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigablrString
# print(type(soup)) # 3. BeautifulSoup
# 4. Comment

title = soup.title   # get the title of html page

anchors = soup.find_all('a')
all_links = set()

for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://www.codewithharry.com"+link.get('href')
        all_links.add(linkText)
        print(linkText)

