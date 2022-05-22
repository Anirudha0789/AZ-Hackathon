# import required module
from sklearn.feature_extraction.text import TfidfVectorizer

# merge documents into single corpus
corpus = []
count = 0
while(count < 1944):
  count+=1
  fo1 = open('Keywords/keyword-'+str(count)+'.txt', encoding='utf-8')
  docs = fo1.read()
  corpus.append(docs)
  # corpus.insert(1, docs)
  
# create object
tfidf = TfidfVectorizer()
  
# get tf-df values
result = tfidf.fit_transform(corpus)
  
# get idf values
# fo1 = open('idf.txt', 'w+', encoding='utf-8')
# for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
#     words = (ele1, ':', ele2)
#     fo1.write(str(words)+'\n')
    
  

# get indexing
# fo2 = open('word_indexes.txt', 'w+', encoding='utf-8')
# # fo2.write('Word indexes:\n')
# fo2.write(str(tfidf.vocabulary_))
  
# display tf-idf values
fo3 = open('tf-idf.txt', 'w+', encoding='utf-8')
# fo3.write('tf-idf value:\n')
# fo3.write(str(result)+'\n')
print(result)
  
# # in matrix form
# fo4 = open('tf-idf-matrix.txt', 'a', encoding='utf-8')
# fo4.write('\ntf-idf values in matrix form:')
# fo4.write((str(result.toarray())))

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