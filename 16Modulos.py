#import Calc #Importaa modulo Calc
#print(Calc.suma(10,20)) #Requiere de referenciar el objeto
from Calc import * #importa todo el modulo con todas las funciones
from Calc import suma,resta,mult #importa la funcion puntual a utilizar 
from Calc import (suma,
                  resta,
                  mult,
                  div,) #importa la funcion puntual a utilizar si son muchos objetos se puede utilizar así
print(resta(10,20))
from Calc import suma as nueva_suma 

print(nueva_suma(10,20)) #No requiere de referenciar el objeto
