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

res = r.get('https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports')

if res.status_code != 200:
    raise('Algo salio mal topo')

links = lg.Links('https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports')
jsonLinks = links.find(duplicates = False)
jsonLinks = r'{'+str(jsonLinks)+r'}'

# OPCION Regex
#linkRegex = re.compile(r'/docs/default-source/coronaviruse/situation-reports(.*)')
#mo = linkRegex.search(str(jsonLinks))
#linkString=mo.group(1)
#print(linkString)


#Necesito una lista de JSONS si o si SINO PINCHA LOAD


inputJson = json.loads(jsonLinks)
outputJson = [x for x in inputJson if ('/docs/default-source/coro' in x['href'] )]
outputJson = json.dumps(outputJson, ensure_ascii = False).encode('utf-8')
s = outputJson.decode()


#urllib.request.urlretrieve(urlPdf, 'just-a-file.pdf')
#urlPdf = https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200406-sitrep-77-covid-19.pdf?sfvrsn=21d1e632_2
#/docs/default-source/coronaviruse/situation-reports/20200406-sitrep-77-covid-19.pdf?sfvrsn=21d1e632_2
