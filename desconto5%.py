item =  float(input('Qual é o valor do item que você quer?'))
d = item * 0.05
print('O valor do seu item é : R${} , o valor em cima do seu item é de 5% que corresponde á: R$ {:.2f} de desconto'.format(item,d))
t = item - d
print('Sendo assim o valor do seu item com desconto ficará: R${:.2f}'.format(t))
