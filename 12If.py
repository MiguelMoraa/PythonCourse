color = 'verde'
if color == 'verde':
    print("Siga")
elif color == 'amarillo':
    print("Precaución")
else:
    print("Alto")

numero = 123456789
contador = 0
while numero >= 1:
    contador += 1 #inclrementa valor de 1 en 1 (con singo - en decrementar)
    numero = numero / 10
else:
    print("La cantidad de digitos es ",contador) #Finaliza el ciclo e imprime el mensaje

numeros = [1,2,3,4,5,6,7,8,9]
for i in numeros:
    print(i)

val = {"a":1,"b": 2}
for llave in val:
    print(llave)

valor = ((1, 2), ["strings", "Strings"], (True, False))
for a, b in valor:
    print(a, b)

for valor in range(1,10,2): # 1 es el valor donde comenzara el conteo, 2 son los saltos del conteo
    print(valor)

lista = [1,2,3,4,5]
for j, k in enumerate(lista,1): #El 1 uno es que comenzara a pratir de allí
    print("indice", j , "Valor", k)

mensaje = "Mi nombre completo"
for char in mensaje:
    if char == "c":
        break
    if char == "b":
        continue
    print(char)

calif = 5
color = None
if calif >= 7:
    color = "Verde"
else:
    color = "Rojo"

print(calif, color)

calificacion = 7
clr = "Verde" if calificacion >= 7 else "Rojo"
print(calificacion, clr)