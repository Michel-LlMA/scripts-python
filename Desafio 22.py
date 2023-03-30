nome = str(input('Qual é seu nome completo? ')).strip()
print ('Seu nome com todas letras maiúsculas é: {}'.format(nome.upper()))
print ('Seu nome com todas letras minúsculas é: {}'.format(nome.lower()))
print ('Seu nome completo tem um total de {} letras'.format(len(nome.replace(' ', ''))))
pnome = nome.split()[0]
print ('Seu primeiro nome tem {} letras.'.format(len(pnome)))
#print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))