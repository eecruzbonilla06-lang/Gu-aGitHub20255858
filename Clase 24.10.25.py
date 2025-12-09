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