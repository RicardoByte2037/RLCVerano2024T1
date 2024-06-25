import matplotlib.pyplot as plt

def plot_pie(datos, marcas_texto):
    max_index = datos.index(max(datos))
    separaciones = [0.08 if i == max_index else 0 for i in range(len(datos))]

    plt.pie(datos,
            explode=separaciones,
            counterclock=False,
            startangle=90,
            autopct="%0.1f%%",
            pctdistance=0.8,
            labels=marcas_texto)

    plt.title("Distribución de Sabores", fontsize=20)
    plt.show()
    