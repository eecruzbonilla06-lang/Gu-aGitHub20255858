def registrar_prestamo(lista_libros , lista_estudiantes , lista_prestamos): #creamos una funcion para registrar los prestamos
    pedir_carnet = input("Ingrese el carnet del estudiante: ").upper() #pedimos que ingrese el carnet del estudiante que quiere hacer el préstamos
    comp_carnet = False 
    for estudiante in lista_estudiantes: #creamos este for para cada estudiante de la lista de estudiantes
        if estudiante['carnet'] == pedir_carnet: #aqui indica que si el estudiante del carnet que se ingrese coincide con uno ya guardado, sucede lo siguiente:
            comp_carnet = estudiante
            
    if comp_carnet is False: #si el carnet ingresado no coincide con ninguno anteriormente guardado, imprime que el estudiante no existe
        print("El estudiante no existe.")
        print()
        return #esto es para que termine si el carnet no existe
    pedir_codigo = input("Ingrese el codigo del libro: ").upper() #aqui pide el codigo del libro que se va a prestar
    
    comp_libro = False
    for libro in lista_libros: #creamos este for para cada libro en la lista de los libros
        if libro['codigo'] == pedir_codigo: #si el codigo ingresado coincide con uno ya antes registrado, sucede lo siguiente:
            comp_libro = libro

    if comp_libro is False: #si el codigo ingresado no coincide con ninguno antes registrado, se imprimirá que el libro no existe
        print("El libro no existe.")
        print()
        return #esto hace que termine 
    if not libro["disponible"]: #si el libro ya se presto a alguien mas antes, se va a imprimir que el libro no esta disponible
        print("El libro no esta disponible.")
        print()
        return #esto hace que termine
    if libro["disponible"]: #si el libro si esta disponible, pasa lo siguiente:
        fecha = input("Ingrese la fecha del prestamos en formato DD/MM/AAA: ") #le pide que ingrese la fecha en la que se esta haciendo el prestamos
        dic_prestamo = {
        "carnet_estudiante": pedir_carnet,
        "codigo_libro": pedir_codigo,
        "fecha": fecha
        } #se crea el diccionario de los libros prestados
    lista_prestamos.append(dic_prestamo) #se agrega a la lista de los prestamos
    libro["disponible"] = False #se marca como que ya no está disponible pq se ha realizado exitosamente el prestamo
    
    print("El prestamo se ha realizado exitosamente.") #mensaje que tira cuando ya se realizo exitosamente el prestamo
    print()
    
def mostrar_prestamo(lista_prestamos): #creamos otra funcion para mostrar el listado de los prestamos
    print("LISTA DE PRESTAMOS:")
    print()
    for prestamo in lista_prestamos: #este for para que suceda la siguiente en cada prestamo de la lista:
        print(
            f"Carnet: {prestamo['carnet_estudiante']} "
            f"Codigo del libro: {prestamo['codigo_libro']} "
            f"Fecha: {prestamo['fecha']} "
        )#imprime la informacion acorde al diccionario anteriormente creado

    
            
