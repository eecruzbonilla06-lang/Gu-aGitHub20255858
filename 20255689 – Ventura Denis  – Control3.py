seguir = True #Variable que mantendrá todo el sistema funcionando hasta que se elija la opción de salir
agente = 'encargado' #Varaible que permitirá acceder al sistema
platillo= [] #Lista de platillos
precios = [] #Lista de precios
comp= input('Favor ingrese nombre del agente: ') #Variable que se usará para comprobar que el agente seleccionado sea el correcto
print() #Este y todos los "print()" fueron colocados por estética
while comp != agente: #Comprobación que se repetirá hasta que el agente seleccionado sea el correcto
    print('Agente no registrado') #Mensaje a mostrar en caso el agente seleccionado sea incorrecto
    print()
    comp= input('Favor ingrese nombre del agente: ') #Pedir ingresar nuevo nombre de agente
    print()

while seguir: #Mientras la variable "seguir" siga siendo True, todo el sistema seguirá funcionando
    print("1. Creación de platillos") #Opción 1
    print("2. Consulta de platillos y precios") #Opción 2
    print("3. Colocar un pedido") #Opción 3
    print("4. Salir") #Opción 4
    print()
    opcion= int(input("Elija una de las opciones (1-4): ")) #Variable que recibirá la opción elegida por el usuario
    if opcion == 4: #Opción elegida: salir
        print()
        print('Gracias por usar este programa, feliz día :) ') #Mensaje de despedida
        seguir = False #Termina la condición que mantiene activo todo el programa, por lo tanto, termina acá.
    elif opcion == 1: #Opción elegida: Creación de platillos
        print()
        platillo.append(input('Ingrese el nombre del platillo a crear: ').capitalize()) #Se añadirá al final de la lista "platillos" en formato capitalizado
        precios.append(float(input('Ingrese el precio del platillo a crear: '))) #Se añadirá el precio al final de la lista "precios" en formato decimal
        
        print()
    elif opcion ==2: #Opción elegida: 2
        print()
        if len(platillo)<=0: #Verificación de si hay platillos ingresados o no
            print('Actualmente no hay platillos ingresados') #Mensaje a mostrar en caso no hayan platos ingrasados
            print()
        else:
            for i in range(len(platillo)): #Bucle donde la variable "i" tomará el valor 0 hasta la cantidad total de platos añadidos (contada con el comando len())
                print(f"{platillo[i]}: ${precios[i]}") #Imprime todos los platos con sus precios respectivos en una línea para cada uno hasta que se termine el bucle
            print()
    elif opcion ==3: #Opción elegida: 3
        print()
        if len(platillo)>0: #Comprobación en caso haya o no platillos ingresados
            platoelegido = input('Indique el nombre del platillo para su orden: ').capitalize() #Elegir el nombre de platillo en formato capitalizado para que concuerde con la lista "platillos"
            print()
            if platoelegido in platillo: #Verificación que el platillo elegido se encuentre en la lista
                posicionplato = platillo.index(platoelegido) #Variable que contendrá la posición del platillo elegido
                print(f"Usted ha elegido {platoelegido.lower()} con un precio de ${precios[posicionplato]}") #Imprime el plato elegido en minúsculas y el precio usando la posición del platillo respectivo para la lista "precios"
                print()
            else:
                print('El platillo ingresado no es válido') #Mensaje a mostrar en caso el plato ingresado no esté en la lista
                print()
        else:
            print('Actualemente no hay platillos ingresados') #Mensaje a mostrar en caso se verifique que no hay platillos añadidos en la lista
            print()
    else:
        print()
        print('La opción elegida no es válida') #Mensaje a mostrar en caso la opción elegida no se encuentre entre 1-4 (por lo tanto, no es válida)
        print()