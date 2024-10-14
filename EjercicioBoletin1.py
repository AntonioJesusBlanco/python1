#1
nombre1=input()
print ("!Hola ", nombre1, "-Me alegro de conocerle, ",nombre1)

#2 
nombre2 = input()
print (nombre2.upper)
print (len(nombre2))

#3
numeroIntroducido = int(input())
numeroEnPar=0

while numeroEnPar<numeroIntroducido:
    print(numeroEnPar)
    numeroEnPar+=2

#4
peso = float(input())
altura = float(input())
imc= peso/altura
print (round(imc,2))

#5
import random

numeroAlAzar1 = random.randint(2, 10)
numeroAlAzar2 = random.randint(2, 10)
multiplicacion = numeroAlAzar1*numeroAlAzar2
print ("Dime un numero")
numeroIntento=int(input())
if numeroIntento == multiplicacion:
    print("Has acertado")
else:
    print("Error, el numero correcto era ",multiplicacion)
