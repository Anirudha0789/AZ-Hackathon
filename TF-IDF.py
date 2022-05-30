import math
import string
import re

from gensim.parsing.preprocessing import remove_stopwords

keywords = []
sentence = []

# f2 = open("./sentence.txt", 'a+')
for cnt in range(0, 2469):
    f1 = open('Problems/problem-'+str(cnt+1)+'.txt', encoding='utf-8')
    docs = str(f1.read())

    # filtered_sentence = remove_stopwords(docs)
    docs = docs.replace("\\n", " ")

    documents_clean = []
    # for :
    # Remove Unicode
    document_test = re.sub(r'[^\x00-\x7F]+', ' ', docs)

    # Remove Mentions
    document_test = re.sub(r'@\w+', ' ', document_test)

    # Lowercase the document
    document_test = document_test.lower()

    # Remove punctuations
    document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test)

    # Lowercase the numbers
    document_test = re.sub(r'[0-9]', ' ', document_test)

    # Remove the doubled space
    document_test = re.sub(r'\s{2,}', ' ', document_test)
    documents_clean.append(document_test)

    filtered_sentence = remove_stopwords(documents_clean[0])

    filtered_sentence = sorted(filtered_sentence.split(" "))

    sentence.append(filtered_sentence)
    
    # writing in the sentence.txt file
    # f2.write(str(filtered_sentence)+'\n')

    filtered_sentence = set(filtered_sentence)

    for i in filtered_sentence:
        keywords.append(i)


keywords = sorted(set(keywords))

# f3 = open("Keywords.txt", 'w+', encoding='utf-8')
# f3.write('\n'.join(keywords))


# Calculating TF and writing in the tf.txt
TF = []
# f4 = open('./tf.txt', 'a+', encoding='utf-8')
for i in range(len(sentence)):
    no_of_keywords_local = len(sentence[i])
    # tf_local = []
    for j in range(len(keywords)):
        cnt = (sentence[i].count(keywords[j]))
        if cnt == 0:
            continue
        tf_local = []
        tf_local.append(i)
        tf_local.append(j)
        tf_local.append(cnt/no_of_keywords_local)
        TF.append(tf_local)
        # f4.write(str(tf_local) + '\n')


# Calculating IDF and writing in the idf.txt
IDF = []

N = len(sentence)

counts = []
for i in range(len(keywords)):
    counts.append(0)

for i in range(len(TF)):
    counts[TF[i][1]] += 1

# print(counts)
for i in range(len(keywords)):
    IDF.append((1+math.log(N/counts[i])))

# f5 = open("./idf.txt", 'w+')
# for i in IDF:
#   f5.write(str(i) + "\n")


# # Calculating Importance Matrix (TFIDF Matrix) and writing in the tf-idf.txt
Importance_Matrix = []
# f6 = open('./tf-idf.txt', 'a+')
for i in range(len(TF)):
    Imp_Matrix = []
    Imp_Matrix.append(TF[i][0])
    Imp_Matrix.append(TF[i][1])
    Imp_Matrix.append(TF[i][2] * IDF[TF[i][1]])

    Importance_Matrix.append(Imp_Matrix)
    # f6.write(str(Imp_Matrix)+'\n')


# # Calculate Magnitude of the vector and writing in the Magnitude.txt
Magnitude = []

for i in range(len(sentence)):
    Magnitude.append(0.0)

for i in range(len(Importance_Matrix)):
    Magnitude[Importance_Matrix[i][0]] += Importance_Matrix[i][2] * \
        Importance_Matrix[i][2]

for i in (range(len(Magnitude))):
    Magnitude[i] = math.sqrt(Magnitude[i])


f7 = open("./Magnitude.txt", 'w+')
for i in Magnitude:
  f7.write(str(i) + "\n")