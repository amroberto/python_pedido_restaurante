# O cliente pode optar por escolher 1 prato e uma bebida
# Mostre a escolha do cliente
# Utilize o while

print('====== RESTAURANTE 2 ======')

n = 1
pratos_escolhidos = []
bebidas_escolhidas = []

pratos = ['Bife', 'Frango', 'Peixe']
bebidas =  ['Refrigerante', 'Suco', 'Agua']

pessoas = int(input('Quantidade de pessoas no pedido>> '))

while n <= pessoas:
        
    for i in pratos:
        print(i)
    prato = input(f'Escolha o prato da pessoa {n}>>')
    pratos_escolhidos.append(prato)

    for i in bebidas:
        print(i) 
    bebida = input(f'escolha sua bebida da pessoa {n}>>')
    bebidas_escolhidas.append(bebida)
    n +=1

print('-----Detalhes do pedido-------')
print('Pratos', pratos_escolhidos)
print('Bebidas', bebidas_escolhidas)


