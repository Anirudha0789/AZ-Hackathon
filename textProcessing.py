# from base64 import decode
# from string import digits
# import nltk
# import io
# import re
# import fileinput
# import string
# import os
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
 
# stop_words = set(stopwords.words('english'))
# count = 0
# while(count < 903):
#     count+=1
#     file1 = open("NewFolder/processed-"+str(count)+".txt", encoding="utf-8")

#     # Creating New Folder or opening existing one.

#     new_folder = r'Newfold'
#     if not os.path.exists(new_folder):
#         os.makedirs(new_folder)
    
#     # Use this to read file content as a stream:

#     line = file1.read()
#     words = line.split()
#     for r in words:
#         if not r in stop_words:
#             appendFile = open('Newfold/pro-'+str(count)+'.txt','a+', encoding="utf-8")
#             appendFile.write(" "+r)
#             appendFile.close()

# *************************************************************

from pydoc import importfile
import unicodedata
from unittest import result
import nltk
import string
import re
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def text_lowercase(text):
    return text.lower()

def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_URL(sample):
    """Remove URLs from a sample string"""
    return re.sub(r"http\S+", "", sample)


new_folder = r'NewFolder'
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

count = 0
while(count < 902):
    count+=1
    file1 = open('Problems/problem-'+str(count)+'.txt', 'r', encoding='utf-8')
    words = file1.read()
    words = words.replace('\n', " ").split(".")
    words = str(words)
    words = remove_URL(words)
    words = text_lowercase(words)
    words = remove_numbers(words)
    words = remove_punctuation(words)
    words = str(words)
    fo1 = open("NewFolder/processed-"+str(count)+".txt", 'a', encoding='utf-8')
    fo1.write(words)
    # print(stop_words)