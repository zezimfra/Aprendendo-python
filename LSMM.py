routes = int(input('Quantas rotas você percorreu hoje? '))
acum = 0

for count in range(0, routes):
    value = float(input('Qual foi o valor dessa rota? £'))
    acum += value

real = acum * 7.19
print('Você conseguiu £{:.2f}, que dá R${:.2f}.'.format(acum, real))

print('-='*15)

if acum >= 50:
    print('Hoje foi \033[32mprodutivo\033[m!')
else:
    print('Não foi dessa vez.')
print('-='*15)