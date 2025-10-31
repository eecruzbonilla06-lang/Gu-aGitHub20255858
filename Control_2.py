#Ejercicio 1

"""
menu = ["Hamburguesa" , "Hotgo" , "Pizza" , "Tacos" , "Lasaña" , "Ensalada" , "Pupusas" , "Burrito" , "Alitas de pollo" , "Papas fritas"]

elección = int(input("Ingrese el numero del plato en el menu: "))

print(f"El plato seleccionado por Alvin es: {menu[elección-1]}")

"""
#Ejercicio 2
"""
precios = ["1. Hamburguesa: $3.52" , "2. Hotgo: $55.15" , "3. Pizza: $4.25" , "4. Tacos: 60.25" , "5. Lasaña: $5.65 " , "6. Ensalada: $3.25" , "7. Pupusas: $2.65" , "8. Burrito: $70.75" , "9. Alitas de pollo: $6.25" , "10. Papas fritas: $2.55"]
print(precios)

plato_a_corregir = int(input("Ingrese el numero de plato al que quieres cambiar el precio: "))
plato_a_corregir = plato_a_corregir-1

nuevo_precio = float(input("Ingrese el precio actualizado: "))

precios[plato_a_corregir] = nuevo_precio

print(f"Los precios actualizados son: {precios} ")
"""

#Ejercicio 3
"""
correo = input("Ingrese el correo a validar: ")

print(f"El correo contiene exactamente un @: {correo.count("@") == 1}")
print(f"El @ esta ubicado al inicio: {correo[0]=="@"}")
print(f"El @ esta ubicado al final: {correo[-1]=="@"}")
"""

#Ejercicio 4
"""
control1 = float(input("Ingrese la nota del control 1: "))
parcial1 = float(input("Ingrese la nota del parcial 2: "))
control2 = float(input("Ingrese la nota del control 2: "))
parcial2 = float(input("Ingrese la nota del parcial 2: "))
tarea_practica = float(input("Ingrese la nota de la tarea practica: "))

print(f"La nota final es: {(control1*0.15+parcial1*0.4+control2*0.25+parcial2*0.2+tarea_practica*0.05):.2f}")
"""

#Ejercicio 5

M = int(input("Ingrese el entero M: "))
B = input("Ingrese string B: ")
S = int(input("Ingrese el entero S: "))
A = input("Ingrese string A: ")

contraseña_parte_1 = A[::S]

mitad = contraseña_parte_1 + "_Alvin"


contraseña_parte_2 = B*S

print(f"La contraseña es: {mitad+contraseña_parte_2}")



