# En este modulo desarrollamos la logica para el sistema

import modulo_datos as dat

def registrar_estudiantes():
    """Funcion que valida y registra estudiante"""
    while True:
        try:
            carnet_i = int(input("Digite el numero de carnet: "))
        except:
            print("Formato inváido, por favor ingrese solo números.")
        else:
            carnet_string = str(carnet_i)
            existe = "No"
            for e in dat.estudiantes:
                if e["carnet"] == carnet_i:
                    existe = "Si"
            if len(carnet_string) >= 6 and len(carnet_string) <= 10 and existe == "No":
                break
            else:
                print("El largo debe ser mayor a 5 y menos a 11, y el carnet no debe de existir.")
    while True:
        nombre_i = input("Digite el nombre del estudiante: ")
        if len(nombre_i) > 1:
            break
        else:
            print("El largo del nombre debe ser al menos 2.")
    while True:
        apellido_i = input("Digite el apellido del estudiante: ")
        if len(apellido_i) > 1:
            break
        else: 
            print("El largo del apellido debe ser al menos 2.")    
    dat.estudiantes.append({
        "carnet":carnet_i,
        "nombre":nombre_i,
        "appellido":apellido_i
    })
    # print(dat.estudiantes)



def inscripciones():
    while True:
        carnet_es = input("Ingrese el carnet del estudiante que quiere hacer la inscripción: ")
        if carnet_es.lower() == "salir":
            print("Volviendo al menu principal...")
            break
        else:
            try:
                carnet_es_ent=int(carnet_es)
            except:
                print("Formato inválido, por favor ingrese solo números.")
            else:
                exis2 = "No"
                for es in dat.estudiantes:
                    if es["carnet"] == carnet_es_ent:
                        exis2 = "Si"
                if exis2 == "Si":
                    break
                else:
                    print("El carnet que ingresó no existe. Por favor ingrese uno existente.")
    print("""
        CÓDIGO	DESCRIPCIÓN
            PY	Python Básico
            JS	JavaScript para Principiantes
            BD	Introducción a Bases de Datos
            SE	Seguridad en Entornos Digitales
        """)
    while True:
        try:
            codigo = input("Ingrese el código del curso que quiere inscribir: ")
        except:
            print("Formato inváido, por favor ingrese solo el código")
        else:
            exis3 = "No"
            for cod in dat.cursos:
                if codigo.upper()=="PY" or codigo.upper()=="JS" or codigo.upper()=="BD" or codigo.upper()=="SE":
                    exis3 = "Si"
            if exis3 == "Si":
                if codigo.upper() == "PY":
                    tupla1 = (carnet_es_ent,codigo.upper())
                    dat.lista_py.append(tupla1)
                    dat.carnets_ins.append(carnet_es_ent)
                    break
                elif codigo.upper() == "JS":
                    tupla2 = (carnet_es_ent,codigo.upper())
                    dat.lista_js.append(tupla2)
                    dat.carnets_ins.append(carnet_es_ent)
                    break
                elif codigo.upper() == "BD":
                    tupla3 = (carnet_es_ent,codigo.upper())
                    dat.lista_bd.append(tupla3)
                    dat.carnets_ins.append(carnet_es_ent)
                    break
                elif codigo.upper() == "SE":
                    tupla4 = (carnet_es_ent,codigo.upper())
                    dat.lista_se.append(tupla4)
                    dat.carnets_ins.append(carnet_es_ent)
                    break
            
            else:
                print("El código que ingresó no existe. Por favor ingrese uno existente.")
    
    tupla = (dat.lista_py,dat.lista_js,dat.lista_bd,dat.lista_se)
    dat.inscritos.append(tupla)
    print(dat.inscritos)
    

def reporte():
    while True:
        if len(dat.inscritos) == 0:
            print("Actualmente no hay inscripciones.")
            break
        else:
            print("""
                1.	PY
                2.	JS
                3.	BD
                4.	SE
                5.	Estudiantes sin inscripción
                """)
            try:
                opcion = int(input("Por favor ingrese una opción: "))
            except:
                print("Formato inválido. Por favor ingrese solo números")
            else:
                if opcion >= 1 and opcion <= 5:
                    if opcion == 1:
                        if len(dat.lista_py) == 0:
                            print("No hay estudiantes inscritos en este curso")
                            break
                        else:
                            print(dat.lista_py)
                            break
                    elif opcion == 2:
                        if len(dat.lista_js) == 0:
                            print("No hay estudiantes inscritos en este curso")
                            break
                        else:
                            print(dat.lista_js)
                            break
                    elif opcion == 3:
                        if len(dat.lista_bd) == 0:
                            print("No hay estudiantes inscritos en este curso")
                            break
                        else:
                            print(dat.lista_bd)
                            break
                    elif opcion == 4:
                        if len(dat.lista_se) == 0:
                            print("No hay estudiantes inscritos en este curso")
                            break
                        else:
                            print(dat.lista_se)
                            break 
                    elif opcion == 5:
                        no_inscritos = []
                        cuenta_estudiantes_no_inscritos = 0
                        for comprobar in dat.estudiantes:
                            if comprobar["carnet"] not in dat.carnets_ins:
                                no_inscritos.append(comprobar["carnet"])
                                cuenta_estudiantes_no_inscritos = cuenta_estudiantes_no_inscritos + 1
                                break
                        if cuenta_estudiantes_no_inscritos == 0:
                            print("Actualmente, todos los estudiantes están inscritos en un curso")
                        elif cuenta_estudiantes_no_inscritos > 0:
                            print(no_inscritos)
                            break


def salir():
    print("Muchas gracias por haber usado este programa.")
    return

