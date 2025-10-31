#EJERCICIO 1

correo = input()

"print(correo.count('@') me cuenta la cantidad de caracteres de '@' que hay en el correo que el usuario puso"

condicion1 = correo.count('@')==1 
posicion_arroba = correo.index('@')  #saber en que posicion es el arroba
condicion2_1 = posicion_arroba >= 3 
condicion2_2 = (len(correo) - posicion_arroba) > 3
condicion3 = correo.count('.') >= 1
condicion4 = correo.count(' ') == 0
condicion5_1 = correo[0] != '.'
condicion5_2 = correo[-1] != '.'

print(condicion1 and condicion2_1 and condicion2_2 and condicion3 and condicion4 and condicion5_1 and condicion5_2)


#EJERCICIO 2
"""
cadena = input()

condicion1 = cadena.count('z')
condicion2 = cadena.lower().count('z') #le pongo lower para que haga toda la cadena minuscula porque en realidad solo le estoy dando una z minuscula 'z' y no cuenta la cantidad mayuscula.

print(condicion2)
"""

#EJERCICIO 3
"""
X = int(input())
A = input() #lapiz
B = input() #mochila

condicion_rara= A[:X:][::-1] #primero solo es las ultimas x letras de la cadena, luego se habren otros corchetes y se pone -1 en los saltos para que invierta el orden de los caracteres

condicion1 = A[:X:]
condicion2 = B[-X:]
print(condicion1 + condicion2)

variable1 = len(A)
division1 = (variable1 // X)
condicion1 = A[:division1:]


variable2 = len(B)
division2 = (variable2 // X)
condicion2 = B[-division2::]

print(condicion1 + condicion2)
"""
#EJERCICIO 4
"""
A = int(input())
B = int(input())
C = int(input())
D = int(input())

multi1 = A * B
multi2 = C * D

print(multi1 - multi2)
"""

#EJERCICIO 5

"""
dato1 = float(input())
dato2 = float(input())
dato3 = float(input())
dato4 = float(input())
dato5 = float(input())
dato6 = float(input())

lista = [dato1 , dato2 , dato3 , dato4 , dato5 , dato6]

sal1 = max(lista)
sal2 = min(lista)
sal3 = sal1 - sal2
sal4 = dato1 + dato2 + dato3 + dato4 + dato5 + dato6 #cuando tenemos datos numericos en una lista, podemos sumarlos todos usando sum(lista)
sal5 = sal4 / 6 #aqui no tiene que ser division exacta porque ya la estamos redondeando con los dos decimales. Tambien podemos dividirlo entre len(lista)

print(f"Maximo: {sal1:.2f}")
print(f"Minimo: {sal2:.2f}")
print(f"Diferencia: {sal3:.2f}")
print(f"Suma: {sal4:.2f}")
print(f"Promedio: {sal5:.2f}")
"""

#EJERCICIO 6
"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
por1 = float(input())
por2 = float(input())
por3 = float(input())
por4 = float(input())
por5 = float(input())

prom1 = num1 * por1
prom2 = num2 * por2
prom3 = num3 * por3
prom4 = num4 * por4
prom5 = num5 * por5

print(int(prom1 + prom2 + prom3 + prom4 + prom5))
"""

#EJERCICIO 7
 
"""
nom = input()
ape = input()
 
variable1 = nom[:5:] + ape[0]
Nick = variable1.lower()

Pin_1 = len(nom) * 1000 + len(ape)
Pin_2 = Pin_1 % 10000



print(f"Nick: {Nick}")
print(f"Pin: {Pin_2}")
print(f"ID: C3-{Nick}-{Pin_2}")
"""

#EJERCICIO 8

"""
F = input()

print(F[6:] + F[2:6:] + F[:2:])
"""

#EJERCICIO 9

"""
pp = ["Hamburguesa" , "Pizza" , "Tacos" , "Pupusas" , "Hotdog"]
c = ["Papas fritas" , "Alitas de pollo" , "Ensalada" , "Sopa" , "Lasaña"]

num1 = int(input())
num2 = int(input())

print(f"El pedido de Alvin es: {pp[num1-1]} con {c[num2-1]}")
"""

#EJERCICIO 10

"""
N = int(input())

multi = N * (N+1) // 2
print(multi)
"""

#EJERCICIO 1 AGAIN

correo = input()

"""con1 = correo.count('@') == 1

posi_correo = correo.index('@')
con2 = posi_correo >= 3
con2_1 = len(correo) - posi_correo > 3

con3 = correo.count('.') >= 1

con4 = correo.count(" ") == 0"""
"""
con5 = correo[0] != "."


print(con5)
"""