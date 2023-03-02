print("\n --- Distribuidora Percentuais --- \n")

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
Outros = 19849.53

Total = sp + rj + mg + es + Outros

per_sp = sp / Total
per_rj = rj / Total
per_mg = mg / Total
per_es = es / Total
per_outros = Outros / Total

print(Total)
print("Percentual de SP: {}%".format(per_sp))
print("Percentual de RJ: {}%".format(per_rj))
print("Percentual de MG: {}%".format(per_mg))
print("Percentual de ES: {}%".format(per_es))
print("Percentual de Outros: {}%".format(per_outros))