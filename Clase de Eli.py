"""

nota = int(input('Ingrese la nota: '))

if nota == 10:
    print('E')
else: #ponemos else para abrir las otras posibilidades
    if nota > 7:
        print('MB')
    else: #aqui tengo que ponerle el else para que me salga una sola opcion, priorizando las primeras
        if nota > 5:
            print('B')
        else:
            if nota > 3:
                print('R')
            else: 
                print('M')
"""
"""
monto = int(input('Ingrese el monto: '))
tipo = input('Ingrese el tipo de venta: ')

if monto > 500 and tipo.lower() == 'local':
    print('10%')
else:
    if monto > 500 and tipo.lower() == 'export':
        print('14%')
    else:
        if monto > 200 and tipo.lower() == 'local':
            print('8%')
        else: 
            if monto > 200 and tipo.lower() == 'export':
                print('12%')
#eso no me sirvio para nada porque no tengo que poner el procentaje textual y me compliqué mucho
""" 
"""
#aqui viene el bueno

monto = int(input('Ingrese el monto: '))
tipo = input('Ingrese el tipo de venta: ')

if tipo.lower() == 'local':
    if monto > 500:
        impuesto = 0.1
    else:
        if monto > 200:
            impuesto = 0.08
        else:
            if monto > 50:
                impuesto = 0.06
            else:
                impuesto = 0
                
elif tipo.lower() == 'exportacion':
    if monto > 500:
        impuesto = 0.14
    elif monto > 200:
        impuesto = 0.12
    elif monto > 50:
        impuesto = 0.1
    else:
        impuesto = 0
        
else:
    print("Este tipo no es valido")
    
print(f"El impuesto a pagar de tipo {tipo} por venta de {monto:,.2f}")
print(f"es de {monto*impuesto:,.2f}")
"""

#NUEVO TEMA

#ITERABLE: Objeto capaz de devolver sus componentes uno a la vez.
#ITERADOR: Objeto que representa un flujo de datos

#vamos a crear un iterable

nombre = ['Ana' , 'Sebas' , 'Maria'] #un iterable con tres iteradores. Las cadenas son iterables

"""print(len(nombre[0])) #aqui si me va a dar la cantidad de caracteres porque el primer iterador del iterable es un texto"""

"""for nombrecito in nombre:
    print(nombrecito)"""
    
for nombrecito in nombre:
    if nombrecito == 'Sebas':
        print('Ya lo encontre')

        
nombre_buscar = input('Nombre a buscar: ')
for n in nombre:
    if n == nombre_buscar:
        print('Ya lo encontre')
    else: 
        print('Aqui no esta')
    
nombre2 = [1 , 2 , 3]

"""print(len(nombre[0])) #esto no se puede porque el iterador 0 del iterable no tiene caracteres, no es un texto"""

for numerito in nombre2: #aqui me puedo inventar el nombre de los iteradores, no del iterable
    #for significa: para cada
    print(numerito) #es como entrar a cada cuartito y gritar el nombre del numero que encuentra en cada cuartito
    

