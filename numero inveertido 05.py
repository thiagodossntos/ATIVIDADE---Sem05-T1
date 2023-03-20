def invertido(numero):
    resultado = str(numero) [::-1]
    return int(resultado)

# corpo do programa!
numero = input('digite aqui qualquer numero que sera invertido: ')
resultado = invertido(numero)

print(f'o reultado foi {resultado}')