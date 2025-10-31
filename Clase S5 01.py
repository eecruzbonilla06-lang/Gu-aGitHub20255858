nombre = "Alvin"
print(nombre[2:5:2]) #INICIO:FIN:SALTO se cuenta desde cero y se suma uno más porque el último no s incluye

palabra = "RECONOCER"
print(palabra[:4:1]) #si aquí no pongo nada en el inicio, se asume que es desde cero y si no pongo nada en salto, se asume que es de uno

palabra1_1 = "RECONOCER"
print(palabra1_1[1:9:2]) #si queremos solo las vocales

palabra1_2 = "RECONOCER"
print(palabra1_2[:9:2]) #si queremos solo las consonantes 

palabra2 = "ratón" 
print(palabra2[::-1]) #esto hará que la palabra se escriba totalmente al revés porque los saltos son negativos, es decir, empieza del final

####################

prueba = "bob"
print(prueba==prueba[::-1]) #si no se pone nada en fin, por defecto se sabe que es la última

numero = 1234

print(len(prueba)) # esto para saber el número de letras

#edad = input() #esto es para ingresar números, me permite meter valores en mi código
#print(len(edad))

print(palabra.lower())
print(palabra2.upper()) #lleva paréntesis porque los métodos son funcionas aderidas a un objeto
print(palabra2.capitalize()) #las funciones llevan el nombre de la función y el apartado donde yo puedo poner argumentos o parámetros
#print(numero.up)

#tupla es una secuencia de objetos de python
#tupla1 = (17,18,19,18,17,19,18) #tupla lleva paréntesis
#print(tupla1[4])

lista1 = [17,18,19,17,19]  #lista se crea con paréntesis cuadrados
lista1[4] = 18
print(lista1)
print(len(lista1))