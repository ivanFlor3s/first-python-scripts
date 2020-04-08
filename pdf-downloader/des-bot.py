# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:41:40 2020

@author: Ivan
"""
import urllib.request
import requests as r
import linkGrabber as lg
import re
import json
import os
import logging
import bs4

logging.basicConfig(filename ='logout.txt',level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s') 


FILENAME= 'covid-file.pdf'

#Valido si ya existe el archivo
if os.path.exists(FILENAME):
    os.remove(FILENAME)
    logging.debug('Se actualizo el arhivo PDF')

res = r.get('https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports')

if res.status_code != 200:
    raise('Algo salio mal topo')
    
    
soup = bs4.BeautifulSoup(res.text, 'lxml')

list= []

for link in soup.find_all('a', href = True):
    if '/docs/default-source/coronaviruse/situation-reports' in link['href']:
        list.append(link['href'])

urlPdf ='https://www.who.int' + list[0]

# Descargo el PDF
urllib.request.urlretrieve(urlPdf, FILENAME)


#Login del enlace que estoy descargando
covidRegex = re.compile(r'\d\d\d\d\d\d\d\d-sitrep-\d\d-covid-\d\d')
mo = covidRegex.search(list[0])
logging.critical('Se trae info del link: ' + mo.group())



#FALOPA PURA LO DE ABAJO ------------------------------------------------------------------------------
        
#links = lg.Links('https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports')
#jsonLinks = links.find(duplicates = False)

#Corrijo el JSON para reemplazar ' con "
#correctJson= re.compile(r"'")
#jsonLinks = correctJson.sub(r'"',str(jsonLinks))

# OPCION Regex
#linkRegex = re.compile(r'/docs/default-source/coronaviruse/situation-reports(.*)')
#mo = linkRegex.search(str(jsonLinks))
#linkString=mo.group(1)
#print(linkString)

#OPCION JSON de mierda
# JSON crudo
#jsonLinks = "%r"%jsonLinks

#inputJson = json.loads(jsonLinks)
#outputJson = [x for x in inputJson if ('/docs/default-source/coro' in x['href'] )]
#outputJson = json.dumps(outputJson, ensure_ascii = False).encode('utf-8')
#s = outputJson.decode()



#urlPdf = https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200406-sitrep-77-covid-19.pdf?sfvrsn=21d1e632_2
#/docs/default-source/coronaviruse/situation-reports/20200406-sitrep-77-covid-19.pdf?sfvrsn=21d1e632_2
