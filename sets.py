#Vamos a crear nuestro primer ser (esto es un docstring)

"""my_lista = ["rojo" , "verde" , "negro" , "azul" , "rojo" , "azul"] #esta es una lista normal
print(type(my_lista))
print(len(my_lista))
print(my_lista)


my_set2 = {"rojo" , "verde" , "negro" , "azul" , "rojo" , "azul"} #el uso principal es para generar una lista de valores no repetidos

print(type(my_set2))
print(len(my_set2))
print(my_set2) #no se sabe de qué depende el orden"""

#Vamos a crear un diccionario

"""mi_mascota = {
    "tipo": "perro" ,
    "nombre": "Phoenix" , 
    "edad":  4 , 
    "personalidad": "cariñoso"} #en el caso de los diccionarios, me importan los valores, no el orden. A cada una de las variables le ponemos a qué corresponde.
#{tipo, nombre, edad, personalidad}

#nomenclatura_diccionario : clave son índices. Las claves sí pueden tener número, pero tienen que tener sentido para representar algo en particular.
#ITEM = Clave : valor 

rivera_mascota = {
    "edad":  4 , 
    "tipo": "perro" , 
    "personalidad": "cariñoso" , 
    "nombre": "Phoenix" }

mascotas = mi_mascota == rivera_mascota #esto me indica que no importa el orden, sino los valores

    
print(type(mi_mascota))
print(mascotas)"""

#Diccionario 2

birthdays = {
    "Alice": "abril 1",
    "Bob": "diciembre 2",
    "Carol": "marzo 4"
}

birthdays["Carol"] = "septiembre 2" #aquí cambio/modifico el diccionario
print(birthdays["Carol"]) #aquí estoy imprimiendo solo el valor de Carol
birthdays["Pau"] = "julio 31" #aquí añado al diccionario
print(birthdays) #lista actualizada
del birthdays["Bob"] #aquí quito el valor de Bob
print(birthdays)

for f in birthdays.keys(): #la clave
    print(f)

for y in birthdays.values(): #el valor de la clave
    print(y)
    
for person, date in birthdays.items(): #la pareja
    print(f"El cumpleaños de {person} es el dia {date}.")