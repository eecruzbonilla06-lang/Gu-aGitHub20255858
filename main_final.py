#En este modulo vamos a desarrollar el menu

import modulo_funciones as fun

def menu():
    while True:
        print("""
              MENU
            1. Registrar cliente
            2. Registrar pedido
            3. Ver reportes
            4. Salir
            """)
        try:
            decision = int(input("Por favor seleccione una opcion [1-4]: "))
        except:
            print("Formato no valido. Por favor ingrese solo numeros.")
        else:
            if decision == 1:
                fun.registro_clientes()
            if decision == 2:
                fun.sabores_disponibles()
            if decision == 3:
                fun.generar_reporte()
            if decision == 4:
                break 
            else:
                print("Por favor escribir una de esas opciones.")
