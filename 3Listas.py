colores = ["Azul", "Rojo", "Amarillo", "Verde", "Morado", "Anaranjado"]
color = colores[0] #Seleccoina un solo elemento de lista (locación 0)
color1 = colores[-1] #Obtiene el último elemento de la lista
tres_colores = colores[0:3] #Selecciona varios elementos de lista o tres_colores = colores[:3]
colors = colores[2:] #Selecciona todos los indices a partir de 2
saltos = colores[0:5:2] #Selecciona los elementos de rango 0-5 con salto de 2 en 2
inv = colores[::-1] #Seleccoina la lista de manera invertida
print(color)
print(tres_colores)
print(colors)
print(saltos)
print(inv)

num = [1,15,2.4,4.7,7.9,9,7,6,4]
num.sort() #Ordena lista de forma ascendente
num.sort(reverse=True)#Ordena Descendente
print(num)
menor = min(num) #Obtener numero menor
mayor = max(num) #Obtenet numero mayor
print(menor)
print(mayor)
long = len(num) #Tamaño de lista
print(long)
res = 1 in num #Pregunta si el valor 1 esta dentro de la lista (resultado bool)
print(res)
indice = num.index(1) #locación de numero
print(indice)
conta = num.count(1)#Cuantas veces aparece 1 en la lista
print(conta)
num [4] = "3" #Modifica el valor de la locacion 0 a 3 ie de valor 7.9 a valor 3