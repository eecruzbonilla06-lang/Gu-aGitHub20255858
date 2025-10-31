#EJERCICIO 1

# Pide al usuario que ingrese un correo electrónico y lo guarda en la variable `correo`.
correo = input("")

# Busca la posición (índice) del carácter '@' dentro de la cadena `correo`.
correoat = correo.index('@')

# Evalúa varias condiciones sobre el correo y muestra True o False según si todas se cumplen:
print(
    # Comprueba que haya exactamente un '@' en todo el texto.
    correo.count('@') == 1 and

    # Comprueba que haya al menos 3 caracteres antes del '@' (índice >= 3 significa posiciones 0,1,2 existen).
    correoat >= 3 and

    # Comprueba que haya al menos 3 caracteres después del '@'.
    # len(correo) - correoat - 1 es el número de caracteres a la derecha de '@'.
    len(correo) - correoat - 1 >= 3 and

    # Comprueba que haya al menos un punto '.' en alguna parte del correo.
    correo.count('.') >= 1 and

    # Comprueba que no haya espacios en el correo.
    correo.count(' ') == 0 and

    # Comprueba que el primer carácter no sea un punto.
    correo[0] != '.' and

    # Comprueba que el último carácter no sea un punto.
    correo[-1] != '.'
)

#EJERCICIO 2

# Pide al usuario que escriba una cadena de texto y la guarda en la variable `cadena`.
cadena = input("")

# Cuenta cuántas veces aparece la letra "z" dentro de la cadena
# y muestra ese número en pantalla.
print(cadena.count("z"))

# EJERCICIO 3

# Pide al usuario un número entero y lo guarda en la variable X.
X = int(input(""))

# Pide al usuario una cadena de texto y la guarda en la variable A.
A = input("")

# Pide al usuario otra cadena de texto y la guarda en la variable B.
B = input("")

# Imprime una nueva cadena formada por:
# 1️⃣ Los primeros (len(A)//X) caracteres de A. ACA OCUPAMOS // PARA DIVIDIR EN CASO CUANDO PROBAMOS CON / NOS DA ERROR
#     - len(A)//X usa división entera (sin decimales), por lo que toma una cantidad proporcional a A.
# 2️⃣ Los últimos (len(B)//X) caracteres de B.
#     - B[-(len(B)//X):] significa “desde esa posición hasta el final”.
# Luego concatena ambas partes.
print(A[0:(len(A)//X)] + B[-(len(B)//X):])

# EJERCICIO 4

# Pide al usuario un número entero y lo guarda en la variable A.
A = int(input(""))

# Pide otro número entero y lo guarda en la variable B.
B = int(input(""))

# Pide otro número entero y lo guarda en la variable C.
C = int(input(""))

# Pide otro número entero y lo guarda en la variable D.
D = int(input(""))

# Calcula el producto de A y B, y el producto de C y D.
# Luego resta el segundo producto al primero y muestra el resultado.
print((A * B) - (C * D))


# EJERCICIO 5

# Pide al usuario que ingrese 6 números decimales (notas) y los guarda en variables separadas.
n1 = float(input(""))
n2 = float(input(""))
n3 = float(input(""))
n4 = float(input(""))
n5 = float(input(""))
n6 = float(input(""))

# Crea una lista llamada 'notas' que contiene los 6 valores ingresados.
notas = [n1, n2, n3, n4, n5, n6]

# Muestra la nota máxima usando la función max(), con 2 decimales.
print(f"Maximo: {max(notas):.2f}")

# Muestra la nota mínima usando la función min(), con 2 decimales.
print(f"Minimo: {min(notas):.2f}")

# Calcula y muestra la diferencia entre la nota máxima y la mínima, con 2 decimales.
print(f"Diferencia: {(max(notas) - min(notas)):.2f}")

# Calcula y muestra la suma total de todas las notas, con 2 decimales.
print(f"Suma: {sum(notas):.2f}")

# Calcula y muestra el promedio de las notas (suma dividido entre la cantidad), con 2 decimales.
print(f"Promedio: {(sum(notas) / len(notas)):.2f}")

# EJERCICIO 6

# Pide al usuario que ingrese 5 números enteros.
# Cada número representa la cantidad de puntos que vale cada problema.
p1 = int(input(""))
p2 = int(input(""))
p3 = int(input(""))
p4 = int(input(""))
p5 = int(input(""))

# Pide al usuario que ingrese 5 números decimales.
# Cada número representa el porcentaje (en forma decimal) obtenido por el equipo en cada problema.
n1 = float(input(""))
n2 = float(input(""))
n3 = float(input(""))
n4 = float(input(""))
n5 = float(input(""))

# Calcula la puntuación total multiplicando los puntos del problema
# por el porcentaje obtenido en ese problema, y luego sumando todos los resultados.
# Ejemplo: si p1=100 y n1=0.8 → aporta 80 puntos.
total = (p1 * n1) + (p2 * n2) + (p3 * n3) + (p4 * n4) + (p5 * n5)

# Convierte el resultado total a un número entero y lo muestra en pantalla.
# Se usa int() para descartar los decimales y dejar solo la parte entera.
print(int(total))

# EJERCICIO 7

# Pide al usuario que ingrese el nombre del competidor
nombre = input("")

# Pide al usuario que ingrese el apellido del competidor
apellido = input("")

# Construye el Nick:
# - Toma los primeros 5 caracteres del nombre (nombre[:5])
# - Agrega la primera letra del apellido (apellido[0])
# - Convierte todo a minúsculas (.lower())
nick = (nombre[:5] + apellido[0]).lower()

# Calcula el Pin:
# - Multiplica la longitud del nombre por 1000
# - Suma la longitud del apellido
# - Aplica módulo 10000 para mantenerlo en 4 dígitos
pin = (len(nombre) * 1000 + len(apellido)) % 10000

# Construye el ID completo en el formato "C3-<nick>-<pin>"
id_completo = (f"C3-{nick}-{pin}")

# Muestra el Nick en la primera línea
print(f"Nick: {nick}")

# Muestra el Pin en la segunda línea
print(f"Pin: {pin}")

# Muestra el ID completo en la tercera línea
print(f"ID: {id_completo}")

# EJERCICIO 8

# Pide al usuario que ingrese una fecha en formato DD/MM/AAAA
fecha = input()

# Imprime la fecha en formato AAAA/MM/DD
# - fecha[6:] toma los caracteres desde la posición 6 hasta el final (el año)
# - fecha[3:5] toma los caracteres en las posiciones 3 y 4 (el mes)
# - fecha[0:2] toma los caracteres en las posiciones 0 y 1 (el día)
# Luego concatena con "/" entre cada parte.
print(fecha[6:] + "/" + fecha[3:5] + "/" + fecha[0:2])


# EJERCICIO 9

# Definir el menú de platos principales y complementos como tuplas
platos_principales = ("Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog")
complementos = ("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña")

# Leer el número del plato principal (entero)
# Se resta 1 porque los índices de las tuplas empiezan en 0
num_plato = int(input("")) - 1

# Leer el número del complemento (entero)
num_complemento = int(input("")) - 1

# Obtener los nombres del plato y del complemento seleccionados
plato = platos_principales[num_plato]
complemento = complementos[num_complemento]

# Mostrar el pedido completo con el formato indicado
print(f"El pedido de Alvin es: {plato} con {complemento}")

# EJERCICIO 10

# Leer el número entero N
N = int(input(""))

# Calcular la suma usando la fórmula: N * (N + 1) // 2
# Se usa // para obtener un resultado entero
suma = N * (N + 1) // 2

# Mostrar el resultado
print(suma)