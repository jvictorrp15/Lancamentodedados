import random
import math

# solicita ao usuário quantos dados serão lançados
n = int(input('Quantos dados voce deseja lançar? '))  # número de dados a serem lançados

# cria uma lista vazia para armazenar os valores de lambda calculados
lam = []  
# cria duas listas vazias para armazenar os resultados dos lançamentos dos dados
igual1 = [] 
diferente1 = []

# enquanto ainda houver dados a serem lançados:
while(n != 0):
    
    # limpa as listas de resultados anteriores
    igual1.clear()
    diferente1.clear()
    
    # realiza o lançamento dos dados n vezes, armazenando os resultados em uma das duas listas criadas
    for i in range(n):
        lancamento = random.randint(1, 6)  # gera um número aleatório entre 1 e 6
        if lancamento == 1:
            igual1.append(lancamento)  # adiciona o resultado à lista de resultados com valor 1
        else:
            diferente1.append(lancamento)  # adiciona o resultado à lista de resultados diferentes de 1

    # exibe o número de dados que caíram com a face 1 para cima e o número de dados restantes
    print("Numero de dados com a face um para cima: ", len(igual1))
    print("Numero de dados restantes: ", len(diferente1))

    # se ainda existirem dados restantes:
    if len(diferente1) != 0:
        # calcula o valor de lambda e adiciona à lista de lambdas
        lam.append(- (math.log(n/len(diferente1))))
            
    # subtrai o número de dados que caíram com a face 1 para cima do total de dados para que sejam lançados os dados restantes
    n = n - len(igual1)

# exibe a média dos valores de lambda calculados
print(f'O lambda é igual a: {-(sum(lam) / len(lam))}')

