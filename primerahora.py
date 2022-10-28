# Primer intento de hacer un script para recopilar los periódicos digitales de
# Puerto Rico

# Load necessary libraries
from scrapy import Selector
import requests
import pandas as pd
import numpy as np
import os
import datetime as dt
import locale
import time


primerahora = pd.read_csv('primerahora.csv')
#primerahora=pd.read_csv('https://raw.githubusercontent.com/edghero/media_data/main/primerahora.csv')
#primerahora['media']='Primera Hora'
#primerahora=primerahora[['date','title','summary','topic','media','link']]
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # I neeed this in order to set the date  format from English to Spanish

# Primera Hora's últimas noticias link
url = 'https://www.primerahora.com/ultimas-noticias/'

html = requests.get(url).content
sel = Selector(text=html)

# Scraping titles
title = sel.xpath('//h3/text()').extract()

# Scraping link's extension
link_extension = sel.xpath('//div[@class="ListItemTeaser__column"]/a/@href').extract()
# Need to convert from list to array in order to paste the two halves of the link
link_extension=np.array(link_extension)
# Passing the link into a variable
ph = 'http://www.primerahora.com'

complete_link = [] # Creating an empty list, so I can append each iteration of pasting the 'www' and link extension together       
for link in link_extension:
    complete_link.append(ph + link)
    
# Scraping for article's topic
topic = sel.xpath('//h4[@class="ListItemTeaser__meta"]/a/text()').extract()

# Scraping for date    
date = sel.xpath('//div[@class="ListItemTeaser__date"]/text()').extract()
#date = pd.to_datetime(date, format=date_format, unit='ns')

#Scraping for article's summary
summary = sel.xpath('//p[@class="ListItemTeaser__lede"]/text()').extract()

#summary_alt=[]
#for x in complete_link:
    #sel=Selector(text=requests.get(x).content)
    #summary_alt.append(sel.xpath('//section[@class="ArticleBody"]/p/text()').extract_first())

#Creating a DataFrame
primerahora_test = pd.DataFrame({
 'date':date,
 'title':title,
 'summary':summary,
 'topic':topic,
 'media':'Primera Hora',
 'link':complete_link})

#primerahora_test['date'] = '2022-09-01'
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # I neeed this in order to set the date  format from English to Spanish
date_format = '%d / %b / %Y' # This is needed in order to convert dates
primerahora_test['date'] = pd.to_datetime(primerahora_test.date, format = date_format) #Changing the date format
primerahora = primerahora.append(primerahora_test) # Appending new data to the old one
primerahora['date'] = pd.to_datetime(primerahora.date) # Reformat dates
primerahora=primerahora.drop_duplicates() #Dropping duplicates

primerahora.to_csv('primerahora.csv', index=False)


    