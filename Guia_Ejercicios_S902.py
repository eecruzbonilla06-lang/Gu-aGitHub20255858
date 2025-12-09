menu = ["Mostar productos","Agregar producto","Registrar nuevo cliente","Mostrar clientes","Registrar pedido","MOstrar pedidos del dia","Mostrar categorias disponibles","Salir"]

for i, opcion in enumerate(menu,start=1):
    print(f"{i}. {opcion}")

print()

clientes = []

cliente1 = {
    input("codigo: "): input("nombre: ")
}

cliente2 = {
    input("correo: "): input("telefono: ")
}


productos = []

producto1 = {
    input("codigo: "): input("nombre: ")
}

producto2 = {
    input("categoria: "): input("precio: ")
}


pedidos = []



