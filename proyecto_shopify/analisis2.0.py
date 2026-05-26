import sqlite3
import pandas as pd
conexion=sqlite3.connect(':memory:')
# creamos la tabla de comisiones dentro de la base de datos en memoria
try:
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasas_comision (
        Category TEXT,
        Porcentaje_Comision REAL
    )
    ''')

    # insertamos las comisiones de las categorías top
    comisiones = [
        ('Fitness', 0.05),       # 5% de comisión
        ('Pet', 0.07),           # 7% de comisión
        ('Digital Goods', 0.10), # 10% de comisión (por ser software)
        ('Beauty & Skincare', 0.04) # 4% de comisión
    ]
    cursor.executemany('INSERT INTO tasas_comision VALUES (?, ?)', comisiones)
    conexion.commit()

except sqlite3.Error as e:
    print(f'fallo la base de datos {e}')

try:
    df= pd.read_csv('shopify_trending_products_2025.csv')
except Exception as e:
    print(f'nos fallo as {e}')


df.to_sql('shopify_tabla', conexion, index=False, if_exists='replace')


consulta=(''' SELECT sh.product_name, sh.Category, sh.Estimated_Revenue_in_2025_USD, ts.Porcentaje_Comision
FROM shopify_tabla  as sh
inner join tasas_comision as ts on sh.Category=ts.Category
where Estimated_Revenue_in_2025_USD > 10000000;''')

resultado=pd.read_sql_query(consulta, conexion)


resultado['ingreso_neto']=resultado['Estimated_Revenue_in_2025_USD']-(resultado['Estimated_Revenue_in_2025_USD'] * resultado['Porcentaje_Comision'])
resultado['ingreso_neto']=resultado['ingreso_neto'].apply(lambda x: f'${x/1e6:.2f} M')
resultado.index=resultado.index + 1
try:
    resultado.to_excel('ingreso_neto.xlsx')
except Exception as e:
    print('no pudimos convertir a to_excel')
else:
    print('todo listo')

conexion.close()






