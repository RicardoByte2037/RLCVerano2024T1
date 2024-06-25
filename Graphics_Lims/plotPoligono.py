import matplotlib.pyplot as plt 

def plot_grafPoligono(clases, mrks, fr):
    datos_x_poligono = [0] + list(range(1, len(clases) + 1)) + [list(range(1, len(clases) + 1))[-1] + 1]
    datos_y_poligono = [0] + fr + [0]

    plt.figure(figsize=(15, 5))
    plt.plot(datos_x_poligono, datos_y_poligono, 
             linewidth=3, 
             color="#1C2833", 
             linestyle="--", 
             marker="o", 
             markersize=10, 
             markerfacecolor="#EB7AF5", 
             markeredgecolor="#003DA2",
             markeredgewidth=1.5)
    
    plt.xticks(list(range(1, len(clases) + 1)), mrks, fontsize=10)
    plt.xlabel("Marcas de clase", fontsize=15)
    plt.ylabel("Frecuencia relativa", fontsize=15)
    plt.title("Polígono de frecuencias", fontsize=20)
    plt.grid()
    plt.show()
        