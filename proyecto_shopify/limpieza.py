import pandas as pd
import sqlite3
try:
    df = pd.read_csv('shopify_trending_products_2025.csv')
except Exception as e:
    print(f'hubo error al leer :{e}')


conexion=sqlite3.connect(':memory:')

df.to_sql('shopify_tabla', conexion, index=False, if_exists='replace')


consulta1='''SELECT category, sum(Estimated_Revenue_in_2025_USD) as Generado
FROM shopify_tabla
group by category
order by sum(Estimated_Revenue_in_2025_USD) desc;'''

print('\n___Dinero Generado por categoria___')
vista1=pd.read_sql_query(consulta1, conexion)
#El .apply() agarra una
#instrucción y se la aplica a todas las filas de la columna al mismo tiempo, como un tiro.
vista1['Generado'] = vista1['Generado'].apply(lambda x: f'${x / 1e6:.2f} M')
#La e significa elevado a la potencia de 10 
#Así que el número que viene después de la e te dice cuántos ceros le tienes que poner por delante al 1


# Le sumamos 1 al índice
vista1.index = vista1.index + 1
print(vista1)


consulta2=''' SELECT Trend_Source, SUM(Estimated_Total_Units_Sold_in_2025) as total
FROM shopify_tabla
group by Trend_Source;'''

print('\n___Fuentes de tendencia___')
vista2=pd.read_sql_query(consulta2, conexion)
vista2['total']=vista2['total'].apply(lambda x: f'{x / 1e6:.2f} M uni...')
#La e significa elevado a la potencia de 10 
#Así que el número que viene después de la e te dice cuántos ceros le tienes que poner por delante al 1


# Le sumamos 1 al índice
vista2.index = vista2.index + 1
print(vista2)


consulta3='''SELECT Product_Name, category, Estimated_Total_Units_Sold_in_2025
FROM shopify_tabla
order by Estimated_Total_Units_Sold_in_2025 DESC limit 3
;'''

vista3=pd.read_sql_query(consulta3, conexion)
vista3['Estimated_Total_Units_Sold_in_2025']=vista3['Estimated_Total_Units_Sold_in_2025'].apply(lambda x: f'{x :,}  uni...')
#La e significa elevado a la potencia de 10 
#Así que el número que viene después de la e te dice cuántos ceros le tienes que poner por delante al 1


# Le sumamos 1 al índice
vista3.index = vista3.index + 1

print('\n____ Top 3 prodectos estrella')
print(vista3)

conexion.close()
#


