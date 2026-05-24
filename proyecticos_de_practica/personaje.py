punto_completo='●'
punto_vacio='○'
def personaje(nombre, fuerza, inteligencia, carisma):
    if not isinstance(nombre,str):
        return 'El nombre del personaje debe ser texto'
    if nombre== '':
        return 'El personaje debe tener un nombre'
    if len(nombre)>10:
        return 'El nombre del personaje es demasiado largo'
    if nombre==' ':
        return 'El nombre del personaje no debe tener espacios'
    if not isinstance(fuerza, int) or not isinstance(inteligencia, int) or not isinstance(carisma,int):
        return 'Todas las estadisticas deben ser numeros enteros'
    if fuerza<1 or inteligencia<1 or carisma<1 :
        return 'Todas las estadisticas deben ser menores a 1'
    if fuerza>4 or inteligencia>4 or carisma>4 :
        return 'Todas las estadisticas no deben ser mas de 4'
    if fuerza + inteligencia + carisma != 7:
        return 'El personaje debe comensar con 7 puntos'
    STR='STR'+ (punto_completo*fuerza) + (punto_vacio*(10-fuerza))
    INT='INT' + (punto_completo*inteligencia) + (punto_vacio*(10-inteligencia))
    CHA='CHA' + (punto_completo*carisma) + (punto_vacio*(10-carisma))
    return (f'{nombre}/n{STR}/n{INT}/n{CHA}')
