import unicodedata

def clases_str_sort(datos_formated):
    """
    Función para ordenar alfabéticamente una lista de strings, ignorando acentos y mayúsculas.
    
    Parámetros:
    - datos_formated (list): lista de strings que representan los datos formateados
    
    Lo que hace:
    - Ordena la lista de strings alfabéticamente en orden ascendente, ignorando acentos y mayúsculas
    - Devuelve la lista de strings ordenada
    
    Uso:
    - Se utiliza para ordenar la lista de datos formateados para su posterior análisis y visualización
    - Se aplica a la lista de datos formateados para obtener una lista ordenada alfabéticamente
    """
    
    # Normalizar los caracteres y ignorar acentos y mayúsculas
    datos_formated.sort(key=lambda x: unicodedata.normalize('NFD', x).casefold())
    return datos_formated
