# sistemas de notas sencillo brou
def calcular_notas(not1,not2,not3,not4):
    for notas in [not1,not2,not3,not4]:
        if not isinstance(notas, (int,float)):
            return 'ingresa valor valido'
    promedi=(not1+not2+not3+not4)/4
    promedio=round(promedi)
    if notas < 10:
        return f'{promedio}:no aprobado'   
    else:
        return f'{promedio}: aprobado'
print(calcular_notas(4,14,10,10))









