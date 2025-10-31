# .lower() y .upper()
nombre = "Walter"
apellido = "Gonzalez"
print("Nombre original:", nombre)
print("Apellido original:", apellido)

# .lower() → convierte todo a minúsculas
nick = (nombre[:5] + apellido[0]).lower()
print("Nick en minúsculas:", nick)

# .upper() → convierte todo a mayúsculas
print("Apellido en mayúsculas:", apellido.upper())
print()

# 2️⃣ len() → longitud de strings o listas
print("Longitud del nombre:", len(nombre))
print("Longitud del apellido:", len(apellido))
notas = [5, 7, 9, 6, 8, 10]
print("Cantidad de notas:", len(notas))
print()

# 3️⃣ count() → contar ocurrencias
texto = "pizza"
print("Número de letras 'z' en 'pizza':", texto.count("z"))

# Para correos: contar '@'
correo = "usuario@correo.com"
print("Cantidad de '@' en correo:", correo.count("@"))
print()

# 4️⃣ index() → obtener posición de un carácter en un string
correoat = correo.index("@")
print("Índice de '@' en correo:", correoat)
print()

# 5️⃣ max() y min() → máximo y mínimo de listas
print("Lista de notas:", notas)
print("Máxima nota:", max(notas))
print("Mínima nota:", min(notas))
print("Diferencia:", max(notas)-min(notas))
print("Suma de todas las notas:", sum(notas))
print("Promedio:", sum(notas)/len(notas))
print()

# 6️⃣ Slicing ([:], [-:], etc.)
fecha = "17/10/2025"
print("Fecha original:", fecha)
print("Año:", fecha[6:])
print("Mes:", fecha[3:5])
print("Día:", fecha[:2])

cadena = "Python"
print("Primeras 3 letras:", cadena[:3])
print("Últimas 2 letras:", cadena[-2:])
print("Letras del 2 al 4:", cadena[1:4])
print()

# 7️⃣ Operaciones aritméticas y f-strings
A, B, C, D = 5, 6, 3, 2
resultado = (A*B) - (C*D)
print(f"(A*B)-(C*D) = ({A}*{B}) - ({C}*{D}) = {resultado}")

# Fórmula suma de 1 a N sin bucles
N = 10
suma = N*(N+1)//2
print(f"Suma de enteros de 1 a {N}: {suma}")
print()

# 8️⃣ Tuplas y acceso a elementos
# ACA RECUERDEN SE LE RESTA UNO A LA ELECCION DEL USUARIO PORQUE COMENZAMOS A CONTAR EN 0
platos_principales = ("Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog")
complementos = ("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña")
print("Primer plato:", platos_principales[0])
print("Último complemento:", complementos[-1])
print()

# 9️⃣ Concatenación y f-strings
plato = platos_principales[1]
complemento = complementos[2]
pedido = f"El pedido de Alvin es: {plato} con {complemento}"
print(pedido)
