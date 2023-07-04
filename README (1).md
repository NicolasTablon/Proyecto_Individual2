
# Proyecto Individual N°1

Machine Learning Operations (MLOps)

Henry's Labs
Por Nicolás Tablón (DTS-11)

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

•	def cantidad_filmaciones_mes( Mes ): Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
                   
•	def cantidad_filmaciones_dia( Dia ): Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
                    
•	def score_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
                    
•	def votos_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.

 •	def get_actor( nombre_actor ): Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno. La definición no deberá considerar directores.
                    
•	def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.


## Etapa del Sistema de Recomendación ➡️


•	def recomendacion( titulo ): Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores

