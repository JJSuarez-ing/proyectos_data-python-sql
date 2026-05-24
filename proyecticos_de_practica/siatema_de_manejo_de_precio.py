def total_a_pagar(precios):
    cuenta_total=0
    for lista in precios:
        if lista > 5:
            cuenta_total+=lista
    return f'Tu total a pagar es:{cuenta_total} '
precios=[1,4,5,6]
print(total_a_pagar(precios))
