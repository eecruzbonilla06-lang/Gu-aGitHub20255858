#EJERCICIO 1
"""
N = int(input())

if N >= 0:
    print("Positivo")
else: 
    print("negativo")
"""  
#EJERCICIO 2
"""
Num = int(input())

con1 = Num%2


if con1 == 0:
    print(Num + 2)
    print(Num - 1)
else:
    print(Num + 1)
    print(Num - 2)
"""

#EJERCICIO 3
"""
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

prom = (n1 + n2 + n3 + n4 + n5 + n6) / 6

if prom > 9.5:
    print("Gana Premio :)")
else:
    print("No Gana Premio :(")
"""

#EJERCICIO 4
"""N = int(input())

numero5 = 0
numero7 = 0

for i in range(N):
    numeros = int(input())
    if numeros == 5:
        numero5 = numero5 + 1
    elif numeros == 7:
        numero7 = numero7 + 1
print(numero7 , numero5)"""

# EJERCICIO 5

"""n = int(input())
c = list(map(int , input().split(' ')))
pa = int(c[0])
pb = int(c[1])
pc = int(c[2])

combo = []
daño = []

for i in range(n):
    combo.append(input().upper())
    contA = combo[i].count('A')
    contB = combo[i].count('B')
    contC = combo[i].count('C')
    dañoA = contA * pa
    dañoB = contB * pb
    dañoC = contC * pc
    daño_total = dañoA + dañoB + dañoC
    daño.append(daño_total)
    
for v in daño:
    print(v)"""
    

#EJERCICIO 6

"""N = int(input())
nombres = []
for i in range(N):
    nombres.append(input())
    
for v in nombres:
    x = len(v)
    if x <= 6:
        print("No vale la pena")
    elif x >= 8:
        print("Si aguanto otro desarrollo de personaje")
    elif 6 < x < 8:
        print("Dios no creo aguantar esta vez")"""
        
#EJERCICIO 7

"""numeros = list(map(int , input().split(' ')))
x = numeros[0]
y = numeros[1]
if x < y:
    print(y)
elif y < x:
    print(x)"""
    
#EJERCICIO 8

"""A = int(input())
mayores = 0
fila = []

for n in range(A):
    fila.append(int(input()))
    
for v in fila:
    if v >= 15:
        mayores = mayores + 1

print(mayores)
"""

#EJERCICO 9

"""estado = input().lower()       

if estado == "conectado":
    print("Ola Ivan")
elif estado == "desconectado":
    print("ol...")"""
    
    
#EJERCICIO 10

"""N = int(input())

lista = []

for n in range(N):
    lista.append(int(input()))
    
    
for v in lista:
    if v >=3:
        print("Ok")
    elif v < 3:
        print("No")"""

    
    
    