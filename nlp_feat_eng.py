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
###############################################################################
# SECCIONES DE FUNCIONES
# Funcion para lemmatizar el texto
def preprocess(text):
    # Create Doc object
    doc = nlp(text, disable=['ner','parser'])
    # Generate lemmas
    lemmas = [token.lemma_ for token in doc]
    # Remove stopwords and non-alphabetic characters
    a_lemmas = [lemma for lemma in lemmas
                if lemma.isalpha() and lemma not in stop_words]
    return ' '.join(a_lemmas)
# Funcion para remover caracteres que no son alfa numéricos
def remove_punct(text):
    removed = re.sub(r"\W", ' ', text)
    return(removed)

# Funcion para encontrar personas en el documento
def persons(text):
    doc = nlp(text)
    ne = ', '.join([(ent.text) for ent in doc.ents
          if ent.label_ == "PER"])
    return(ne)
#Funcion para encontrar organizaciones en el documento
def orgs(text):
    doc = nlp(text)
    ne = ', '.join([(ent.text) for ent in doc.ents
          if ent.label_ == "ORG"])
    return(ne)
# Funcion para convertir todos los caracteres en minusculo
def lower_text(text):
    lowered = text.lower()
    return(lowered)    
#Funcion para obtener nombres propios
def get_proper_nouns(text):
    doc = nlp(text)
    pos = ', '.join([token.text for token in doc if token.pos_ == 'PROPN'])
    return pos
# Funcion para obtener nombres
def get_nouns(text):
    doc = nlp(text)
    pos = ', '.join([token.text for token in doc if token.pos_ == 'PROPN'])
    return pos
# Funcion para remover stop words y lowercase SIN LEMATIZAR
def remove_stopwords(text):
    tokens = word_tokenize(text)
    remove = [token.lower() for token in tokens if token not in stop_words]
    return ' '.join(remove)

# Funcion para obtemer n-grams    
def get_ngrams(text, ngram_from=2, ngram_to=2, n=None, max_features=20000):
    
    vec = CountVectorizer(ngram_range = (ngram_from, ngram_to), 
                          max_features = max_features).fit(text)
    bag_of_words = vec.transform(text)
    sum_words = bag_of_words.sum(axis = 0) 
    words_freq = [(word, sum_words[0, i]) for word, i in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)
   
    return words_freq[:5] 

# Funcion para obtener los tfidf
def get_tfidf(text):
    vec = TfidfVectorizer()
    bag_of_words = vec.fit_transform(text)
    sum_words = bag_of_words.sum(axis = 0) 
    words_freq = [(word, sum_words[0, i]) for word, i in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)
   
    return words_freq[:10]

###############################################################################

df['title_preprocessed'] = df['title'].apply(preprocess)
df['title_preprocessed'] = df['title_preprocessed'].apply(lower_text)
df['persons'] = df['title'].apply(persons)
df['organizations'] = df['title'].apply(orgs)
df['nouns'] = df['title'].apply(get_nouns)

medios = pd.read_csv('medios_pr.csv')

medios['title_preprocessed'] = medios['title'].apply(preprocess)
medios['title_preprocessed'] = medios['title_preprocessed'].apply(lower_text)
medios['persons'] = medios['title'].apply(persons)
medios['organizations'] = medios['title'].apply(orgs)
medios['nouns'] = medios['title'].apply(get_nouns)
medios['proper_nouns'] = medios['title'].apply(get_proper_nouns)

newspapers = list(medios.media.unique())

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
    print(get_ngrams(x['title_preprocessed']))☺

topics = list(df.topic.unique())
for topic in topics:
    x = df[df['topic']==topic]
    print('\nLos ngrams mas comunes de {}'.format(topic))
    print(get_ngrams(x.title_preprocessed))

