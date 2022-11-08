# Script para funciones

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

# Funcion para obtener verbos
def get_verbs(text):
    doc = nlp(text)
    pos = ', '.join([token.text for token in doc if token.pos_ == 'VERB'])
    return pos

# Funcion para remover stop words y lowercase SIN LEMATIZAR

def remove_stopwords(text):
    tokens = word_tokenize(text)
    remove = [token for token in tokens if token not in stop_words]
    return ' '.join(remove)

# Funcion para obtemer n-grams    
def get_ngrams(text, ngram_from=2, ngram_to=2, n=None, max_features=20000):
    
    vec = CountVectorizer(ngram_range = (ngram_from, ngram_to), 
                          max_features = max_features).fit(text)
    bag_of_words = vec.transform(text)
    sum_words = bag_of_words.sum(axis = 0) 
    words_freq = [(word, sum_words[0, i]) for word, i in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)
   
    return words_freq[:10] 

# Funcion para obtener los tfidf
def get_tfidf(text):
    vec = TfidfVectorizer()
    bag_of_words = vec.fit_transform(text)
    sum_words = bag_of_words.sum(axis = 0) 
    words_freq = [(word, sum_words[0, i]) for word, i in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)
   
    return words_freq[:30]

def get_week(date):
    fecha = date.week
    return(fecha)