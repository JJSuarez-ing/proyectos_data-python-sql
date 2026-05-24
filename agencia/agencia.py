import sqlite3
import os 

# Conexión
conexion = sqlite3.connect('agencia.db')
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS modelos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, seguidores INTEGER, ciudad TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS pagos (id_pago INTEGER PRIMARY KEY AUTOINCREMENT, id_modelo INTEger, monto REAL, fecha TEXT, FOREIGN KEY (id_modelo) REFERENCES modelos(id) )")
conexion.commit()
def reg_pagos(cursor,conexion):
    conexion=sqlite3.connect('agencia.db')
    cursor=conexion.cursor()
    try:
        id_modelo=int(input('Ingrese el ID del Modelo: '))
        monto=float(input(f'Ingrese el monto del modelo, "{id_modelo}": '))
        fecha=str(input('Fecha del pago de la campaña del modelo: '))
        cursor.execute("INSERT INTO pagos (id_modelo, monto, fecha) VALUES (?, ?, ?)", (id_modelo, monto, fecha))
        conexion.commit()
        print('Pago registrado con exito')
    except ValueError as e:
        print(f'Dato invalido {e}')
    except sqlite3.IntegrityError as e:
        print(f'Estas intentando registrar el pago de un modelo que no existe  {e}')
    input('PRESIONE ENTER PARA VOLVER')
def tablas_pandas(cursor,conexion):
    import pandas as pd
    conexion = sqlite3.connect('agencia.db')

    # 2. Convertimos las tablas a DataFrames (Las fotos para analizar)
    # No usamos bucles, Pandas lo hace solo
    df_modelos = pd.read_sql_query("SELECT * FROM modelos", conexion)
    df_pagos = pd.read_sql_query("SELECT * FROM pagos", conexion)

    # 3. UNIÓN DE DATOS (El famoso Merge)
    # Pegamos los nombres de los modelos con sus montos de pago
    df_final = pd.merge(df_modelos, df_pagos, left_on='id', right_on='id_modelo')

    # 4. ANÁLISIS DE NEGOCIO: ¿Cuánto ha ganado cada modelo en total?
    # Agrupamos por nombre y sumamos el monto
    ranking_ingresos = df_final.groupby('nombre')['monto'].sum().sort_values(ascending=False)

    print("--- 📊 RANKING DE INGRESOS ---")
    print(ranking_ingresos)

    # 5. ANÁLISIS POR CIUDAD: ¿Dónde está el dinero?
    ranking_ciudad = df_final.groupby('ciudad')['monto'].sum()

    print("\n--- 📍 INGRESOS POR CIUDAD ---")
    print(ranking_ciudad)
    input("PRESIONE ENTER PARA VOLVER")
    conexion.close()
    
def limpio():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def lista_modelos(cursor):
    cursor.execute('SELECT * FROM modelos ORDER BY id DESC')
    modelos_llamada=cursor.fetchall()
    for fila in modelos_llamada:
        print(f'ID-->{fila[0]} nombre--->{fila[1]} seguidores--->{fila[2]} cuidad--->{fila[3]}\n')
    else:
        if not modelos_llamada:
            print('lista vacia')
    input('\nPRESIONE ENTER PARA VOLVER')
def registro(cursor,conexion):
    nombre_u = input("Introduce el nombre del modelo: ")
    try:
        seguidores_u = int(input("Introduce la cantidad de seguidores: "))
    except ValueError:
        print('Ingreso un dato invalido a seguidores por ahora le asignaremos el numero 0')
        seguidores_u=0
    ciudad_u = input("Introduce la ciudad: ")
    try:
        cursor.execute("INSERT INTO modelos (nombre, seguidores, ciudad) VALUES (?, ?, ?)", 
                        (nombre_u, seguidores_u, ciudad_u))
    
        conexion.commit()
        print("\n Datos guardados correctamente.")
    except sqlite3.Error as e:
        print(f" Error de base de datos: {e}")
    cursor.execute("SELECT * FROM modelos ORDER BY id DESC LIMIT 1")
        #resultado = cursor.fetchone() # Usamos fetchone porque solo insertamos uno, fetchone nos devuelve una tupla por eso la asignamos a una variable e imprimimos por posiciones 
    resultado=cursor.fetchone()
    if resultado:
        print(f"Modelo:{resultado} Registrado exititoxamente")
    input('\nPRESIONE ENTER PARA VOLVER')
def eliminacion(cursor,conexion):
    try:
        eliminacion_for_id = int(input('¿A quién quieres eliminar? (ingresa ID): '))
        # Verificar si el ID existe
        cursor.execute("SELECT id FROM modelos WHERE id = ?", (eliminacion_for_id,))
        existe = cursor.fetchone()
        if existe:
            cursor.execute("DELETE FROM modelos WHERE id = ?", (eliminacion_for_id,))
            conexion.commit()
            print(f'Eliminado exitosamente el modelo con ID {eliminacion_for_id}')
        else:
            print('No se encuentra el usuario con ese ID')
    except ValueError:
            print('ID inválido, ingrsa numero entero')
    except sqlite3.Error as e:
            print(f'Error de base de datos: {e}')
    input('\nPRESIONE ENTER PARA VOLVER')
def edicion_modelo(cursor,conexion):
    try:
            editar_id = int(input('¿A qué modelo quieres editar? Ingresa ID: '))
            cursor.execute("SELECT id FROM modelos WHERE id = ?", (editar_id,))
            existe = cursor.fetchone()
            if not existe:
                print('No se encuentra el modelo con ese ID.')
            else:
                nombre_u = input("Introduce el nombre del modelo: ")
                try:
                    seguidores_u = int(input("Introduce la cantidad de seguidores: "))
                except ValueError:
                    print('Ingreso un dato inválido a seguidores, asignamos 0.')
                    seguidores_u = 0
                ciudad_u = input("Introduce la ciudad: ")
                cursor.execute(
                    "UPDATE modelos SET nombre = ?, seguidores = ?, ciudad = ? WHERE id = ?",
                    (nombre_u, seguidores_u, ciudad_u, editar_id)
                )
            conexion.commit()
            print(f'Modelo con ID {editar_id} actualizado correctamente.')
    except ValueError:
            print('ID inválido, ingresa un número entero.')
    except sqlite3.Error as e:
        print(f'Disculpe, fallo nuestra base de datos: {e}')
    input('\nPRESIONE ENTER PARA VOLVER')
def estadisticas(cursor):
    try:
        print('=====================ESTADISTICAS DE LA AGENCIA======================')
        #PROMEDIO DE SEGUIDORES DE LA AGENCIA
        cursor.execute( "SELECT COUNT(*) FROM modelos")
        todos=cursor.fetchone()[0]
        print(f'Tenemos modelos {todos} totales en la agencia')
        # AVG DE SGUIDORES DE LA AGENCIA 
        cursor.execute("SELECT ROUND(AVG(seguidores), 2) FROM modelos")
        avg=cursor.fetchone()[0]
        print(f'Nuestro average de seguidores:{avg}')
        # TOP DE MODELOS MAS FAMOSOS DE LA AGENCIA 
        cursor.execute('SELECT nombre, seguidores FROM modelos ORDER BY seguidores DESC LIMIT 3')
        top3=cursor.fetchall()
        print('=========Top 3 modelos mas Reconocidos de la agencia===========')
        for i,modelo in enumerate(top3, start=1):
            print(f'{i}:{modelo[0]} con {modelo[1]} seguidores')
    except sqlite3.Error as e:
        print(f'Fallo nuestra base de datos {e}')
    input("\nPRESIONA ENTER PARA VOLVER")
def reporte_general(cursor):
    try:
        cursor.execute("SELECT nombre, seguidores, ciudad FROM modelos ORDER BY seguidores DESC")
        modelos=cursor.fetchall()
    except sqlite3.Error as e:
        print(f' nuestra base de datos fallo {e}')
    with open('reporte_agencia.txt', 'w', encoding='utf-8') as archivo:
    #lo dejamos de esa forma sencillo para que pandas no se confunda en caso de que querramos hacer ,
    #un analisis en otro momento, pudimos haber creado un dataframe? si, pero estabamos trabando un poco de logica
    #se que le bucle daña un poco la estructura del archivo bro, entiende que lo hice con un bucle 
        for i in modelos:
            model= f'modelo:{i[0]} , seguidores:{i[1]}, cuidad:{i[2]}\n'
            archivo.write(model)
        print('reporte en sus archivos, listos')
    input('\nPRESIONA ENTER PARA CONTINUAR')

programa_devuelto=True
while programa_devuelto:
    limpio()
    print("\n--- BIENVENIDO AL REGISTRO DE LA AGENCIA ---\n")
    try:
        opcion=int(input('''
        1. Mostrar Lista de Modelos\n 
        2. Registrar Modelos\n  
        3. Eliminar Modelo\n 
        4. Editar Modelo\n 
        5. Estadisticas\n 
        6. Reportes\n
        7. Estadisticas Avanzadas\n
        8. Resgistro de Pago\n
        9. salir\n'''))
        if opcion>9 or opcion<0:
            print('Te saliste del rango de opciones')
    except ValueError as e:
        print(f'Opcion invalida {e}') 
        input('\nPRESIONA ENTER PARA VOLVER...')
        continue
    if opcion==1:
        lista_modelos(cursor)
    if opcion==2:
        registro(cursor,conexion)
    if opcion==3:
        eliminacion(cursor,conexion)
    if opcion==4:
        edicion_modelo(cursor,conexion)
    if opcion==5:
        estadisticas(cursor)
    if opcion==6:
        reporte_general(cursor)
    if opcion==7:
        tablas_pandas(cursor,conexion)
    if opcion==8:
        reg_pagos(cursor, conexion)
    if opcion==9:
        print('bye')
        break
conexion.close()