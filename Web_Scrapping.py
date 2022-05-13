# import time

# from lib2to3.pgen2 import driver
# from webbrowser import Chrome
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get("https://www.codechef.com/tags/problems/dynamic-programming")

# time.sleep(5)

# html = driver.page_source
# # print(html)

# soup = BeautifulSoup(html, 'html.parser')
# all_ques_div = soup.findAll("div", {"class": "problem-tagbox-inner"})

# # print(len(all_ques_div))

# all_ques = []
# for ques in all_ques_div:
#     all_ques.append(ques.findAll("div")[0].find("a"))

# # print(all_ques[0])

# urls = []
# title = []
# for ques in all_ques:
#     urls.append("https://www.codechef.com"+ques['href'])
#     title.append(ques.text)

# # print(urls[10])

# with open("problem_urls.txt", "w+") as f:
#     f.write('\n'.join(urls))

# with open("problem_titles.txt", "w+") as f:
#     f.write('\n'.join(title))

#****************************************************

# import time

# from lib2to3.pgen2 import driver
# from webbrowser import Chrome
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

# urls = ["https://www.codechef.com/problems/XYSTR", "https://www.codechef.com/problems/SUBINC", "https://www.codechef.com/problems/ALTARAY"]

# count = 0
# for url in urls:
#     driver.get(url)
#     count+=1
#     time.sleep(5)
#     html = driver.page_source
#     soup = BeautifulSoup(html, "html.parser")

#     problem_text = soup.find("div", {"class" : "problem-statement"}).get_text()

#     problem_text = problem_text.encode("utf-8")
#     problem_text = str(problem_text)

#     with open("problem_text-"+str(count)+".txt", "w+") as f:
#         f.write(problem_text)

# ******************************************************************************

import time
import os
import re

from lib2to3.pgen2 import driver
from webbrowser import Chrome
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.codechef.com/tags/problems/array")

time.sleep(5)

html = driver.page_source
# print(html)

soup = BeautifulSoup(html, 'html.parser')
all_ques_div = soup.findAll("div", {"class": "problem-tagbox-inner"})

# print(len(all_ques_div))

all_ques = []
for ques in all_ques_div:
    all_ques.append(ques.findAll("div")[0].find("a"))

# print(all_ques[0])

urls = []
title = []
for ques in all_ques:
    urls.append("https://www.codechef.com"+ques['href'])
    title.append(ques.text)

with open("problem_urls_array.txt", "w+") as f:
    f.write('\n'.join(urls))

with open("problem_titles_array.txt", "w+") as f:
    f.write('\n'.join(title))


# Creating New Folder

new_folder = r'Array_problems'
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

count = 0
for url in urls:
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    problem_text = soup.find("div", {"class" : "problem-statement"}).get_text()

    # File name with the title.
    with open("Array_problems/"+title[count]+".txt", "w+", encoding="utf-8") as f:
        txt = problem_text
        # txt = re.sub(r'\n\s*\n', '\n', txt)
        # Adds two blanks between all paragraphs
        txt = re.sub(r'\n\n\n', '\n', txt)
        # Removes the blank lines from the EOF
        txt = re.sub(r'\n*\Z', '', txt)
        f.write(txt)
    count+=1