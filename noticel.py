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

noticel=pd.read_csv('noticel.csv')
#noticel=pd.read_csv('https://raw.githubusercontent.com/edghero/media_data/main/noticel.csv')
noticel['date']=pd.to_datetime(noticel.date)

noticel_url ='https://www.noticel.com/'
sel=Selector(text=requests.get(noticel_url).content)

title=sel.xpath('//div[@class="entry-title"]/a/h2[@class="teaser__headline"]/span[@class="teaser__headline-marker"]/text()').extract()
link=sel.xpath('//div[@class="entry-title"]/a/@href').extract()
summary_strip=sel.xpath('//div[@class="teaser-content image col-md-8"]/div[@class="teaser-body"]/text()').extract()
summary=[]
for x in summary_strip:
    summary.append(x.strip())
    
date_messy=sel.xpath('//div[@class="teaser-content image col-md-8"]/div[@class="teaser-article-date"]/div[@class="teaser-article-pubdate"]/text()').extract()
date=[]
pattern='\w*\s\d{2},\s\d{4}'
for x in date_messy:
   date.append(re.findall(pattern, str(x)))

date1=[]
for x in date:
    date1.append(''.join(x))

topic_messy=sel.xpath('//div[@class="teaser-image col-md-4"]/div[@class="category_overlay"]/text()').extract()
topic=[]
for x in topic_messy:
    topic.append(x.strip())

# I found an instance wher the topic was not included in the article's interface
# Keep the following code lines as an alternate way to scrape the topic
#topic=[]    
#for x in link:
#    sel=Selector(text=requests.get(x).content)
#    topic.append(sel.xpath('//div[@class="category"]/text()').extract())
#    time.sleep(1)

sel.xpath('//div[@class="category"]/text()').extract()
noticel_ultimo=pd.DataFrame({
    'date':date1,
    'title':title,
    'summary':summary,
    'topic': topic,
    'media':'Noticel',
    'link': link})
noticel_ultimo['date']= pd.to_datetime(noticel_ultimo.date)

noticel=noticel.append(noticel_ultimo)
noticel=noticel.drop_duplicates(subset=['link'])

noticel.to_csv('noticel.csv', index=False)
