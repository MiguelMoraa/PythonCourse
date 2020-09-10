mensaje = "Hola que tal, me llamo Miguel Angel"
res = mensaje.count("Miguel") #Cuenta cunatas veces aparece el string dentro del texto
print(res)
res = "Miguel" in mensaje #Verifica si aparece el string en el texto (bool)
print(res)
res = mensaje.find("Miguel") #Verifica locacion de la primer letra en el string
print(res)
res = mensaje[res: res + len("Miguel")] #Extrae string del mensaje
print(res)
res = mensaje.startswith("Hola") #Indica string con que inicia el texto (bool)
print(res)
res = mensaje.endswith("Angel") #identifica con que termina un texto
print(res)
