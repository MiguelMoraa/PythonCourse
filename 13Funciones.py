def saluda():
    print("Hola Mundo")
saluda()

def crear_mensaje(nombre):
    return "Hola {}, bienvenido al curso".format(nombre)
print(crear_mensaje("Miguel"))

def suma(v1 ,v2, v3):
    return v1 + v2 + v3
print(suma(10, 20, 30))

def tipo_curso():
    return "Pyhon", "Basic" , 3
lenguaje, nivel, version = tipo_curso()
print (lenguaje, nivel, version)

def crear_usuario(nombre="", apellido="", edad=27): #Asignacoin de valores por default en parámetros es opcional
    return{
        "nombre": nombre,
        "apellido": apellido,
        "nombre_completo" : "{} {}".format(nombre, apellido),
        "edad": edad
    }
info = crear_usuario("Miguel", "Mora")
info2= crear_usuario(apellido= "Hernández")
print(info["nombre_completo"]) #Imprimir parámetro en especifico de función
print(info["edad"])
print(info2)

def add(parametro_requerido, *args): #Funcion para cuando no se sabe cuántos parámetros necesita
    total = 0
    print(parametro_requerido)
    for valores in args:
        total += valores
    return total
print(add("Este es un argumento requerido",10,20,30,40,50,60,70,80,90,100))

def usuarios_autenticados(**kwargs):
    print(kwargs)
usuarios_autenticados(Miguel= True, Mora= False) #Agrupa valores en un diccoinario

def func_combinada(requerido,*args, **kwargs):
    print(requerido)
    print(args)
    print(kwargs)
func_combinada("Valor requerido", 10,11, val1=True, val2=False)

def mi_func(parametro):
    if parametro:
        return 100

resultado = mi_func("a")
if resultado:
    print("El resultado no es None")

animal = "León" #Definida como variable global
animales = "Delfin"

def cuadrado(numero):
 return numero * numero

lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)

lista_resultado = list(resultado)
print(lista_resultado)

def mos_animal():
    global animales
    animales = "Aguila"
    animal = "Jirafa" #Definida como variable local
    print(animal)
    print(animales)
mos_animal()
print (animal)
print(animales)

def calc_grados(grados):
    return grados * 1.8 + 32
func_var = calc_grados
print(func_var(32))

mi_funcion = lambda grados=0 : grados * 1.8 +32 #Funcion express
res = mi_funcion(32)
print(res)

def playlist(lista):
    def reproduce():
        nonlocal lista #modifica el valor de la variables
        lista= [1, 2, 3, 4]
        for val in lista:
            print(val)
    reproduce()
lista = ["Track 1","Track 2", "Track 3", "Track 4"]
playlist(lista)

def mos_mens(mensaje):
    mensaje= mensaje.title()
    def mos():
        print(mensaje)
    return mos
var_func = mos_mens("Miguel Mora")
var_func()

def decorador(funcion):
    def nueva_func(*args,**kwargs):
        print("Podemos agregar código antes")
        resultado = funcion(*args,**kwargs)
        print("Podemos agregar código después")
        return resultado
        #pass #Funcion no hará nada
    return nueva_func 
@decorador
def func_decorar():
    print("Esta es una función a decorar")
func_decorar()

@decorador
def suma(val1, val2):
    return val1 + val2
resultado = suma(10,20)
print(resultado)

def tab_mult(num_tab, veces=10):
    for posicion in range(1, veces + 1):
        yield num_tab * posicion, num_tab, posicion

for res, posicion, num_tab in tab_mult(9,20):
    print(posicion,"*",num_tab,"=" ,res)