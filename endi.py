# Load necessary libraries
from scrapy import Selector
import requests
import pandas as pd
import numpy as np
import os
import datetime as dt
import locale
import time
import re


endi=pd.read_csv('endi.csv')
#endi=pd.read_csv('https://raw.githubusercontent.com/edghero/media_data/main/endi.csv')
endi['date']=pd.to_datetime(endi.date)


endi_url ='https://www.elnuevodia.com'
url='https://www.elnuevodia.com/ultimas-noticias/'

sel=Selector(text=requests.get(url).content)

title=sel.xpath('//h1[@class="story-tease-title"]/*/text()').extract()[0:10] #Titulo
topic=sel.xpath('//div[@class="story-tease-body"]/span[@class="story-tease-category"]/a/text()').extract() #Topic
summary=sel.xpath('//div[@class="story-tease-summary"]/p/text()').extract() # Summary
date_messy=sel.xpath('//p[@class="story-tease-date"]/text()').extract()

pattern = '\d+\s\w{2}\s\w+\s\w{2}\s\d{4}'
date_messy_2=[]
for x in date_messy:
    date_messy_2.append(np.array(re.findall(pattern,str(x))))

date_messy_3 = []
for x in date_messy_2:
    date_messy_3.append(re.sub('(de)','', str(x)))

DATE=[]
for x in date_messy_3:
     DATE.append(str(x)[1:-1])  

date=[]
for x in DATE:
    date.append((re.sub("'", '', x)))

complete_link=[]    
link_extension=sel.xpath('//h1[@class="story-tease-title"]/a/@href').extract()[0:10]
for x in link_extension:
    complete_link.append(endi_url+x)
    
endi_ultimo=pd.DataFrame({
    'date':date,
    'title':title,
    'summary':summary,
    'topic':topic,
    'media':'El Nuevo Dia',
    'link':complete_link})
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') 
date_format='%d %B %Y'
endi_ultimo['date']=pd.to_datetime(endi_ultimo.date, format=date_format)

endi=endi.append(endi_ultimo)
endi=endi.drop_duplicates(subset=['link'])

endi.to_csv('endi.csv',index=False)
    