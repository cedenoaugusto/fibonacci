""" 
Secuencia de Fibonacci 
F(n) = n-1 + n-2
"""
def calcular_fibonacci(cant):
    lista_resultado = list()

    for n in range(cant):
        if n == 0:
            total = 0
            n1 = 0
        elif n == 1:
            total = 1
            n2 = 1
        else:
            total = n1 + n2
            n1 = n2
            n2 = total

        lista_resultado.append(f'F({n}) => {total}')

    return lista_resultado

print('*****************************************')
salida = calcular_fibonacci(20)
for i in salida:
    print(i)