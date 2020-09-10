# C:\Users\mxmiher>Downloads\Cursos\Python\HolaMundo.py para compilar el script en la terminal
CONSTANTE = "Es una constante" #Las cnostantes simepre van en mayusculas 
nombre_tutor = "Miguel" #Sanke Case (_)

var1, var2, var3 = 10, 20, 5*5

print ("Hola Mundo")
print (nombre_tutor)
print (CONSTANTE)
print(var1,var2,var3)

mayor = var1 > var2
menor = var1 < var2
mayor_igual = var1 >= var2
menor_igual = var1 <= var2
igual = var1 == var2 # o
igual2 = var1 is var2
dierente = var1 != var2

print(menor,mayor,menor_igual,igual2,mayor_igual,igual,dierente)

nombre = input("¿Cúal es tu nombre?\n") #Función para almencenar datos desde teclado
edad = int(input("¿Cúal es tu edad?\n")) #int convierte el string en numero entero
peso = float(input("¿Cúal es tu peso?\n")) #int convierte el string en numero flotante
autorizacion = input("¿Estás autorizado?(Sí/No)\n") == "Si" #Si importa la mayuscula

print ("Hola", nombre)
print (nombre,edad)
print (nombre,edad,peso)
print("Estado de autorización", autorizacion)