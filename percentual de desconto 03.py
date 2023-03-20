def percentual(preco, porcentagem):
    return preco * (porcentagem / 100)


preco = float(input('digite seu preço: '))
porcentagem = float(input('agora o seu desconto: '))

aumento = preco + percentual(preco, porcentagem)
desconto = preco - percentual(preco, porcentagem)

print(f'o aumento no preço foi de {aumento :.2f}')
print(f'o deconto no preçp foi de {desconto :.2f} ')
