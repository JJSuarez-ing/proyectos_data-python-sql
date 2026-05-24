def control_acceso(edades):
    aceptados=0
    rechazados=0
    for edad in edades:
        if edad<18:
            rechazados+=1

        else:
            aceptados+=1
    return f'aceptados:{aceptados},rechazados:{rechazados}'
mis_edades = [18, 15, 25, 30, 12]
print(control_acceso(mis_edades))