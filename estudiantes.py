def registrar_estudiante(lista_estudiante): #creamos una funcion para registrar a los estudiantes
    nombre_estudiante = input("Ingrese el nombre del estudiante: ").capitalize() #para ingresar el nombre del estudiante
    carnet = len(lista_estudiante) + 1 #creamos esta variable para asociar la posición del estudiante con el numero de carnet
    carnet_estudiante = f"S{carnet:03d}" #aqui ya creamos el carnet del estudiante con la variable anterior
    
    dic_estudiantes = {
        "estudiante": nombre_estudiante,
        "carnet": carnet_estudiante,
        } #creamos el diccionario de estudiantes donde relacionamos los valores
    
    lista_estudiante.append(dic_estudiantes) #aqui vamos agregando a la lista de estudiantes cada estudiante registrado
    print("El nuevo estudiante ha sido registrado exitosamente")
    print() #esto es nada mas para hacer mas estético todo. Genera un espacio de por medio
    
def mostrar_estudiantes(lista_estudiantes): #aqui creamos otra funcion ´para mostrar la lista de estudiantes
    print("LISTA DE ESTUDIANTES:")
    print()
    for estudiante in lista_estudiantes: #este bucle es para que imprima cada estudiante con sus valores asociados
        print(
            f"Carnet: {estudiante['carnet']} "
            f"Estudiante: {estudiante['estudiante']} "
        )

            
    