dias = int(input('Por quantos dias voce utilizou o veiculo? ')) 
km = float(input('Quantos Km rodou? '))
pago = (dias * 60) + (km * 0.15)
print ('Voce utilizou o veiculo por {:.0f} dias e rodou {}km. \nO valor a pagar ficou {:.2f}'.format (dias, km, pago))