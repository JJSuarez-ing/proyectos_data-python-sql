print('calculador basico')
print('====================')
print('que operacion desea realizar?: ')
(print('1. suma'))
(print('2. resta'))
(print('3. multiplicacion'))
(print('4. division'))
(print('5. modulo o recisuo'))
(print('6. exponente o potencia'))
(print('7. salir'))
operacion=int(input('ingrese la operacion a realizar (1-7): '))
if operacion=='':
    print('debe ingrsear un valor valido')
elif not isinstance(operacion, int):
    print('no puede ingresar caracteres alfabeticos ')
elif operacion>=8:
    print('el limite de nuestra calculador por ahora es de 7')
elif operacion==0:
    print('debe una operacion valida entre el 1 y el 7 ')

elif operacion==1:
    numero1=int(input('ingrese el primer numero a sumar: '))
    numero2=int(input('ingrese el segundo numero a sumar: '))
    print(f'la suma de {numero1} y {numero2} es: {numero1+numero2}')
elif operacion==2:
    numero1=int(input('ingrese el primer numero a restar: '))
    numero2=int(input('ingrese el segundo numero a restar: '))
    print(f'la resta de {numero1} y {numero2} es: {numero1-numero2}')
elif operacion==3:
    numero1=int(input('ingrese el primer numero a multiplicar: '))
    numero2=int(input('ingrese el segundo numero a multiplicar: '))
    print(f'la multiplicacion de {numero1} y {numero2} es: {numero1*numero2}')
elif operacion==4:
    numero1=int(input('ingrese el primer numero a dividir: '))
    numero2=int(input('ingrese el segundo numero a dividir: '))
    if numero1==0 or numero2==0:
        print('no se puede dividir entre 0')
    else:
        print(f'la division de {numero1} y {numero2} es: {numero1/numero2}')
elif operacion==5:
    numero1=int(input('ingrese el primer numero para obtener el modulo: '))
    numero2=int(input('ingrese el segundo numero para obtener el modulo: '))
    print(f'el modulo de {numero1} y {numero2} es: {numero1%numero2}')
elif operacion==6:
    numero1=int(input('ingrese la base: '))
    numero2=int(input('ingrese el exponente: '))
    print(f'el exponente de {numero1} y {numero2} es: {numero1**numero2}')
else:
    if operacion==7:
        print('Gracias por usar mi calculadora, hasta luego!')
        