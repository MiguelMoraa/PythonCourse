tupla = (1,2,3,4,5,6,7,8,9,0)
lista = [10, 20, 30 , 40]
uno, dos, tres, *cuatro = tupla #Uso de * es para almacenar multiples varaibles en un registro (lista)
print(uno)
print(dos)
print(tres)
print(cuatro)
res = zip(tupla, lista) #Regresa un objeto tipo Zip
res = tuple (res) #Hacer una tupla con 2 elementos
res = list(res)# Hecar una lista con 2 elementos
print(res)
mensaje = ("Este", "es", "un", "mensaje", "del", "curso", "Tupla ORG")
mensaje_dos = ["Este", "es", "un", "mensaje", "del", "curso", "Lista ORG"]
new_list = list(mensaje)
new_tulpe = tuple (mensaje_dos)
print(new_list)
print(new_tulpe)
mens = "Curso Tuplas y Listas"
string = list(mens)
string_2 = tuple(mens)
print(string)
print(string_2)
