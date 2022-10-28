import pandas as pd

medios_pr=pd.read_csv('medios_pr.csv')
endi=pd.read_csv('endi.csv')
vocero=pd.read_csv('vocero.csv')
noticel=pd.read_csv('noticel.csv')
primerahora=pd.read_csv('primerahora.csv')


medios_pr=medios_pr.append(endi)
medios_pr=medios_pr.append(noticel)
medios_pr=medios_pr.append(primerahora)
medios_pr=medios_pr.append(vocero)

medios_pr=medios_pr.drop_duplicates(subset=['link'])

medios_pr.to_csv('medios_pr.csv', index=False)

#Experimenting a little bit
medios_pr.columns
medios_pr[medios_pr['topic'] == "Tribunales"]
media_day=medios_pr.groupby(['date','media']).count()