from random import randint
n = int(input('Informe um número de 0 a 5: '))
numero = randint(0, 5)
if n == numero:
    print('Voce acertou o numero aleatorio.')
else: 
    print('Voce errou pois o numero sorteado foi {} e voce digitou {}.'.format(numero, n))
