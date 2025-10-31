#Ejercicio 1

menu = ["Hamburguesa" , "Hotgo" , "Pizza" , "Tacos" , "Lasaña" , "Ensalada" , "Pupusas" , "Burrito" , "Alitas de pollo" , "Papas fritas"]

elección = int(input("Ingrese el numero del plato en el menu: "))

print(f"El plato seleccionado por Alvin es: {menu[elección-1]}")