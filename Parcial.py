#Autor: AndrésF.Núñez
#Fecha: 01-10-2025

#Crear un algoritmo que lea 5 numeros enteros uno por uno e identifique cuales son positivos y pares. Al final, debe mostrar la suma total de esos numeros
print("Punto 1.)\n")
R1=1 

tot=0
while R1<6:
    R1=R1+1
    val1=int(input("ingrese un número: "))
    if val1>0:
        val1/2
        if type(val1)==int:
            val1*2
            tot=tot+val1
print("la suma de los positivos y pares es: ",tot)

#Diseñe un programa que lea la edad de una persona y muestre un mensaje segun el siguiente criterio: <13=niño, entre 13 y 17= adolescente, entre 18 y 59=adulto, >60=adulto mayor.
#Restriccion: el programa debe validar que la eda sea un numero positivo, si no, mostrar un  mensaje de error

print("Punto 2.)\n")
edad=0
while edad<=0:
    edad=int(input("Dejame tu edad porfavor: "))
    if edad<=0:
        print("Que me des tu edad, sea serio")
    else:
        break
if edad<13:
    print("Niño")
if 12<edad<18:
    print("Adolescente")
if 17<edad<60:
    print("Adulto")
if edad>59:
    print("Adulto Mayor")

#Solicite al usuario que escriba una palabra (sin espacios) y cuente cuantas vocales tiene. El contador debe ser sensible a mayusculas y minusculas

print("Punto 3.)\n")

wor="ey"
while wor.count(" ")==0:
    wor=input("Dame una palabra porfavor, y sin espacios: ")
    if wor.count(" ")>0:
        print("Que no tenga espacios, dije")
        wor="ey"
    else:
        break
print("la palabre tiene: ")
a=wor.count("a")+wor.count("A")
print("a: ",a)
e=wor.count("e")+wor.count("E")
print("e: ",e)
i=wor.count("i")+wor.count("I")
print("i: ",i)
o=wor.count("o")+wor.count("O")
print("o: ",o)
u=wor.count("u")+wor.count("U")
print("u: ",u)