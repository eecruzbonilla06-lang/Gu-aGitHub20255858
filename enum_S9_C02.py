"""usuarios = ["Ana" , "Carlo" , "Luis" , "Maria" , "Lorenzo"]

for i, usuario in enumerate(usuarios,start=1): #toma un iterable y le agrega otro iterable al lado izquierdo comenzando con una secuencia de numeros (lo que significa enumerate). Todo según la cantidad de números/iteradores tenga el iterable
    print(f"{i} {usuario}")"""

#OTRO EJERCICIO
    
usuarios = ["Ana" , "Carlo" , "Luis" , "Maria" , "Lorenzo"]
edades = [20 , 19 , 21 , 22 , 18] 
frutas = ["mango" , "fresa" , "pera" , "sandia" , "piña"]
for usuario , edad , fruta in zip(usuarios , edades , frutas): #estamos agarrando dos listas distintas, las ponemos a la par y la convertimos una sola.
    print(f"El usuario {usuario}, con edad {edad}, le gusta {fruta}")