import pandas as pd
import sqlite3

# Conectamos y traemos la data fusionada
conexion = sqlite3.connect('agencia.db')
df_modelos = pd.read_sql_query("SELECT * FROM modelos", conexion)
df_pagos = pd.read_sql_query("SELECT * FROM pagos", conexion)
df_final = pd.merge(df_modelos, df_pagos, left_on='id', right_on='id_modelo')
conexion.close()

# =====================================================================
# EL RETO DE DESPEDIDA
# =====================================================================

# PASO A: Filtra 'df_final' para dejar SOLO los registros donde 'monto' sea MAYOR a 500.
# (Pista: Usa los corchetes mágicos [] y el signo >)
df_top = df_final[df_final['monto']>500]
# PASO B: Ordena ese nuevo 'df_top' de mayor a menor según la columna 'monto'.
# (Pista: Usa el método .sort_values(by='monto', ascending=False) )
df_top_ordenado = df_top.sort_values(by='monto', ascending= False)

# PASO C: Exporta 'df_top_ordenado' a un archivo Excel llamado 'modelos_top.xlsx' sin índices.
# ¡Tu código aquí!
df_top_ordenado.to_excel('modelos_top.xlsx', index=False)

print('Reporte Top generado con éxito!')