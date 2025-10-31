#Ejercicio 2

precios = ["1. Hamburguesa: $3.52" , "2. Hotgo: $55.15" , "3. Pizza: $4.25" , "4. Tacos: 60.25" , "5. Lasaña: $5.65 " , "6. Ensalada: $3.25" , "7. Pupusas: $2.65" , "8. Burrito: $70.75" , "9. Alitas de pollo: $6.25" , "10. Papas fritas: $2.55"]
print(precios)

plato_a_corregir = int(input("Ingrese el numero de plato al que quieres cambiar el precio: "))
plato_a_corregir = plato_a_corregir-1

nuevo_precio = float(input("Ingrese el precio actualizado: "))

precios[plato_a_corregir] = nuevo_precio

print(f"Los precios actualizados son: {precios} ")