# RegEx Practice
import pandas as pd
import numpy as np
import re
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
from collections import Counter
from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary

endi=pd.read_csv('endi.csv')
 
endi_luma=endi[endi.title.str.contains('LUMA')]

#word_tokenized=[word_tokenize(word) for word in endi_luma.summary]

# Obtain the text data
luma_1=endi_luma['summary'].iloc[1,] # Selecting just one article's summary
luma_resumenes = '   '.join(endi_luma['summary']) #joins all articles' summaries into a single string

#Tokenize words
luma_1_token = word_tokenize(luma_resumenes)
# Convert tokens into lowercase
luma_1_lower = [w for w in word_tokenize(luma_resumenes.lower())
          if w.isalpha()]
# Remove stopwords (Spanish)
luma_no_stops =[t for t in luma_1_lower
                if t not in stopwords.words('spanish')]

#Create a counter with lower case
bow_luma = Counter(luma_no_stops)

# Print the 3 most common tokens
print(bow_luma.most_common(10))

dictionary=Dictionary(luma_no_stops)


### Using gensim

#Iteration to convert to lowercase and tokenize every word of records for endi_luma['summary']

sent_token = [word_tokenize(x.lower()) for x in endi_luma['summary']]

#Creating a Dictionary from the articles
dictionary=Dictionary(sent_token)
#Select the id for "plantas"
dictionary.token2id.get('plantas')
# Creating a corpus
corpus=[dictionary.doc2bow(x) for x in sent_token]

bow_doc=sorted(corpus, key=lambda w: w[1], reverse=True)

# Print the top 5 words of the document alongside the count
for word_id, word_count in bow_doc[:2]:
    print(dictionary.get(word_id), word_count)