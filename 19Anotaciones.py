def saluda(nombre: str) -> None: #str sirve como anotacion para informar que tipo de valor está recibiendo la función y ña fllecha el tipo de dato a retornar en este caso NONE
    print ("Hola, " + str(nombre))

def suma (v1: int, v2: int=100)-> int:
    return v1 + v2

saluda("Miguel")

print(suma(10))