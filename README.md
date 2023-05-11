# Lançamento de dados
Este código em Python é um programa que simula o lançamento de dados e calcula o valor de um parâmetro lambda a partir do número de lançamentos com a face 1 para cima. Vamos comentar as linhas do código para entender melhor o que ele faz:

```python
import random
import math
```
O código começa importando as bibliotecas "random" e "math", que serão usadas para gerar números aleatórios e realizar cálculos matemáticos, respectivamente.

```python
n = int(input('Quantos dados voce deseja lançar? '))
```
Aqui, o programa solicita que o usuário digite o número de dados que deseja lançar.

```python
lam = []
igual1 = []
diferente1 = []
```
Cria três listas vazias chamadas "lam", "igual1" e "diferente1". "lam" é a lista que armazenará os valores de lambda calculados no programa. "igual1" e "diferente1" são as listas que armazenarão os números de dados com a face 1 para cima e os números de dados com as outras faces para cima, respectivamente.

```python
while(n != 0):
    igual1.clear()
    diferente1.clear()
```
Este é um loop while que executa o código dentro dele enquanto o valor de "n" for diferente de zero. A cada iteração, as listas "igual1" e "diferente1" são limpas.

```python
for i in range(n):
    lancamento = random.randint(1, 6)
    if lancamento == 1:
        igual1.append(lancamento)
    else:
        diferente1.append(lancamento)
```
Este é um loop for que itera "n" vezes e em cada iteração gera um número aleatório entre 1 e 6, simulando um lançamento de dados. Se o número gerado for 1, o resultado é adicionado à lista "igual1". Caso contrário, é adicionado à lista "diferente1".

```python
print("Numero de dados com a face um para cima: ", len(igual1))
print("Numero de dados restantes: ", len(diferente1))
```
Imprime na tela o número de dados com a face 1 para cima e o número de dados restantes.

```python
if len(diferente1) != 0:
    lam.append(- (math.log(n/len(diferente1))))
n = n - len(igual1)
```
Se a lista "diferente1" não estiver vazia, o programa calcula o valor de lambda e adiciona à lista "lam". Em seguida, subtrai o número de elementos da lista "igual1" do valor de "n".

```python
print(f'O lambda é igual a: {sum(lam) / len(lam)}')
```
Finalmente, o programa calcula a média dos valores de lambda armazenados na lista "lam" e imprime na tela.
