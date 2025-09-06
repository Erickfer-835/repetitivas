num=int(input("ingresa un numero(si es cero se acabara): "))
contador=0
contador2=2
while num!=0:
    num=int(input("ingresa un numero(si es cero se acabara): "))
    if num%2==0:
        contador=contador+num
    else:
        contador2=contador2+num

print("la suma de numeros pares es: ",contador," y la suma de impares: ",contador2)