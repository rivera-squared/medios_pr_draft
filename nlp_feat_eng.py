import pandas as pd
import numpy as np
import spacy
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# !python -m spacy download es_core_news_sm
#!python -m spacy download es_core_news_md

stop_words = stopwords.words('spanish')

# nlp = spacy.load('es_core_news_sm')
nlp = spacy.load('es_core_news_md')

df = pd.read_csv('primerahora.csv')
medios = pd.read_csv('medios_pr.csv')


###############################################################################

df['title_preprocessed'] = df['title'].apply(preprocess)
df['title_preprocessed'] = df['title_preprocessed'].apply(lower_text)
df['persons'] = df['title'].apply(persons)
df['organizations'] = df['title'].apply(orgs)
df['nouns'] = df['title'].apply(get_nouns)
df['verbs'] = df['title'].apply(get_verbs)
medios = pd.read_csv('medios_pr.csv')

medios['title_preprocessed'] = medios['title'].apply(preprocess)
medios['title_preprocessed'] = medios['title_preprocessed'].apply(lower_text)
medios['persons'] = medios['title'].apply(persons)
medios['organizations'] = medios['title'].apply(orgs)
medios['nouns'] = medios['title'].apply(get_nouns)
medios['proper_nouns'] = medios['title'].apply(get_proper_nouns)
medios['title_new'] = medios['title'].apply(remove_stopwords)
###############################################################################

newspapers = list(medios.media.unique())

# 2n-gramns mas comunes por periodico
for newspaper in newspapers:
    x = medios[medios['media'] == newspaper]
    print('\nFrases mas comunes publicadas por {}'.format(newspaper))
    print(get_ngrams(x['title_new']))

tokens_cluster = [word_tokenize(doc.lower()) for doc in df['title_preprocessed']]    

clean_token = []
for token in tokens_cluster:
    for tok in token:
        clean_token.append(tok)
print('\nLas 50 palabras mas frecuentes \n')    
print(Counter(clean_token).most_common(50))
    

tokens_cluster = [word_tokenize(doc.lower()) for doc in df['persons']]    

clean_token = []
for token in tokens_cluster:
    for tok in token:
        clean_token.append(tok)
print('\nLas 50 palabras mas frecuentes \n')    
print(Counter(clean_token).most_common(50))

for x in df['persons'][72]:
    if x.isalpha():
        print(x.isalpha())

# 2n-gramns mas comunes por periodico
for newspaper in newspapers:
    x = medios[medios['media'] == newspaper]
    print('\nFrases mas comunes publicadas por {}'.format(newspaper))
    print(get_ngrams(x['title_preprocessed']))

topics = list(df.topic.unique())
for topic in topics:
    x = df[df['topic']==topic]
    print('\nLos ngrams mas comunes de {}'.format(topic))
    print(get_ngrams(x.title_preprocessed))

