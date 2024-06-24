import matplotlib.pyplot as plt

def plot_pie(datos, marcas_texto, separaciones):
    # Crea una figura con un tamaño de 8x8 pulgadas (opcional)
    plt.figure(figsize=(8, 8))  

    # Crea un gráfico de pie con los datos
    # El parámetro explode especifica la separación de cada porción del pie
    # El parámetro counterclock=False indica que el gráfico se dibuja en sentido horario
    # El parámetro startangle=90 indica que el gráfico comienza en el ángulo de 90 grados (arriba)
    # El parámetro autopct="%0.1f%%" indica que se mostrará el porcentaje de cada porción con un decimal
    # El parámetro pctdistance=0.8 indica que el porcentaje se mostrará a una distancia del 80% del radio del pie
    # El parámetro colors especifica los colores de cada porción del pie
    # El parámetro labels especifica las etiquetas de cada porción del pie
    plt.pie(datos, 
            explode=separaciones,
            counterclock=False,
            startangle=90, 
            autopct="%0.1f%%",
            pctdistance=0.8, 
            colors=["#37CA64", "#FF99F3", "#37C5CA", "#E74E50", "#FC8C29", "#DEE74E"],
            labels=marcas_texto)

    # Establece el título del gráfico (opcional)
    plt.title("Distribución de Sabores", fontsize=20)  

    # Muestra el gráfico
    plt.show()
    