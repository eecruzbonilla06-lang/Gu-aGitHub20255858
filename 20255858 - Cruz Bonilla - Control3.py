agente = "encargado" #Esta es la variable agente que tiene el valor de encargado
comproba = input("Favor ingrese nombre del agente: ").lower() #Puse esta variable para que sea lo primero que pida antes de entrar al bucle de comprobación. Así mismo, le puse lower para que, sin importar de la manera en la que la palabra "encargado" se ingrese, siempre sea en minúscula como el valor de agente.
print() #Estos print vacíos son solo para que se vea más estético.
platillo = [] #Esta es la lista vacía, que posteriormente se llenará con los datos que se metan, de los platillos.
precios = [] #Esta es la lista vacía de los precios de los platillos de la lista de platillo.

while comproba != agente: #Este es el primer bucle. Se centra en nada más permitir o no el acceso al sistema de la "aplicación" que se verá en el siguiente bucle, acorde al valor que se ingrese.
    print("Agente no registrado") #Tal como la indicación de arriba lo indica, si el valor metido en el input de la variable comproba no es igual al valor de la variable agente, es decir, encargado, entonces imprimirá "Agente no registrado".
    print()
    comproba = input("Favor ingrese nombre del agente: ").lower() #Aquí ponemos nuevamente la variable de comproba porque ya está adentro del bucle, hasta que se escriba el valor de la variable agente, lo cual haría que el bucle termine.
    print()
    
sistema = True #Creamos esta otra variable para empezar el bucle del sistema de las opciones.

while sistema: #Aquí va a suceder todo lo que se diga en las líneas de abajo, todo y cuando (mientras) "sistema" siga siendo True.
    print("1. Creación de platillos.")
    print("2. Consulta de platillos y precios.")
    print("3. Colocar un pedido.")
    print("4. Salir.") #Puse las opciones de esta manera para que se viera más estético y ordenado.
    print()
    opcion = int(input("Elija una de las opciones: ")) #Empezamos con esta variable en el segundo bucle para que, el que ingresa los datos, pueda elegir la opción.
    print()
    
    if opcion == 1: #Empezamos con el primer if que me abre todo lo que va a suceder si la opción seleccionada por el que entra los datos es igual a 1.
        platillo.append(input("Ingrese el nombre del platillo a crear: ").capitalize()) #Ponemos el append para agregar el platillo a la lista vacía de los platillos.
        precios.append(float(input("Ingrese el precio del platillo a crear: "))) #Aquí el append cumple la misma función pero agregando a la lista vacía de "Precios", con la diferencia que le puse "float" para que permita meter decimales.
        print()
        print("El platillo y su precio han sido guardados.") #Puse esto para que a la persona le quede salvedad de que los platillos, anteriormente agregados, quedaron guardados en la lista antes vacía.
        print()
        
    elif opcion == 2: #Este elif abre la segunda opción, es decir, todo lo que va a suceder si la persona ingresa un "2" al momento de seleccionar la opción.
        for i in range(len(platillo)): #Aquí me está indicando que por cada uno de los caracteres, los cuales he denominado como "i" (desde 0 hasta el último) voy a hacer lo siguiente:
            print(f"{platillo[i]}: ${precios[i]}") #Va a imprimir el platillo "i", en el orden que se hayan ingresado anteriormente los platillos, junto con el precio.
        if opcion == 2 and len(platillo) == 0: #Este supuesto sucede si la extensión (len) de la lista platillo es igual a 0, es decir, no hay ningún platillo en este.
            print("Actualmente no hay platillos ingresados.") #Estonces se va a imprimir este mensaje si sucede lo anterior.
            print()
    
    if opcion == 3 and len(platillo) == 0: #Aquí estoy indicando qué va a suceder si no hay ningún platillo en la lista de platillos y la persona quiere la opción 3 (hacer una orden).
            print("Actualmente no hay platillos disponibles.") #En ese caso, va a imprimir este mensaje.
            print()
            
    elif opcion == 3: #Este elif abre todo lo que va a suceder si la opción seleccionada es la 3 y sí hay platillos disponibles en la lista de platillos.
        pedido = input("Indique el nombre del platillo para su orden: ").capitalize() #La variable para que pueda escribir el platillo que desea pedir.
        print()
        if pedido in platillo: #Aquí me está indicando que si el nombre ingresado en la variable platillo está en la lista de platillos, va a suceder lo siguiente:
                lugar_plato = platillo.index(pedido) #Bueno, esta es una variable que me ayuda a hacer la relación entre el precio y el platillo gracias a la función de index. Donde la variable "Lugar_plato" es igual la posición del pedido hecho en la lista de platillos.
                print(f"Usted ha elegido {pedido.lower()} con un precio de ${precios[lugar_plato]}") #Aquí lo imprime. Puse el lower a la variable pedido para que entre en el formato del texto y puse la variable anteriormente creada para poder hacer la relación del precio del platillo solicitado.
                print()
        else:
                print("El nombre del platillo ingresado no existe.") #esto es lo que sucede si se solicita un platillo que no está dentro de la lista de platillos.
                print()
                
    elif opcion == 4: #este elif es para salir del sistema, tal como lo indica la opción 4.
        print("Gracias por haber hecho uso de esta apliacion.") #Se imprimirá este mensaje si es así.
        print()
        sistema = False #Se pone esto para que cierre el bucle.
        
    
   
