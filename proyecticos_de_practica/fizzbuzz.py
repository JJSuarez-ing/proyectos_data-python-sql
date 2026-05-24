# Problema:
# Imprime los números del 1 al 50.
# - Si el número es múltiplo de 3, imprime "Fizz".
# - Si el número es múltiplo de 5, imprime "Buzz".
# - Si es múltiplo de ambos, imprime "FizzBuzz".

for i in range(1,51):
    if i%3==0 and i%5==0:
        print('fizzbuzz')
    elif i%3==0:
        print(' buzz')
    elif i%5==0:
        print(' frizz')
    else:
        print(i)
