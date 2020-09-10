diccionario = {} #o Diccoinario = dict ()
diccionario["nombre"] = "Miguel" #Agregar llave con valor a diccionario
#o diccionario = {"nombre": "Miguel"}
valor = diccionario["nombre"] #Obtener valor
diccionario ["nombre"] = 90
print(diccionario)
print(valor)
dic = {"a": 1, "b":2, "c":3}
res = dic.get("a")
print(res)
res = "z" in diccionario #Verifica si la llave Z se encuentra en el diccionario
print(res)
res = dic.get("z", "la llave no exite") #Segundo valor se retorna si la llave no existe
print(res)
res = dic.setdefault("z",{}) #Crea una llave "z" con valor de diccionario vacio
print(res)
res = dic.keys() #Obtener todas lsa llaves del diccoinario
print(res)
res = tuple(res) #Convuerte las llaves en una tupla
res = dic.values() #obiene valores de todas las llaes
print(res)
res = dic.items() #Obtiene llaves con su valor}
del dic["a"] #Elimina llave
dic.pop("b") #Elimina llave
val = dic.pop("c") #Obtiene ubicación de llave
print(val)
dic = {} #Vciar diccinoario
dic.clear() #Vaciar diccinoario
print(dic)