colores = "Azul; Rojo; Amarillo; Verde; Morado; Anaranjado"
separador = "; "
res = colores.split(separador) #Generar una lista aaprtir de un string
print(res)
nuevo_string = ", ".join(res) #Genera un string apartir de una lista con un coma y espacio de separador
print(nuevo_string)
texto_salto = """"Este 
                  es
                  un 
                  texto 
                  con 

                  salto
                  de
                  linea"""
resultado = texto_salto.splitlines() #Genera una lista con texto con salt de lineas
print(resultado)
