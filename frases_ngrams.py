from datetime import date
# Script para obtener frecuencias de ngrams en DataFrame 

# Load Data use "nlp_feat_eng.py"
# Load functions using "funciones_.py"

stop_words = stopwords.words('spanish')

newspapers = list(medios.media.unique())

palabras = ['el','la','puerto', 'rico','gobierno','tras']
stop_words.extend(palabras)

medios['date'] = pd.to_datetime(medios['date'])

medios['title_1'] = medios['title'].apply(lower_text)
medios['title_2'] = medios['title_1'].apply(remove_stopwords)
medios['title_3'] = medios['title_2'].apply(remove_punct)
#medios['week'] = medios['date'].apply(get_week)

#medios = medios[(medios['week'] >= 30) & (medios['week']<34)]

fechas = list(medios.date.unique())
for fecha in fechas:
    print(medios[medios['date'] == fecha])
    
semanas = list(medios['week'].unique())


frases_periodicos = []
for newspaper in newspapers:
    x = medios[medios['media'] == newspaper]
    x_ng = get_ngrams(x.title_3)
    x_df = pd.DataFrame(x_ng, columns = ['Frases','Frecuencias'])
    x_df['Periodico'] = newspaper
    frases_periodicos.append(x_df)
    
# Including week to the analysis    
frases_periodicos = []
for semana in semanas:
    for newspaper in newspapers:
        x = medios[(medios['week'] == semana) & (medios['media'] == newspaper)]
        x_ng = get_ngrams(x.title_3)
        x_df = pd.DataFrame(x_ng, columns = ['Frases','Frecuencias'])
        x_df['Periodico'] = newspaper
        x_df['Semana'] = semana
        frases_periodicos.append(x_df)
        
frases_periodicos = []
for fecha in fechas:
    for newspaper in newspapers:
        x = medios[(medios['date'] == fecha) & (medios['media'] == newspaper)]
        x_ng = get_ngrams(x.title_3)
        x_df = pd.DataFrame(x_ng, columns = ['Frases','Frecuencias'])
        x_df['Periodico'] = newspaper
        x_df['Fecha'] = fecha
        frases_periodicos.append(x_df)        
        

frases_periodicos = pd.concat(frases_periodicos)

frases_periodicos.to_csv('frases_periodicos.csv', index = False)

covid = medios[medios['title_3'].str.contains('covid 19', regex = False)]

covid['date'] = pd.to_datetime(covid['date'], format = "%Y-%m-%d")

covid['week'] = covid['date'].apply(get_week)

def get_week(date):
    fecha = date.week
    return(fecha)