import matplotlib.pyplot as plt

def plot_grafPie():
    datos = [10, 20, 20, 15, 35]
    marcas_texto = [0.165, 0.495, 0.825, 1.155, 1.485]
    separaciones = [0, 0, 0, 0, 0]

    plt.figure(figsize=(8, 8))

    plt.pie(datos,
            explode=separaciones,
            counterclock=False,
            startangle=90,
            autopct="%0.1f%%",
            pctdistance=0.8,
            colors=["#37CA64", "#FF99F3", "#37C5CA", "#E74E50", "#FC8C29"],
            labels=marcas_texto)

    plt.title("Gráfico de Pastel", fontsize=15)
    plt.show()

