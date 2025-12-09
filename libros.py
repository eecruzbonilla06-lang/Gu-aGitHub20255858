def registrar_libros(lista_libros): #aqui abrimos la primera funcion que es para registrar libros
    titulo_libro = input("Ingrese el titulo del libro: ").title() #pedimos el titulo del libro
    autor_libro = input("Ingrese el autor del libro: ").title() #pedimos el autor del libro
    numero = len(lista_libros) + 1 #creamos la variable numero para recolectar el código posteriormente
    codigo_libro = f"L{numero:03d}" #aqui recolectamos el codidigo y le ponemos el :03d para que no quede cerrado a llegar hasta L009, y asi pueda pasar hasta L234, por ejemplo
    
    dic_libros = {
        "codigo": codigo_libro,
        "titulo": titulo_libro,
        "autor": autor_libro,
        "disponible": True
        } #creamos el diccionario de los libros, donde relacionamos el codigo, el titulo, el autor y su estado
    
    lista_libros.append(dic_libros) #aqui agregamos cada elemento del diccionaro a la lista de libros
    print("El nuevo libro ha sido registrado exitosamente")
    print()
    
def mostrar_libros(lista_libros): #creamos la siguiente funcion para mostrar la lista de libros
    print("LISTA DE LIBROS:")
    print()
    for libro in lista_libros:
        if libro["disponible"]:
            print(
                f"Codigo: {libro['codigo']} "
                f"Titulo: {libro['titulo']} "
                f"Autor: {libro['autor']} "
                f"Estado: Disponible "
            ) #todo esto si el libro está disponible
        else:
            print(
                f"Codigo: {libro['codigo']} "
                f"Titulo: {libro['titulo']} "
                f"Autor: {libro['autor']} "
                f"Estado: Prestado "  #esto si el libro ya ha sido prestado antes y no esta disponible
                )
            
    