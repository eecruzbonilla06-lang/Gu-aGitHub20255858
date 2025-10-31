#Ejercicio 3

correo = input("Ingrese el correo a validar: ")

print(f"El correo contiene exactamente un @: {correo.count("@") == 1}")
print(f"El @ esta ubicado al inicio: {correo[0]=="@"}")
print(f"El @ esta ubicado al final: {correo[-1]=="@"}")