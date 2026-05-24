import pandas as pd
#ceacion de series con indice y valor
notas  = pd.Series([20,30,1,25,65,7,80])
print(notas.dtype)
print(notas.size)
print(notas.index)
print(notas[1:2])
print(notas*2)
#ceacion de series con indice y valor
materias = pd.Series(['Economia', 'contabilidad', 'lenguaje', 'matematicas','fisica' , ' quimica', 'programacion'])
resultado=pd.Series(index=notas, data=materias.values)
#juntamos series apartir de indice y valor, en este caso tenemos que extraerle solamente el valor a materias para que el indice sea el que definimos alli y solamente los valores de materia sea el valor 

print(resultado)
print('suma de la lista de notas:', notas.sum())
#datadeame paartiendo de dicc
data = {'NOMBRES': ['jose', 'maria', 'david'] , 'APELLIDOS': ['Suarez', 'Iriarte', 'Martins']}
estudiantes=pd.DataFrame(data)
print(estudiantes)
#dateframe partiendo de list
df= pd.DataFrame([['maria', 48], ['jose', 19], ['david', 52]], columns=['NOMBRES', 'EDADES'])
print(df)
#leemos archivos 
df= pd.read_csv('reporte_agencia.txt')
df.columns=['MODELOS', 'SEGUIDORES', 'CIUDAD']
print(df)