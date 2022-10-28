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

# Upload dataframe
vocero = pd.read_csv('vocero.csv')
vocero=pd.read_csv('https://raw.githubusercontent.com/edghero/media_data/main/vocero.csv')
#vocero['media']='El Vocero'
#vocero=vocero[['date','title','summary','topic','media','link']]



########################################################################
# "Ley y orden" section
url_lo = 'https://www.elvocero.com/ley-y-orden/'
html_lo = requests.get(url_lo).content
sel_lo = Selector(text=html_lo)

# Scraping link
complete_link_lo = []
link_lo = 'https://www.elvocero.com'

link_extension_lo=sel_lo.xpath('//h3[@class="tnt-headline "]/a/@href').extract()
link_extension_lo=np.array(link_extension_lo)

# For loop to concanate link and its extension
for x in link_extension_lo:
    complete_link_lo.append(link_lo + x)

complete_link_lo=np.array(complete_link_lo)

# Scraping for title
title_lo=sel_lo.xpath('//h3[@class="tnt-headline "]/a/text()').extract() 

# Eliminate newline (\n) from the title
title_LO=[]
for x in title_lo:
    title_LO.append(x.strip())
    
#Scraping for date and summary
summary_lo_ART =[]
date_lo_ART =[]

for x in complete_link_lo:
    sel=Selector(text=requests.get(x).content)
    date_lo_ART.append(sel.xpath('//li[@class="hidden-print"]/time/@datetime').extract())
    summary_lo_ART.append(sel.xpath('//h2[@class="subhead"]/span/text()').extract())
    time.sleep(1)
#Althouth the previous lines of codes successfully scraped the article's summary and date,
#it does so in a list and in need of some data cleaning. As reader, the user will find the information useful but, from a coding perspective,
#it will create headaches as one will want to use other functions and commands in the future.

summary_lo_final=[]
for x in summary_lo_ART:
    summary_lo_final.append(''.join(x))

# The following lines of code will use regex to extract only the yyyy-mm-dd of each list
pattern = '\d{4}-\d{2}-\d{2}'
date_lo_ART_fixed=[]

for x in date_lo_ART:
    date_lo_ART_fixed.append(re.findall(pattern, str(x)))

# The following lines of code will convert the string into a datetime format
date_format = '%Y-%m-%d'  
date_lo_final=[]
for x in date_lo_ART_fixed:
    date_lo_final.append((pd.to_datetime(''.join(x), format=date_format)))
    

           
#Now I have all the columns ready to create a DataFrame

vocero_lo=pd.DataFrame({
    #'date':date_lo_ART_fixed,
    'date':date_lo_final,
    'title':title_LO,
    'summary':summary_lo_final,
    'topic': 'Ley y Orden',
    'media':'El Vocero',
    'link':complete_link_lo})

########################################################################

########################################################################
# "Gobierno" section

url_go = 'https://www.elvocero.com/gobierno/'
sel_go = Selector(text=requests.get(url_go).content)

# Scraping link
complete_link_go = []
link_go = 'https://www.elvocero.com'

link_extension_go=sel_go.xpath('//h3[@class="tnt-headline "]/a/@href').extract()
link_extension_go=np.array(link_extension_go)

# For loop to concanate link and its extension
for x in link_extension_go:
    complete_link_go.append(link_go + x)

complete_link_go=np.array(complete_link_go)

# Scraping for title
title_go=sel_go.xpath('//h3[@class="tnt-headline "]/a/text()').extract() 

# Eliminate newline (\n) from the title
title_GO=[]
for x in title_go:
    title_GO.append(x.strip())
    
#Scraping for date and summary
summary_go_ART =[]
date_go_ART =[]

for x in complete_link_go:
    sel=Selector(text=requests.get(x).content)
    date_go_ART.append(sel.xpath('//li[@class="hidden-print"]/time/@datetime').extract())
    summary_go_ART.append(sel.xpath('//h2[@class="subhead"]/span/text()').extract())
    time.sleep(1)
#Althouth the previous lines of codes successfully scraped the article's summary and date,
#it does so in a list and in need of some data cleaning. As reader, the user will find the information useful but, from a coding perspective,
#it will create headaches as one will want to use other functions and commands in the future.

summary_go_final=[]
for x in summary_go_ART:
    summary_go_final.append(''.join(x))

# The following lines of code will use regex to extract only the yyyy-mm-dd of each list
pattern = '\d{4}-\d{2}-\d{2}'
date_go_ART_fixed=[]

for x in date_go_ART:
    date_go_ART_fixed.append(re.findall(pattern, str(x)))

# The following lines of code will convert the string into a datetime format
date_format = '%Y-%m-%d'  
date_go_final=[]
for x in date_go_ART_fixed:
    date_go_final.append((pd.to_datetime(''.join(x), format=date_format)))
    
           
#Now I have all the columns ready to create a DataFrame

vocero_go=pd.DataFrame({
    'date':date_go_final,
    'title':title_GO,
    'summary':summary_go_final,
    'topic': 'Gobierno',
    'media':'El Vocero',
    'link':complete_link_go})

########################################################################

########################################################################
# "Deportes" section

url_dep = 'https://www.elvocero.com/deportes/'
sel_dep = Selector(text=requests.get(url_dep).content)

# Scraping link
complete_link_dep = []
link_dep = 'https://www.elvocero.com'

link_extension_dep=sel_dep.xpath('//h3[@class="tnt-headline "]/a/@href').extract()
link_extension_dep=np.array(link_extension_dep)

# For loop to concanate link and its extension
for x in link_extension_dep:
    complete_link_dep.append(link_dep + x)

complete_link_dep=np.array(complete_link_dep)

# Scraping for title
title_dep=sel_dep.xpath('//h3[@class="tnt-headline "]/a/text()').extract() 

# Eliminate newline (\n) from the title
title_DEP=[]
for x in title_dep:
    title_DEP.append(x.strip())
    
#Scraping for date and summary
summary_dep_ART =[]
date_dep_ART =[]

for x in complete_link_dep:
    sel=Selector(text=requests.get(x).content)
    date_dep_ART.append(sel.xpath('//li[@class="hidden-print"]/time/@datetime').extract())
    summary_dep_ART.append(sel.xpath('//h2[@class="subhead"]/span/text()').extract())
    time.sleep(1)
#Althouth the previous lines of codes successfully scraped the article's summary and date,
#it does so in a list and in need of some data cleaning. As reader, the user will find the information useful but, from a coding perspective,
#it will create headaches as one will want to use other functions and commands in the future.

summary_dep_final=[]
for x in summary_dep_ART:
    summary_dep_final.append(''.join(x))

# The following lines of code will use regex to extract only the yyyy-mm-dd of each list
pattern = '\d{4}-\d{2}-\d{2}'
date_dep_ART_fixed=[]

for x in date_dep_ART:
    date_dep_ART_fixed.append(re.findall(pattern, str(x)))

# The following lines of code will convert the string into a datetime format
date_format = '%Y-%m-%d'  
date_dep_final=[]
    
for x in date_dep_ART_fixed:
    date_dep_final.append((pd.to_datetime(''.join(x), format=date_format)))
           
#Now I have all the columns ready to create a DataFrame

vocero_dep=pd.DataFrame({
    'date':date_dep_final,
    'title':title_DEP,
    'summary':summary_dep_final,
    'topic': 'Deportes',
    'media':'El Vocero',
    'link':complete_link_dep})

########################################################################

########################################################################
# "Economia" section

url_eco = 'https://www.elvocero.com/economia/'
sel_eco = Selector(text=requests.get(url_eco).content)

# Scraping link
complete_link_eco = []
link_eco = 'https://www.elvocero.com'

link_extension_eco=sel_eco.xpath('//h3[@class="tnt-headline "]/a/@href').extract()
link_extension_eco=np.array(link_extension_eco)

# For loop to concanate link and its extension
for x in link_extension_eco:
    complete_link_eco.append(link_eco + x)

complete_link_eco=np.array(complete_link_eco)

# Scraping for title
title_eco=sel_eco.xpath('//h3[@class="tnt-headline "]/a/text()').extract() 

# Eliminate newline (\n) from the title
title_ECO=[]
for x in title_eco:
    title_ECO.append(x.strip())
    
#Scraping for date and summary
summary_eco_ART =[]
date_eco_ART =[]

for x in complete_link_eco:
    sel=Selector(text=requests.get(x).content)
    date_eco_ART.append(sel.xpath('//li[@class="hidden-print"]/time/@datetime').extract())
    summary_eco_ART.append(sel.xpath('//h2[@class="subhead"]/span/text()').extract())
    time.sleep(1)
#Althouth the previous lines of codes successfully scraped the article's summary and date,
#it does so in a list and in need of some data cleaning. As reader, the user will find the information useful but, from a coding perspective,
#it will create headaches as one will want to use other functions and commands in the future.

summary_eco_final=[]
for x in summary_eco_ART:
    summary_eco_final.append(''.join(x))

# The following lines of code will use regex to extract only the yyyy-mm-dd of each list
pattern = '\d{4}-\d{2}-\d{2}'
date_eco_ART_fixed=[]

for x in date_eco_ART:
    date_eco_ART_fixed.append(re.findall(pattern, str(x)))

# The following lines of code will convert the string into a datetime format
date_format = '%Y-%m-%d'  
date_eco_final=[]
    
for x in date_eco_ART_fixed:
    date_eco_final.append((pd.to_datetime(''.join(x), format=date_format)))
           
#Now I have all the columns ready to create a DataFrame

vocero_eco=pd.DataFrame({
    'date':date_eco_final,
    'title':title_ECO,
    'summary':summary_eco_final,
    'topic': 'Economia',
    'media':'El Vocero',
    'link':complete_link_eco})

########################################################################

########################################################################
# "Escenario" section

url_esc = 'https://www.elvocero.com/escenario/'
sel_esc = Selector(text=requests.get(url_esc).content)

# Scraping link
complete_link_esc = []
link_esc = 'https://www.elvocero.com'

link_extension_esc=sel_esc.xpath('//h3[@class="tnt-headline "]/a/@href').extract()
link_extension_esc=np.array(link_extension_esc)

# For loop to concanate link and its extension
for x in link_extension_esc:
    complete_link_esc.append(link_esc + x)

complete_link_esc=np.array(complete_link_esc)

# Scraping for title
title_esc=sel_esc.xpath('//h3[@class="tnt-headline "]/a/text()').extract() 

# Eliminate newline (\n) from the title
title_ESC=[]
for x in title_esc:
    title_ESC.append(x.strip())
    
#Scraping for date and summary
summary_esc_ART =[]
date_esc_ART =[]

for x in complete_link_esc:
    sel=Selector(text=requests.get(x).content)
    date_esc_ART.append(sel.xpath('//li[@class="hidden-print"]/time/@datetime').extract())
    summary_esc_ART.append(sel.xpath('//h2[@class="subhead"]/span/text()').extract())
    time.sleep(1)
#Althouth the previous lines of codes successfully scraped the article's summary and date,
#it does so in a list and in need of some data cleaning. As reader, the user will find the information useful but, from a coding perspective,
#it will create headaches as one will want to use other functions and commands in the future.

summary_esc_final=[]
for x in summary_esc_ART:
    summary_esc_final.append(''.join(x))

# The following lines of code will use regex to extract only the yyyy-mm-dd of each list
pattern = '\d{4}-\d{2}-\d{2}'
date_esc_ART_fixed=[]

for x in date_esc_ART:
    date_esc_ART_fixed.append(re.findall(pattern, str(x)))

# The following lines of code will convert the string into a datetime format
date_format = '%Y-%m-%d'  
date_esc_final=[]
    
for x in date_esc_ART_fixed:
    date_esc_final.append((pd.to_datetime(''.join(x), format=date_format)))
           
#Now I have all the columns ready to create a DataFrame

vocero_esc=pd.DataFrame({
    'date':date_esc_final,
    'title':title_ESC,
    'summary':summary_esc_final,
    'topic': 'Escenario',
    'media':'El Vocero',
    'link':complete_link_esc})

########################################################################

########################################################################
# "Opinion" section

url_op = 'https://www.elvocero.com/opinion/'
sel_op = Selector(text=requests.get(url_op).content)

# Scraping link
complete_link_op = []
link_op = 'https://www.elvocero.com'

link_extension_op=sel_op.xpath('//h3[@class="tnt-headline "]/a/@href').extract()
link_extension_op=np.array(link_extension_op)

# For loop to concanate link and its extension
for x in link_extension_op:
    complete_link_op.append(link_esc + x)

complete_link_op=np.array(complete_link_op)

# Scraping for title
title_op=sel_op.xpath('//h3[@class="tnt-headline "]/a/text()').extract() 

# Eliminate newline (\n) from the title
title_OP=[]
for x in title_op:
    title_OP.append(x.strip())
    
summary_op=sel_op.xpath('//p[@class="tnt-summary"]/text()').extract()    
    
#Scraping for date and summary
summary_op_ART =[]
date_op_ART =[]

for x in complete_link_op:
    sel=Selector(text=requests.get(x).content)
    date_op_ART.append(sel.xpath('//li[@class="hidden-print"]/time/@datetime').extract())
    summary_op_ART.append(sel.xpath('//h2[@class="subhead"]/span/text()').extract())
    time.sleep(1)
#Althouth the previous lines of codes successfully scraped the article's summary and date,
#it does so in a list and in need of some data cleaning. As reader, the user will find the information useful but, from a coding perspective,
#it will create headaches as one will want to use other functions and commands in the future.

summary_op_final=[]
for x in summary_op_ART:
    summary_op_final.append(''.join(x))

# The following lines of code will use regex to extract only the yyyy-mm-dd of each list
pattern = '\d{4}-\d{2}-\d{2}'
date_op_ART_fixed=[]

for x in date_op_ART:
    date_op_ART_fixed.append(re.findall(pattern, str(x)))

# The following lines of code will convert the string into a datetime format
date_format = '%Y-%m-%d'  
date_op_final=[]
    
for x in date_op_ART_fixed:
    date_op_final.append((pd.to_datetime(''.join(x), format=date_format)))
           
#Now I have all the columns ready to create a DataFrame

vocero_op=pd.DataFrame({
    'date':date_op_final,
    'title':title_OP,
    'summary':summary_op,
    'topic': 'Opinion',
    'media':'El Vocero',
    'link':complete_link_op})

########################################################################

vocero=vocero.append(vocero_lo)
vocero=vocero.append(vocero_go)
vocero=vocero.append(vocero_dep)
vocero=vocero.append(vocero_eco)
vocero=vocero.append(vocero_esc)
vocero=vocero.append(vocero_op)
vocero['date'] = pd.to_datetime(vocero.date) #Format date column as datetime
vocero=vocero.drop_duplicates(subset=['link'])

vocero.to_csv('vocero.csv', index=False)




