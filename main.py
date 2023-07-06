from fastapi import FastAPI
import pandas as pd
import io
import json
import re
from datetime import datetime
import requests
from typing import List
from io import StringIO
from fastapi import FastAPI
import uvicorn
import ast

url = "https://raw.githubusercontent.com/NicolasTablon/Proyecto_Individual2/main/Csv_Proyecto_Terminado.csv"

response = requests.get(url)
response.raise_for_status()

df= pd.read_csv(io.BytesIO(response.content), encoding="UTF-8", delimiter=",", error_bad_lines=False)

# Crear una instancia de FastAPI
app = FastAPI()
@app.get('/peliculas_duracion')
def peliculas_duracion(pelicula: str):
    pelicula_encontrada = df[df["title"] == pelicula]
    if not pelicula_encontrada.empty:
        duracion = pelicula_encontrada["runtime"].values[0]
        año = pelicula_encontrada["anio"].values[0]
        return f"{pelicula}. Duración: {duracion}. Año: {año}"
    else:
        return "Película no encontrada"
        
@app.get('/franquicia')
def franquicia(franquicia: str):
    # Filtrar el DataFrame para obtener las películas de la franquicia solicitada
    peliculas_franquicia = df[df['production_companies'] == franquicia]

    # Obtener la cantidad de películas de la franquicia
    cantidad_peliculas = len(peliculas_franquicia)

    # Calcular la ganancia total y promedio de la franquicia
    ganancia_total = peliculas_franquicia['revenue'].sum()
    ganancia_promedio = peliculas_franquicia['revenue'].mean()

    # Devolver la respuesta en el formato requerido
    return f"La franquicia {franquicia} posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}"


    
@app.get('/peliculas_idioma')
def peliculas_idioma(idioma: str):
    cantidad_peliculas = sum(1 for _, pelicula in df.iterrows() if isinstance(pelicula["spoken_languages"], str) and idioma in pelicula["spoken_languages"])
    return f"{cantidad_peliculas} cantidad de películas fueron estrenadas en {idioma}"
    
@app.get('/peliculas_pais')    
def peliculas_pais(pais: str):
    # Filtrar el DataFrame para obtener las películas del país solicitado
    peliculas_pais = df[df['production_countries'].str.contains(pais, na=False)]

    # Obtener la cantidad de películas del país
    cantidad_peliculas = len(peliculas_pais)

    # Devolver la respuesta en el formato requerido
    return f"Se produjeron {cantidad_peliculas} películas en el país {pais}"


    
@app.get('/productoras_exitosas')
def productoras_exitosas(productora: str):
    peliculas_productora = df[df["production_companies"].str.contains(productora, na=False)]
    cantidad_peliculas = len(peliculas_productora)
    revenue_total = peliculas_productora["revenue"].sum()
    return f"La productora {productora} ha tenido un revenue de {revenue_total} y ha realizado {cantidad_peliculas} películas"

@app.get("/director/{director}")
def get_director(director: str):
    # Creamos un dataset nuevo aplicando el filtro del director y que no este vacio
    df1 = df[df['director'].notna() & df['director'].str.contains(director)]
    # Sumamos los retornos del director
    retorno_dir = df1['return'].sum() 
    cantidad_peliculas = df1.shape[0]    
    data = {
        "director": director,
        "retorno del director": retorno_dir,
        "total de peliculas dirigidas": cantidad_peliculas,
        "peliculas": [{
            "titulo": df1["title"].tolist(),
            "estreno": df1["release_date"].tolist(),
            "retorno": df1["return"].tolist(),
            "presupuesto": df1["budget"].tolist(),
            "ganancias": df1["earns"].tolist(),
        }]
    }
    # Convert the data dictionary to a JSON string with proper indentation
    json_data = json.dumps(data, indent=4)    
    # Create a response object with the JSON data and the appropriate media type
    response = Response(content=json_data, media_type="application/json")
    return response

    
@app.get('/recomendacion')
async def recomendacion(titulo: str):
    # Convertir el título proporcionado a minúsculas
    titulo = titulo.lower()

    # Obtener la fila correspondiente al título proporcionado
    pelicula = df.loc[df['title'].str.lower() == titulo]

    if pelicula.empty:
        return []

    # Obtener la puntuación de la película
    puntuacion = pelicula['vote_average'].values[0]

    # Encontrar películas similares según la puntuación
    peliculas_similares = df.loc[df['vote_average'] >= puntuacion].sort_values('vote_average', ascending=False)

    # Obtener los títulos de las 5 películas con puntuacion mas similar
    recomendaciones = peliculas_similares['title'].head(5).tolist()

    return recomendaciones

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

   
