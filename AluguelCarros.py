d = int(input('Por quantos dias você alugou o carro ?'))
km = float(input('Por quantos KM voce percorreu ? '))
da = (60 * d)
kma = (km * 0.15)
t = (da + kma)
print('Voce alugou por :{}dias , rodou : {}km então você pagará no total : R${}'.format(d,km,t))


