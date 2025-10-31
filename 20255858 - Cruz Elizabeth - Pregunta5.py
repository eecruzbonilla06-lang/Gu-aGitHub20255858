palabra = input()
letra = input()

letra_minu = letra.lower()

conte = palabra.count(letra_minu) >= 1

print(conte)