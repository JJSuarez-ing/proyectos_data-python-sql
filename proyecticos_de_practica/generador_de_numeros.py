def number_pattern(n):

    if not isinstance(n, int):
        print('Argument must be an integer value.')
    if n < 1:
        print('Argument must be an integer greater than 0.')
    else:
        resultado=[]
        for i in range(1, n + 1):
            resultado.append(str(i))
    return resultado
print(" ".join(number_pattern(4)))