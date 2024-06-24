def format_str(datos):
    datos_str = []
    for elemento in datos:
        datos_str.append(elemento.strip().lower().title())
    return datos_str
