"""#Vamos a jugar

aprobacion = True

while aprobacion: #aquí es mientras tu aprobacion sea positiva, se va a seguir repitiendo el ciclo de preguntar, hasta que pongamos n que significa que ya no queremos jugar
    eleccion = input("Quieres seguir jugando? (Y/N)")
    if eleccion.lower() == "n":
        aprobacion = False 
    elif eleccion.lower() == "y":
        print("Me alegra que quieras seguir jugando!")
    else: 
        print("La opcion elegida no es valida.")"""
        
        
"""#Una aplicación para registrar alumnos

alumnos = []

for a in range(3):
    alumno = input("Digite el nombre: ")
    alumnos.append(alumno)
    
print(alumnos)"""

#Sistema de gestion de alumnos

menu_iniciado = True 
alumnos = []

while menu_iniciado:
    """print("Demole")
    menu_iniciado = False"""#no entendi esto
    opcion = int(input("1.Apregar, 2.Consultar, 3.Modifical, 4.Borrar, 5.Salir"))
    if opcion == 5:
        menu_iniciado = False
    elif opcion == 1:
        alumnos.append(input("Digite el nombre del alumno: "))
        print(alumnos)
    elif opcion == 2:
        for a in alumnos:
            print(a)
    elif opcion == 3:
        indice = int(input("Digite el numero del alumno (1-3)"))
        nuevo = input("Digite el nombre nuevo: ")
        alumnos[indice-1] = nuevo 
    elif opcion == 4:
        indice = int(input("Digite el numero del alumno (1-3) a proponer"))
        alumno_borrado = alumnos.pop(indice-1)
        print(f"Hemos borrado a: {alumno_borrado}")
        
        
print("Gracias por usar nuestro sistema")