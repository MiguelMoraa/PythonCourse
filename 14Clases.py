class Usuario:
    def __init__(self, username= "", email="", nombre= ""):
        self.username = username
        self.email = email
        self.nombre = nombre
    def saluda(self):
        return "Hola soy un usuario, " + self.username
    def mos_username(self):
        print(self.username)
    def mos_nombre(self):
        print(self.nombre)

miguel = Usuario("Miguel","miguelmoraa@icloud.com", "Mora")
mora = Usuario("ok", "ok","ok")
res = mora.saluda()
resultado = miguel.saluda()
print(resultado)
print(res)

class Circulo:
    pi = 3.141516 #Variable de clase (mismo valor para todos los objetos)
    def __init__(self, radio):
        self.radio = radio #Es unna variable de instancia (difernte valor a cada instancia)

cir_a = Circulo(100)
cir_b = Circulo(200)

cir_b.radio = 100

print(cir_a.radio)
print(cir_b.radio)

print(cir_a.pi)
print(cir_b.pi)
print(Circulo.pi)

class Triangulo:
    numero = 2
    @staticmethod
    def area(base, altura):
        return (base * altura) / Triangulo.numero

resultado = Triangulo.area(10,20)
print(resultado)

class Cir:
    pi = 3.141516
    pot = 2
    @classmethod
    def area(cls, radio):
        return cls.pi * radio**Cir.pot

res = Cir.area(10)
print(res)

class Animal: #Clase padre
    def comer(self):
        print("Comiendo")
    def dormir(self):
        print("Durmiendo")
    def comun(self):
        print("Este es un metodo de Animal")

class Mascota:
    def fecha_adopt(self, fecha):
        self.fecha_de_adopt = fecha
        def comun(self):
            print("Este es un metodo de Mascota")

class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre
    def ladrar(self):
        print("Ladrando")
    def comun(self):
        print("Este es un metodo de Perro")
    def dormir(self):
        print(self.nombre, "está duminedo!")
        Animal.dormir(self)
        print("No molestar")

class Gato(Animal, Mascota):
    def ronronear(self):
        print("Ronroneando")
    def comun(self):
        print("Este es un metodo de Gato")

firulais = Perro("Frulais")
firulais.ladrar()
firulais.comer()
firulais.dormir()
firulais.fecha_adopt("Hoy")
print(firulais.fecha_de_adopt)
firulais.comun()

misifuz = Gato()
misifuz.comer()
misifuz.dormir()
misifuz.ronronear()

class Gato_2:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre

class Pato(object):
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre

gato = Gato_2("Misiuz")
gato.edad = 6
pato = Pato("Donald")
print(gato.__dict__)
print(pato.__dict__)