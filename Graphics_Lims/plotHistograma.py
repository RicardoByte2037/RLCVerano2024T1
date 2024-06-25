import matplotlib.pyplot as plt

def plot_grafHist(frecuencias_relativas, marcas_clase, marcas_texto):
    plt.figure(figsize=(12, 6))
    plt.bar(marcas_clase, frecuencias_relativas, width=1, edgecolor="k", color=["#37CA64", "#FF99F3", "#37C5CA", "#E74E50", "#FC8C29"])
    
    plt.xticks(marcas_clase, marcas_texto, fontsize=15, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencia relativa", fontsize=20)
    plt.title("Histograma", fontsize=25)
    plt.ylim(0, 6) 

    plt.grid()
    plt.show()
    