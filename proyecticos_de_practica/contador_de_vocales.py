# Problema:
# Escribe un programa que cuente cuántas vocales tiene una palabra.
# Ejemplo: "murciélago" -> 5
contador =0
palabra=input('ingrese palabra:')
for vocales in palabra:
    if vocales== 'a' or vocales=='e' or vocales=='i' or vocales== 'o' or vocales=='u':
        contador+=1
        print(contador, end=' ')