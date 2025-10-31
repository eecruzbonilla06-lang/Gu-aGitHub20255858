#Ejercicio 4

control1 = float(input("Ingrese la nota del control 1: "))
parcial1 = float(input("Ingrese la nota del parcial 2: "))
control2 = float(input("Ingrese la nota del control 2: "))
parcial2 = float(input("Ingrese la nota del parcial 2: "))
tarea_practica = float(input("Ingrese la nota de la tarea practica: "))

print(f"La nota final es: {(control1*0.15+parcial1*0.4+control2*0.25+parcial2*0.2+tarea_practica*0.05):.2f}")