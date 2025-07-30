alt = float(input('Qual a altura da parede? '))
larg = float(input('Qual a largura da parede? '))
a = alt * larg
print('As dimensões da sua parede é {} x {} área total da sua parede é : {:.2f}m²'.format(alt,larg,a))
tinta = a / 2
print('A quantidade de tinta que você vai precisar é: {:.2F}L'.format(tinta))


