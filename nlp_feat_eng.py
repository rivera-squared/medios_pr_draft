import pandas as pd
import numpy as np
import spacy
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize
import re
# !python -m spacy download es_core_news_sm

stop_words = stopwords.words('spanish')

nlp = spacy.load('es_core_news_sm')

df = pd.read_csv('primerahora.csv')

def preprocess(text):
    # Create Doc object
    doc = nlp(text, disable=['ner','parser'])
    # Generate lemmas
    lemmas = [token.lemma_ for token in doc]
    # Remove stopwords and non-alphabetic characters
    a_lemmas = [lemma for lemma in lemmas
                if lemma.isalpha() and lemma not in stop_words]
    return ' '.join(a_lemmas)

def persons(text):
    doc = nlp(text)
    ne = ', '.join([(ent.text) for ent in doc.ents
          if ent.label_ == "PER"])
    return(ne)

def orgs(text):
    doc = nlp(text)
    ne = ', '.join([(ent.text) for ent in doc.ents
          if ent.label_ == "ORG"])
    return(ne)


def lower_text(text):
    lowered = text.lower()
    return(lowered)    

df['title_preprocessed'] = df['title'].apply(preprocess)
df['title_preprocessed'] = df['title_preprocessed'].apply(lower_text)
df['persons'] = df['title'].apply(persons)
df['organizations'] = df['title'].apply(orgs)

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

re.sub(r"\W", ' ', df['persons'][72])

def remove_punct(text):
    removed = re.sub(r"[?]", ' ', text)
    return(removed)

df['persons'] = df['persons'].apply(remove_punct)
