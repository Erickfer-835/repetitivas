num = input("ingresa un numero ")
numeros = "0123456789"
contador = 0

for nume in num:
    if nume in numeros: 
        contador = contador + 1
print ("esta es la cantidad de digitos : ",contador)