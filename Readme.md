# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

## **Introducción**

Este proyecto busca poner a prueba las habilidades adquiridas y desarrolladas a lo largo de la cursada de en la carrera de Data Science en Henry.

Como estudiante debo destacar el nivel de código requerido, además de las habilidades de búsqueda e interpretación de código requeridas para el desarrollo de cada una de sus etapas.

## **Objetivo del Proyecto**

El objetivo del Proyecto es simular el entorno de trabajo de un Data Engineer, debiendo realizar tareas inherentes al puesto. Aplicar criterio para realizar el EDA y la utilización de las herramientas. Desarrollar un código prolijo, ordenado, eficiente y comentado.
Desarrollar habilidades de aprendizaje en el uso de APIs, Docker y el deployment en Mogenius.
Todo lo anterior dentro del marco de tiempo de una semana laboral, debiendo respetar lineamientos para la entrega y posterior presentación de los resultados.

## **Trabajo realizado**

Fueron provistos los listados de cuatro plataformas de streaming (Amazon, Disney+, Hulu y Netflix), debiendo realizar las tareas propias del EDA: analizar la composición de cada una, realizar una limpieza de datos innecesarios, normalizar los datos y agruparlas en una única tabla diferenciando la plataforma de procedencia de cada dato.

Luego se debieron realizar funciones capaces de responder cuantro consultas, pudiendo extraer así información de los datos.
Las consultas fueron:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  
    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
  El request debe ser: get_actor(plataforma, año)

La última etapa consistió en crear una API que corra localmente con Uvicorn y luego ingestarla dentro de un contenedor de Docker.
Como desafío adicional, se propuso realizar el deployment en Mogenius, obteniendo un acceso web a la API. 

## **Contenido del repositorio**

La raiz del contenedor está compuesta por un archivo con las consignas del Proyecto, un notebook con el código del EDA y otro con el código de las consultas, además de dos carpetas:
- Datasets: contiene los archivos originales con los datos de cada plataforma.
- app: contiene los archivos de Docker.