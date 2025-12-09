from libros import registrar_libros, mostrar_libros #aqui hacemos uso de la modularidad llamando a funciones de otros archivos.py
from estudiantes import registrar_estudiante, mostrar_estudiantes
from prestamos import registrar_prestamo, mostrar_prestamo


lista_libros = [] #la lista vacia de libros en la cual se iran almacenando todos los libros registrados
lista_estudiantes = [] #la lista vacia de estudiante en la cual se iran almacenando todos los estudiantes registrados
lista_prestamos = [] #la lista vacia de prestamos en la cual se iran almacenando todos los prestamos registrados

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar libro")
        print("2. Registrar estudiante")
        print("3. Registrar préstamo")
        print("4. Mostrar libros")
        print("5. Mostrar estudiantes")
        print("6. Mostrar préstamos")
        print("7. Salir")#mostramos todo el menu (las opciones disponibles)
        print()
        opcion = input("Seleccione una opción: ") #input para que ingrese el numero de la opcion que quiere ejecutar

        if opcion == "1": #si escoge la opcion 1, sucede lo siguiente:
            registrar_libros(lista_libros)
        elif opcion == "2": #si escoge la opcion 2, sucede lo siguiente:
            registrar_estudiante(lista_estudiantes)
        elif opcion == "3": #si escoge la opcion 3, sucede lo siguiente:
            registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos)
        elif opcion == "4": #si escoge la opcion 4, sucede lo siguiente:
            mostrar_libros(lista_libros)
        elif opcion == "5": #si escoge la opcion 5, sucede lo siguiente:
            mostrar_estudiantes(lista_estudiantes)
        elif opcion == "6": #si escoge la opcion 6, sucede lo siguiente:
            mostrar_prestamo(lista_prestamos)
        elif opcion == "7": #si escoge la opcion 7, sucede lo siguiente:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.") #cuando se ingresa una opcion que no existe 

menu()
