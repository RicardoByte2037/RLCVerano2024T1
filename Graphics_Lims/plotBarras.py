import matplotlib.pyplot as plt

def plot_grafBarras(frecuencias_relativas, marcas_clase, marcas_texto):
    plt.figure(figsize=(12, 6))

    plt.barh(marcas_clase, frecuencias_relativas,
             height=0.5, edgecolor="k",
             color=["#37CA64", "#FF99F3", "#37C5CA", "#E74E50", "#FC8C29"])

    plt.yticks(marcas_clase, marcas_texto, fontsize=12)
    plt.xlabel("Frecuencias Relativas", fontsize=15)
    plt.ylabel("Marcas de Clase", fontsize=15)
    plt.title("Diagrama de barras", fontsize=20)

    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.gca().invert_yaxis()  
    plt.show()
    