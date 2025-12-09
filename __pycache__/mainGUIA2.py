#Este es el inicio de mi sistema

#Importamos los modulos necesarios
import modulo_funciones as fn



while True:
    print("""
    --- MENU PRINCIPAL ---
    1. Registrar estudiante
    2. Inscribir en curso
    3. Generar reportes
    4. Salir
    """)
    try:
        opcion = int(input("Elija una opcion [1-4]: "))
    except:
        print("Formato inválido. Por favor escriba solo números.")
    else:
        if opcion >= 1 and opcion <= 4:
            if opcion == 1:
                fn.registrar_estudiantes()
                
            elif opcion == 2:
                fn.inscripciones()
             
            elif opcion == 3:
                fn.reporte()
               
            elif opcion == 4:
                fn.salir()
                break
            else:
                print("Por favor seleccione una de las opciones del 1 al 4")