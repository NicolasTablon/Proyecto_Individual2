
# Proyecto Individual N°1

Machine Learning Operations (MLOps)

Henry's Labs
Por Nicolás Tablón (DTS-12)

## ESTRUCTURA DEL PROYECTO ⚪
Los principales archivos desarrollados (que en el apartado siguiente se describirán en forma detallada y precisa su contenido, son:

•	ETL.ipynb
•	APIS.ipynb
•	main.py

## DESARROLLO DE LA SOLUCIÓN (PROYECTO) ⚪
1. Etapa del proceso ETL ➡️
•	Cargamos el archivos csv con la libereria pandas.

•	Luego hacemos todo el trabajo ETL(Extract,Transform,Load)

•	Pasamos los valores nulos o vacios de 'revenue' con 0 y igualmente lo hacemos con la columna 'budget'.

•	Reordenamos el orden de fecha como nos piden al formato '%Y-%m-%d'.

•	Separamos el año a una nueva columna que la llamaremos release_year.

•	Desanidamos por el valor que queremos necesarios de las columnas 'genres', 'belongs_to_collection', 'production_companies' 'production_countries', 'spoken_languages'

•	En una nueva columna que la llamaremos return sacar el resultado de la division entre las columnas revenue y budget.

•	Eliminamos las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,poster_path y homepage.

•	En una nueva columna tengo que sacar el nombre del mes que tengo en la columna release_date, que lo pondremos en la columna reléase_month y igualmente hacemos con los dias de la semana que la pondremos en la columna que llamaremos reléase_day y creamos también dia_espanol.

•	En la columna 'dia_espanol' tengo miércoles y sábado con tildes, le quitaremos las tildes para que nos pueda funcionar.

•	Y por ultimo lo exportamos para hacer las APIS.
## Etapa de desarrollo API ➡️
Debemos crear 6 funciones para los endpoints que se consumirán en la API

•	def peliculas_idioma( Idioma: str ): Se ingresa un idioma . Debe devolver la cantidad de películas producidas en ese idioma..
                   
•	def peliculas_duracion( Pelicula: str ): Se ingresa una pelicula. Debe devolver la duracion y el año.
                    
• def franquicia( Franquicia: str ): Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
                    
•	def peliculas_pais( Pais: str ): Se ingresa un país , retornando la cantidad de peliculas producidas en el mismo.

 •	def productoras_exitosas( Productora: str ): Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.
                    
•	def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.


## Etapa del Sistema de Recomendación ➡️


•	def recomendacion( titulo ): Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores

