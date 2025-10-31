#Ejercicio 5

M = int(input("Ingrese el entero M: "))
B = input("Ingrese string B: ")
S = int(input("Ingrese el entero S: "))
A = input("Ingrese string A: ")

contraseña_parte_1 = A[::S]

mitad = contraseña_parte_1 + "_Alvin"


contraseña_parte_2 = B*S

print(f"La contraseña es: {mitad+contraseña_parte_2}")
