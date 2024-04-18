# Manejar la cadena de bases de datos SQL
from langchain_experimental.sql import SQLDatabaseChain
# Para manejar el modelo de lenguaje
from langchain.chat_models import ChatOpenAI
import os
# Establecer la clave de la API de OpenAI
import API
# Manejar la base de datos SQL
from langchain.sql_database import SQLDatabase

# Creamos una variable para instancia nuestra base de datos
db = SQLDatabase.from_uri("sqlite:///data.db")

# Establecemos la clave de la API OpenAI
os.environ["OPENAI_API_KEY"] = API.OPENAI_API_KEY

# Crea una instancia de la clase ChatOpenAI para usar el modelo
# Se configura con temperatura 0 para que no sea creativo y el modelo 'gpt-3.5-turbo'
llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

# Crea una instancia de la clase SQLDatabaseChain para unir el modelo y la DB
cadena = SQLDatabaseChain(llm=llm, database=db, verbose=False)

# Definimos un formato personalizado para la respuesta que generará el modelo
formato = """
Dada una pregunta del usuario, sigue estos pasos para obtener la información de la base de datos:

1. Crea una consulta SQLite3 utilizando la base de datos 'data.db'.
2. Revisa los resultados de la consulta para obtener la información solicitada.
3. Devuelve el resultado de la consulta.
4. Si es necesario hacer alguna aclaración o proporcionar información adicional, hazlo siempre en español.
#{question}
"""

# Toma la entrada del usuario y ejecuta la cadena para obtener la respuesta
def consulta(input_usuario):
    consulta = formato.format(question=input_usuario)
    resultado = cadena.run(consulta)
    return resultado
