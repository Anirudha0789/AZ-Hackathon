import math
import string
import re

from gensim.parsing.preprocessing import remove_stopwords


f2 = open("./corpus.txt", 'a+', encoding='utf-8')
for cnt in range(0, 2469):
    f1 = open('Problems/problem-'+str(cnt+1)+'.txt', encoding='utf-8')
    docs = str(f1.read())
    local = []
    docs = docs.replace("\\n", " ")
    docs = docs.replace("\n", " ")
    docs = re.sub(r'[^\x00-\x7F]+', ' ', docs)
    docs = re.sub(r'@\w+', ' ', docs)
    docs = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', docs)
    docs = re.sub(r'[0-9]', ' ', docs)
    docs = re.sub(r'\s{2,}', ' ', docs)
    local.append(docs)
    f2.write(str(local)+'\n')


# f2 = open('corpus.txt', encoding='utf-8')
# docs = f2.read()
# docs = docs.split('\n')
# print(docs[2468])