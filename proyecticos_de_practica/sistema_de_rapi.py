print('Sistema vacacional de Rappi')
print('=====================')
# Clave del personal de atencion al cliente
clave_1='cliente'
# Clave del departamento de logistica
clave_2='limpiandoando'
# Clave del departamento de gerencia 
clave_3='firmecoño'
nombre=input('ingrese su nombre: ')
clave=input('ingrese la contraseña de su departamento: ')
if clave==clave_1:
    print( f' Bienvenido/a {nombre} usted es del departamento de atencion al cliente')
    antiguedad=int(input(nombre+ ',ingrese su antiguedad en años en la empresa: '))
    if antiguedad==0:
        print(' a usted no le corresponden vacaciones por ahora')
    elif antiguedad==str('qwertyuiopasdfghjklñzxcvbnm'):
        print('debe ingresar un valor numerico valido')
    elif antiguedad==1:
        print(nombre+ ', le corresponden 6 meses de vaciones')
    elif antiguedad==2 or antiguedad==3 or antiguedad==4 or antiguedad==5 or antiguedad==6:
        print(nombre+ ', le corresponden 14 dias de vacaciones ')
    else:
        if antiguedad>=7:
            print(nombre+ ', le corresponden 20 dias de vacaciones ')
elif clave== clave_2:
    print(f'Bienvenido/a {nombre} , usted es del departamento de logistica ')
    antiguedad=int(input(nombre+ ',ingrese su antiguedad en años en la empresa: '))
    if antiguedad==0:
        print(' a usted no le corresponden vacaciones por ahora')
    elif antiguedad==str('qwertyuiopasdfghjklñzxcvbnm'):
        print('debe ingresar un valor numerico valido')
    elif antiguedad==1:
        print(nombre+ ', le corresponden 7 dias de vaciones')
    elif antiguedad==2 or antiguedad==3 or antiguedad==4 or antiguedad==5 or antiguedad==6:
        print(nombre+ ', le corresponden 15 dias de vacaciones ')
    else: 
        if antiguedad>=7:
            print(nombre+ ', le corresponden 22 dias de vacaciones ')
elif clave== clave_3:
    print(f'Bienvenido/a {nombre} , usted es del departamento de gerencia ')
    antiguedad=int(input(nombre+ ',ingrese su antiguedad en años en la empresa: '))
    if antiguedad==0:
        print(' a usted no le corresponden vacaciones por ahora')
    elif antiguedad==str('qwertyuiopasdfghjklñzxcvbnm'):
        print('debe ingresar un valor numerico valido')
    elif antiguedad==1:
        print(nombre+ ', le corresponden 10 dias de vaciones')
    elif antiguedad==2 or antiguedad==3 or antiguedad==4 or antiguedad==5 or antiguedad==6:
        print(nombre+ ', le corresponden 20 dias de vacaciones ')
    else:
        if antiguedad>=7:
            print(nombre+ ', le corresponden 30 dias de vacaciones ')
else:
    if clave!= clave_1 or clave_2 or clave_3:
        print('contraseña incorrecta')