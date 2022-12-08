from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
import re

#IMPORTACIÓN DE CSV
datos = pd.read_csv('./base_plataformas.csv', engine='python', decimal='.')

app = FastAPI()


#DECORADOR INDEX
@app.get("/",response_class=HTMLResponse)
async def index():
    return """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HENRY Data Science - Proyecto Individual Data Enginering</title>
</head>
<body>
    <h1>Guía de Usuario de la API</h1>
    <h3>/get_max_duration/AÑO/PLATAFORMA/TIPO Por ej: /get_max_duration/2020/netflix/min</h3>
    <p>Devuelve la película/serie con mayor duración por plataforma, año y tipo de duración (min o seasons).</p>
    <h3>/get_count_platform/PLATAFORMA Por ej: /get_count_platform/disney</h3>
    <p>Devuelve la cantidad de películas y de series por plataforma</p>
    <h3>/get_listedin/GENERO Por ej: /get_listedin/comedy</h3>
    <p>Devuelve la cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.</p>
    <h3>/get_actor/PLATAFORMA/AÑO Por ej: /get_actor/amazon/2020</h3>
    <p>Devuelve al actor/actriz con mayor número de apariciones según año y plataforma.</p>
    <h3>Luego de realizar alguna consulta, si desea volver a esta guía, elimine los decoradores.</h3>
</body>
</html>"""

#Decorador de la primera consulta.
@app.get("/get_max_duration/{anio}/{plataforma}/{tipo}")
def get_max_Duracion(Plataforma,año,tipo):
    if tipo == 'min':
        t = 'Movie'
        g = datos[datos['Plataforma'] == Plataforma][datos['Anio_estreno'] == año][datos['Tipo'] == t].groupby(['Plataforma', 'Tipo', 'Anio_estreno'])['Duracion'].idxmax()
        duracion = datos['Duracion'].get(g[0])
        titulo = datos['Titulo'].get(g[0])
        return (f'El Título es {titulo} y su duración es de {duracion} {tipo}')
    elif tipo == 'season':
        t = 'TV Show'
        g = datos[datos['Plataforma'] == Plataforma][datos['Anio_estreno'] == año][datos['Tipo'] == t].groupby(['Plataforma', 'Tipo', 'Anio_estreno'])['Duracion'].idxmax()
        duracion = datos['Duracion'].get(g[0]) 
        titulo = datos['Titulo'].get(g[0])
        return (f'El Título es {titulo} y su duración es de {duracion} {tipo}')