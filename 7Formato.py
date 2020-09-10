texto = "este es un texto"
res = texto.capitalize() #Genera string con primer letra en mayuscula
print(res)
res = texto.swapcase() #Cambia de may a min y viceveza
print(res)
print(texto.upper()) #Todo mayusculas
print(texto.lower()) #Todo minusculas
print(texto.title()) #Formato de titulo
print(texto.replace("este", "Hola",1)) #Remplaza elemento del string lo remplazará solo 1 vez (Opción   )
print(texto.strip()) #Elimina espacio del inicio y fin del texto
print(res.islower()) #pregunta si esta todo en min (bool)
print(res.isupper()) #pregunta si todo esta en may (bool)

curso = "Python"
version = "3"
resultado = "Curso de %s %s" %(curso, version)
print(resultado) #Imprime "Curso de Python 3"
resu =  "Curso de {a} {b}".format(a = curso,b = version)
print(resu) #Imprime "Curso de Python 3"
