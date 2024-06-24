def fa_grouped(lim_inf, lim_sup, datos):
  frecuencias = [0] * len(lim_inf)

  for dato in datos:
    for i in range(len(lim_inf)):
      if lim_inf[i] <= dato <= lim_sup[i]:
        frecuencias[i] += 1
        break

  return frecuencias