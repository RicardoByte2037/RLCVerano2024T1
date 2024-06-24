def tabla(clase, fa_sorted, frecuencia_rel, frecuencia_rel_acum):
    print("{:^10}".format("Clases"), "{:^15}".format("Fa"), "{:^20}".format("Fr"), "{:^20}".format("F acumulada"))
    print("----------", "---------------", "-------------------", "-------------------")
    
    for i in range(len(clase)):
        print("{:^10}".format(f"Clase {clase[i]}"), "{:^15}".format(fa_sorted[i]), "{:^20.3f}".format(frecuencia_rel[i]), "{:^20.3f}".format(frecuencia_rel_acum[i]))
        