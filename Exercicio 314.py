# Proprama para calcular o aluguel de um carro

km = int(input('Quantos quilometros o carro rodou? '))
dias = int(input('Por quantos dias você ficou com o carro? '))
preco_dias = dias * 60
print(preco_dias)
preco_km = km * 1
print(preco_km)
preco_final = preco_dias + preco_km
print('O preço a ser pago por {} dias, {} km rodados é {} Reais'.format(dias, km, preco_final))