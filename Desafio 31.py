viagem = float(input('Qual é a distancia da sua viagem? '))
print ('Voce está prestes a começar uma viagem de {}Km'.format(viagem))
if viagem <=200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print ('E o preço da sua passagem será de R${:.2f}'.format(preço))
