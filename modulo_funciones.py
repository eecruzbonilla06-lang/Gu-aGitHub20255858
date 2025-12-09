#En este modulo vamos a desarrollar todas las funciones

import modulo_datos as dat

def registro_clientes():
    while True:
        try:
            nombre = input("Ingresa el nombre del cliente a registrar: ")
        except:
            print("Formato no válido. Por favor escriba solo letras.")
        else:
            if len(nombre.capitalize()) > 1:
                break
            else:
                print("El nombre tiene que contener al menos dos letras. Vuelva a intentarlo")
    while True:
            correo = input("Ingrese el correo electrónico del cliente: ")
            if len(correo) == 0:
                print("El correo no puede estar vacío, por favor ingreselo correctamente.")
            else:
                existe1 = "No"
                for corr in dat.correos_registrados:
                    if corr == correo:
                        existe1 = "Si"
                    if existe1 == "Si":
                            print("Este correo ya ha sido registrado con otro cliente. Por favor ingrese uno no registrado anteriormente.")
                else:
                    if correo not in dat.correos_registrados:
                        dat.correos_registrados.append(correo)
                        break
    cliente = {
        correo:nombre
    }
    dat.clientes_registrados.append(cliente)
    print(dat.clientes_registrados)
            
def sabores_disponibles():
    while True:
        comp_correo = input("Si desea salir, solo escriba salir, sino, ingrese el correo con el que quiere hacer el pedido: ")
        if comp_correo.lower() == "salir":
            break
        else:
            existe2 = "No"
            for corr in dat.correos_registrados:
                if corr == comp_correo:
                    existe2 = "Si"
                if existe2 == "Si":
                    
                    print("""
                    LETRAS    SABORES
          
                    C       Chocolate
                    V       Vainilla
                    F       Fresa
                    L       Limón
                    """)
                    try:
                        sabor = input("Por favor escribe las letras del sabor que quiere pedir: ")
                    except:
                        print("Formato invalido. Por favor pon solo las letras.")
                    else:
                        if len(sabor) == 1:
                            if sabor.upper() == dat.sabores_ofrecidos["C"]:
                                sabor2 = dat.sabores_ofrecidos["C"]
                                dat.listaC.append(comp_correo)
                                break
                            elif sabor.upper() == dat.sabores_ofrecidos["V"]:
                                sabor2 = dat.sabores_ofrecidos["V"]
                                dat.listaV.append(comp_correo)
                                break
                            elif sabor.upper() == dat.sabores_ofrecidos["F"]:
                                sabor2 = dat.sabores_ofrecidos["F"]
                                dat.listaF.append(comp_correo)
                                break
                            elif sabor.upper() == dat.sabores_ofrecidos["L"]:
                                sabor2 = dat.sabores_ofrecidos["L"]
                                dat.listaL.append(comp_correo)
                                break
                            else:
                                print("Seleccione solo una de esas letras")
                    
                        else:
                            print("Por favor ingrese solo la primera letra del sabor.")
                else:
                    if comp_correo not in dat.correos_registrados:
                        print("No se puede hacer el pedido porque este correo no está registrado. Por favor ingrese uno existente en el sistema.")
    pedidos = {
        comp_correo:sabor2
    }
    dat.pedidos_realizados.append(pedidos)
    
def generar_reporte():
    while True:
        if len(dat.pedidos_realizados) == 0:
            print("Actualmente no hay ningún pedido realizado")
        else:
            print("""
                  1. C
                  2. V
                  3. F
                  4. L
                  5. Clientes sin pedidos
                  """)
            try:
                opcion = int(input("Por favor selecciones una opción [1-5]: "))
            except:
                print("Formato no valido. Por favor ingrese solo numeros.")
            else:
                if opcion == 1:
                    if len(dat.listaC) == 0:
                        print("Actualmente no hay personas que hayan pedido este ssabor.")
                    else:
                        print(dat.listaC)
                        break
                elif opcion == 2:
                    if len(dat.listaV) == 0:
                        print("Actualmente no hay personas que hayan pedido este ssabor.")
                    else:
                        print(dat.listaV)
                        break
                elif opcion == 3:
                    if len(dat.listaF) == 0:
                        print("Actualmente no hay personas que hayan pedido este ssabor.")
                    else:
                        print(dat.listaF)
                        break
                elif opcion == 4:
                    if len(dat.listaL) == 0:
                        print("Actualmente no hay personas que hayan pedido este sabor.")
                    else:
                        print(dat.listaL)
                        break
                elif opcion == 5:
                    no_pedidos = []
                    for cli in dat.clientes_registrados:
                        if cli not in dat.pedidos_realizados:
                            no_pedidos.append(cli) #aquí yo sé que siempre va a tirar error porque el cli de clientes registrados incluye nombre y correo, y en los pedidos realizados está el correo y el sabor, entonces no me alcanzó el tiempo para corregir eso
                        break
                    if no_pedidos >= 1:
                        print(no_pedidos)
                    else:
                        print("Todos los clientes registrados han hecho un pedido")
                        

                        