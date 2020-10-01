import requests
from bs4 import BeautifulSoup
import pandas as pd

result = requests.get("https://resultados.as.com/resultados/baloncesto/nba/clasificacion/")

src = result.content

soup= BeautifulSoup(src, 'html.parser')

eq= soup.find_all('span',class_='nombre-equipo')

equipos = list()

for i in eq:
    equipos.append(i.text)

ptos=soup.find_all('td', class_='hidden-xs')

puntos=list()

for i in ptos:
    
    puntos.append(i.text)

puntosfinal = puntos[0::3]



df= pd.DataFrame({'Nombre': equipos, 'Puntos': puntosfinal} )

print(df)