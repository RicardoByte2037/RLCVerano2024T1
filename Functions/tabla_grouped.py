def tabla_grouped(clases, lim_inf, lim_sup, mrks, fa, fr, facum):
    print("{:^10}".format("Clase"), "{:^25}".format("Limite Inferior"), "{:^25}".format("Limite Superior"), "{:^20}".format("Marca de clase"), "{:^20}".format("Frecuencia Absoluta"), "{:^25}".format("Frecuencia Relativa"), "{:^25}".format("Frecuencia Acumulada"))
    print("----------", "-------------------------", "-------------------------", "-------------------", "-------------------", "-------------------------", "-------------------------")
    
    for i in range(len(clases)):
        print("{:^10}".format(f"Clase {clases[i]}"), "{:^25.3f}".format(lim_inf[i]), "{:^25.3f}".format(lim_sup[i]), "{:^20.3f}".format(mrks[i]), "{:^20}".format(fa[i]), "{:^25.3f}".format(fr[i]), "{:^25.3f}".format(facum[i]))
