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
    <title>HENRY Data Science - Proyecto Individual Data Engineer</title>
</head>
<body>
    <br>
    <h2 style="font-family: Verdana">API con información de series y películas en las plataformas de Amazon, Disney+, Hulu y Netflix</h2>
    <h3 style="font-family: Verdana">Cómo hacer las consultas:</h3>
    <br>
    <h4 style="font-family: Verdana">Para conocer la máxima duración por año, por plataforma y según tipo de film (película= min / serie= season):</h4>
    <p5 style="font-family: Verdana">/get_max_duration/AÑO/PLATAFORMA/TIPO</p5><br>
    <p5 style="font-family: Verdana">Por ej: /get_max_duration/2018/Hulu/min</p5>
    <br>
    <h4 style="font-family: Verdana">Para conocer la cantidad de películas y series por plataforma:</h4>
    <p5 style="font-family: Verdana">/get_count_platform/PLATAFORMA</p5><br>
    <p5 style="font-family: Verdana">Por ej: /get_count_platform/Amazon<p5>
    <br>
    <h4 style="font-family: Verdana">Para conocer la cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo:</h4>
    <p5 style="font-family: Verdana">/get_listedin/GENERO</p5><br>
    <p5 style="font-family: Verdana">Por ej: /get_listedin/Comedy</p5>
    <br>
    <h4 style="font-family: Verdana">Para conocer el actor/actriz con mayor número de apariciones según año y plataforma:</h4>
    <p5 style="font-family: Verdana">/get_actor/PLATAFORMA/AÑO</p5><br>
    <p5 style="font-family: Verdana">Por ej: /get_actor/Netflix/2018</p5>
    <br>
    <br>
    <h4 style="font-family: Verdana">Para volver a la página de inicio, puede hacer hacia atrás.</h4>
</body>
</html>"""

#Decorador de la primera consulta.
@app.get("/get_max_duration/{anio}/{plataforma}/{tipo}")
def get_max_Duracion(anio,plataforma,tipo):
    anio = int(anio)
    lista_plataforma = ['Amazon','Disney','Hulu','Netflix']
    lista_tipo = ['min','season']
    if (plataforma in lista_plataforma) and (tipo in lista_tipo) and (anio in range(datos.Anio_estreno.min(),datos.Anio_estreno.max()+1)):
        if tipo == 'min':
            tipo_MoS = 'Movie'
            gmd = datos[datos['Plataforma'] == plataforma][datos['Anio_estreno'] == anio][datos['Tipo'] == tipo_MoS].groupby(['Plataforma', 'Tipo', 'Anio_estreno'])['Duracion'].idxmax()
            duracion = datos['Duracion'].get(gmd[0])
            titulo = datos['Titulo'].get(gmd[0])
            return (f'El Título es {titulo} y su duración es de {duracion} {tipo}')
        elif tipo == 'season':
            tipo_MoS = 'TV Show'
            gmd = datos[datos['Plataforma'] == plataforma][datos['Anio_estreno'] == anio][datos['Tipo'] == tipo_MoS].groupby(['Plataforma', 'Tipo', 'Anio_estreno'])['Duracion'].idxmax()
            duracion = datos['Duracion'].get(gmd[0]) 
            titulo = datos['Titulo'].get(gmd[0])
            return (f'El Título es {titulo} y su duración es de {duracion} {tipo}.')
    else:
        return (f'Los parámetros ingresados son erróneos.')
    
    
    
#Decorador de la segunda consulta.
@app.get("/get_count_platform/{plataforma}")
def get_count_platform(plataforma):
    lista_plataforma = ['Amazon','Disney','Hulu','Netflix']
    if (plataforma in lista_plataforma):
        gcp = datos[datos['Plataforma'] == plataforma]
        gcp = gcp.groupby(['Plataforma'])['Tipo'].value_counts().to_dict()
        #gcp = pd.DataFrame(gcp)
        return gcp
    else:
        return (f'Los parámetros ingresados son erróneos.')



#Decorador de la tercera consulta.
@app.get("/get_listedin/{genero}")
def get_listedin(genero):
    gl = datos[datos.Genero.str.contains(genero, case=False)].groupby(by=['Plataforma']).Titulo.count()
    gl = pd.DataFrame(gl)
    gl.reset_index(inplace=True)
    gl.sort_values(by='Titulo', inplace=True, ascending=False)
    gl.reset_index(inplace=True, drop=True)
    return (f' El género {genero} se repite con mayor frecuencia en la plataforma {gl.iloc[0]} veces.')



#Decorador de la cuarta consulta.
@app.get("/get_actor/{plataforma}/{anio}")
def get_actor(plataforma,anio):
    anio = int(anio)
    lista_plataforma = ['Amazon','Disney','Hulu','Netflix']
    lista_tipo = ['min','season']
    if (plataforma in lista_plataforma) and (anio in range(datos.Anio_estreno.min(),datos.Anio_estreno.max()+1)):
        actores_lista = []
        ga = datos.query(f"Plataforma == '{plataforma}' and Anio_estreno ==  {anio}").Actores.tolist()
        for i in range(len(ga)):
            actores_temp = ga[i].split(",")
            for j in range(len(actores_temp)):
                if actores_temp[j] != 'Sin dato':
                    actores_lista.append(actores_temp[j])
        actores_dicc = dict(zip(actores_lista,map(lambda x: actores_lista.count(x),actores_lista)))
        actor_max = max(actores_dicc, key=actores_dicc.get)
        actor_max_aparece = actores_dicc.get(actor_max)
        return f'Es {actor_max} con {actor_max_aparece} apariciones.'
    else:
        return (f'Los parámetros ingresados son erróneos')