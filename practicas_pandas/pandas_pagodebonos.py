import sqlite3
import pandas as pd

# 1. Traemos la data (Esto ya te lo conoces de memoria)
conexion = sqlite3.connect('agencia.db')
df_modelos = pd.read_sql_query("SELECT * FROM modelos", conexion)
df_pagos = pd.read_sql_query("SELECT * FROM pagos", conexion)
conexion.close()

# 2. Hacemos el merge para tener nombres, ciudades y montos juntos
df_final = pd.merge(df_modelos, df_pagos, left_on='id', right_on='id_modelo')

# === AQUÍ EMPIEZA TU TRABAJO ===

# PASO A: Crea un nuevo DataFrame llamado 'df_valencia' 
# que contenga SOLO las filas donde la ciudad sea 'valencia'.
# (Pista: Usa los corchetes [] y la lógica que aprendimos hoy).
df_vargas = df_final[df_final['ciudad']=='vargas']
df_vargas['bono']=(df_vargas['monto']*0.10).round(2)

# PASO B: Crea una nueva columna en 'df_valencia' llamada 'bono'.
# Esta columna debe ser igual al 'monto' multiplicado por 0.10 (el 10%).
# (Pista: Recuerda la vectorización, se hace en una sola línea sin bucles).
# ¡Tu código aquí!

# PASO C: Calcula el total de todos los bonos sumando esa nueva columna.
# (Pista: Usa el método de agregación matemática que ya conoces).
total_bonos_vargas = df_vargas['bono'].sum()

# 3. Imprimimos el resultado para el jefe
print("--- 💰 REPORTE DE BONOS - VARGAS ---")
print(f"La agencia debe preparar un total de: {total_bonos_vargas}$ para los bonos.")

df_vargas.to_excel('bonos_vargas.xlsx', index=False)
print('archivo listo bro')