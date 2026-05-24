import pandas as pd
import sqlite3
import datetime 


conexion = sqlite3.connect(r'c:\Users\joses\Documents\Python\agencia\agencia.db')

consulta='''SELECT ciudad, round(avg(monto),2) as promedio
from modelos as m join pagos as p on m.id=p.id_modelo 
group by ciudad
having avg(monto)> 40;'''

df_reporte = pd.read_sql_query(consulta, conexion)


print('_______REPORTE DE LA GAENCIA________')
print(df_reporte)
#.iterrows() es el motor que te permite desarmar
#la tabla fila por fila para que Python pueda analizar los
#datos de cada registro de forma individual
lista=[]
for indice, fila in df_reporte.iterrows():
    ciudad=fila['ciudad']
    promedio=fila['promedio']
    #metemos le ponemos esos parentesis a append([]) para que acepte mas de 2 parametro
    #porque por defecto acepta 1
    lista.append([ciudad.capitalize(), promedio])
#capturamos la fecha de hoy con datatime
hoy=datetime.datetime.now()
fecha=hoy.strftime('%d-%m-%y')

if len(lista):
    archivo=pd.DataFrame(lista, columns= ['Ciudad', 'Promedio'])
    archivo.to_excel(f'reporte_pedido_{fecha}.xlsx', index=False)
    print('todo con exito donde el jefe')
else:
    print('No tenemos nada en la lista bro')

conexion.close()