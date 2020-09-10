#####
print ("Ejercicio 1")

altura = int(input("Ingresar la altura\n"))
base = float(input("Ingresar base\n"))
print ("El área de Trinángulo es: ", ((base * altura)/2))

#####
print ("Ejercicio 2")

dolares = float(input("Ingresar cantidad en dólares\n"))
print ("La cantidad en pesos es: ", dolares * 21)

##### 
print ("Ejercicio 3")
celcius = float(input("Ingresar grados °C\n"))
print ("Grados fahrenheit: ",((celcius * 1.8)+32))

#####
print ("Ejercicio 4") #                                       s   m     h     a     l
print ("La cantidad de segundos que tiene un lustro es: ", (((60 * 60) * 24 * 365) * 5))

#####
print ("Ejercicio 5")
VEL_LUZ = 299792458 / 1000
DISTANCIA = 227940000
TIEMPO = DISTANCIA / VEL_LUZ
print ("El tiempo que tarda la luz del sol en llegar a marte es: ", TIEMPO)

#####
print ("Ejercicio 6")
pi = 3.141516
diametro = 50
perimetro = ((2 * pi) * (diametro / 2))
print("El número de vueltas que da una llanta en 1 km es: ", 100 / perimetro)

#####
print ("Ejercicio 7")
ALTURA, TAN_22 = 20, 0.40403
print("El largo de la sombra es ", (ALTURA / TAN_22))

#####
print ("Ejercicio 8")
Edad_1 = int(input("Ingrese primer edad \n"))
Edad_2 = int(input("Ingrese segunda edad \n"))
igual = Edad_1 is Edad_2
print("Las edades son ", igual)

#####
print ("Ejercicio 9")
from datetime import date
from datetime import datetime

BIRTH_DATE = datetime(1993, 8, 11, 12, 1, 00, 00000)
BIRTH_MONTH = format(BIRTH_DATE.month)
BIRTH_YEAR = format(BIRTH_DATE.year)
today_date= date.today()
today_month = format(today_date.month)
today_year = format(today_date.year)
age = BIRTH_YEAR - today_year
print(age)

#####
print ("Ejercicio 10")
c_inlges = int(input("Ingresa salificación de Inlgés \n"))
c_mate = int(input("Ingresa salificación de Matemáticas \n"))
c_prog = int(input("Ingresa salificación de Programación \n"))
c_espanol = int(input("Ingresa salificación de Español \n"))
c_eco = int(input("Ingresa salificación de Economía \n"))
print("El promedio fue de ", ((c_inlges + c_mate + c_prog + c_espanol + c_eco)/ 5))