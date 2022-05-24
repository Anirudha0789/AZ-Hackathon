# # import required module
# from sklearn.feature_extraction.text import TfidfVectorizer

# # merge documents into single corpus
# corpus = []
# count = 0
# while(count < 1944):
#   count+=1
#   fo1 = open('Keywords/keyword-'+str(count)+'.txt', encoding='utf-8')
#   docs = fo1.read()
#   corpus.append(docs)
#   # corpus.insert(1, docs)
  
# # create object
# tfidf = TfidfVectorizer()
  
# # get tf-df values
# result = tfidf.fit_transform(corpus)
  
# # get idf values
# # fo1 = open('idf.txt', 'w+', encoding='utf-8')
# # for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
# #     words = (ele1, ':', ele2)
# #     fo1.write(str(words)+'\n')
    
  
# # get indexing
# # fo2 = open('word_indexes.txt', 'w+', encoding='utf-8')
# # # fo2.write('Word indexes:\n')
# # fo2.write(str(tfidf.vocabulary_))
  

# # display tf-idf values
# fo3 = open('tf-idf.txt', 'w+', encoding='utf-8')
# # fo3.write('tf-idf value:\n')
# fo3.write(str(result)+'\n')
# # print(result)
  
# # # in matrix form
# # fo4 = open('tf-idf-matrix.txt', 'a', encoding='utf-8')
# # fo4.write('\ntf-idf values in matrix form:')
# # fo4.write((str(result.toarray())))

# ////////////////////////////////////////////////////////////////////////////////


# # import required module
# from sklearn.feature_extraction.text import TfidfVectorizer
# import pandas as pd

# # merge documents into single corpus
# corpus = []
# count = 0
# while(count < 1944):
#   count+=1
#   fo1 = open('Keywords/keyword-'+str(count)+'.txt', encoding='utf-8')
#   docs = fo1.read()
#   corpus.append(docs)

# vectorizer = TfidfVectorizer()
# vectors = vectorizer.fit_transform(corpus)
# feature_names = vectorizer.get_feature_names_out()
# dense = vectors.todense()
# denselist = dense.tolist()
# df = pd.DataFrame(denselist, columns=feature_names)

# # display tf-idf values
# fo3 = open('tf-idf.txt', 'a+', encoding='utf-8')
# # fo3.write('tf-idf value:\n')
# fo3.write('\n'+str(df))

# //////////////////////////////////////////////////////////////////////

# from opcode import opname
# from pydoc import doc
# import string
# from sklearn.feature_extraction.text import TfidfVectorizer
# import pandas as pd
# import numpy as np
# import re
# import sys
# from textblob import TextBlob
# from nltk.stem.porter import PorterStemmer
# from nltk.stem import LancasterStemmer

# def get_similar_articles(q, df):
#   print("query:", q)
#   print("cosine similarity: ")

#   # Convert the query become a vector
#   q = [q]
#   q_vec = vectorizer.transform(q).toarray().reshape(df.shape[0],)
#   sim = {}

#   # Calculate the similarity
#   for i in range(10):
#     sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
  
#   # Sort the values 
#   sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)

#   # Print the articles and their similarity values
#   file1 = open('result.txt', 'w+', encoding='utf-8')
#   for k, v in sim_sorted:
#     if v != 0.0:
#       file1.write("Nilai Similaritas: ")
#       file1.write(str(v)+'\n'+ '\n')
#       file1.write("Title: " + titles[k] + "\t\t\t\t\t")
#       file1.write("link: " + urls[k] +'\n'+ '\n')
#       file1.write(corpus[k] + '\n' + '\n')

# # Merging all the problems
# corpus = []
# count = 0
# while(count < 1944):
#   count+=1
#   fo1 = open('Problems/problem-'+str(count)+'.txt', encoding='utf-8')
#   docs = fo1.read()
#   corpus.append(docs)

# # Merging all the titles
# titles = []
# fo1_titles = open('problem_titles.txt', encoding='utf-8')
# doc_titles = fo1_titles.read()
# doc_titles = doc_titles.split('\n')
# for title in doc_titles:
#   titles.append(title)
#   corpus.append(title)

# # Merging all the urls
# urls = []
# fo1_urls = open('Problem_urls.txt', encoding='utf-8')
# doc_urls = fo1_urls.read()
# doc_urls = doc_urls.split('\n')
# for url in doc_urls:
#   urls.append(url)
#   corpus.append(url)

# # folwe = open('corpus.txt', 'a', encoding='utf-8')
# # folwe.write(str(corpus) +'\n\n\n\n')

# # Text processing
# documents_clean = []
# for d in corpus:
#     # Remove Unicode
#     document_test = re.sub(r'[^\x00-\x7F]+', ' ', d)

#     # Remove Mentions
#     document_test = re.sub(r'@\w+', '', document_test)

#     # Lowercase the document
#     document_test = document_test.lower()

#     # Remove punctuations
#     document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test)
    
#     # Lowercase the numbers
#     document_test = re.sub(r'[0-9]', '', document_test)

#     #  replace \n with space
#     document_test = re.sub("'\r\n'", r"' '", document_test)

#     # Remove the doubled space
#     document_test = re.sub(r'\s{2,}', ' ', document_test)
#     documents_clean.append(document_test)

# folwe = open('corpus.txt', 'a', encoding='utf-8')
# folwe.write(str(documents_clean) +'\n\n\n\n')

# # Instantiate a TfidfVectorizer object
# vectorizer = TfidfVectorizer()

# # It fits the data and transform it as a vector
# X = vectorizer.fit_transform(documents_clean)

# # Convert the X as transposed matrix
# X = X.T.toarray()

# # Create a DataFrame and set the vocabulary as the index
# df = pd.DataFrame(X, index=vectorizer.get_feature_names_out())

# # # display tf-idf values
# # fo3 = open('tf-idf.txt', 'w+', encoding='utf-8')
# # fo3.write(str(df)+'\n')


# # Add The Query
# queryString = 'sudoku'
# queryString = queryString.lower()
# queryString = TextBlob(queryString)
# queryString = str(queryString.correct())

# print(queryString)


# stemmer = PorterStemmer()
# queryString = stemmer.stem(queryString)

# print(queryString)


# # Lanc_stemmer = LancasterStemmer()
# # queryString = Lanc_stemmer.stem(queryString)

# # print(queryString)

# # Call the function
# get_similar_articles(queryString, df)