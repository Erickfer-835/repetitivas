filas = int(input("dime una cantidad de filas para la piramide: "))

for i in range(1, filas + 1):

    espacios = " " * (filas - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)