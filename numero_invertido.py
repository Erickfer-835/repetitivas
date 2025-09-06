num = int(input("Ingresa un número: "))
invertido = 0

while numero > 0:
    digito = num % 10          
    invertido = invertido * 10 + digito
    num //= 10                 

print("Número invertido:", invertido)