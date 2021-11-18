from collections import Counter


print(" ")
nombreEmpresa = str(input("Ingrese el nombre de la empresa: "))
letras = Counter(nombreEmpresa)
for letter , count in letras.most_common(3):
    print('{}: {:>7}'.format(letter, count))