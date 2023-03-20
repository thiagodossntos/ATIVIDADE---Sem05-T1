def minutos_horas(minutos):
    h = minutos // 60
    m = minutos % 60
    return h, m


min = int(input('digite os minutos que serao tranformado: '))
horas, minutos = minutos_horas(min)
print(f'seu minutos foram convertidos em {horas}h:{minutos}m')

