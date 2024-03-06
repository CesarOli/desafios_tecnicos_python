'''Escreva uma função que recebe um array não vazio de inteiros distintos e um inteiro representando 
uma soma alvo. Se quaisquer dois números no array de entrada somam a soma a soma alvo, a função
deve retorná-los no array de saíd, em qualquer ordem. Se nenhum par de números no array de entrada
somarem a soma alvo, a função deve retornar um array vazio.

Note que a soma alvo deve ser obtida somando dois inteiros diferentes do array, cove pode soma 
um inteiro com ele mesmo. Voce pode assumir que existirá no máximo um par de números somando
a soma alvo.

Exemplos de entrada
array = [3, 5, -4, 8, 11, -1, 6]
targetSum = 10

Exemplo de saída
[-1, 11] // pode ser ordem invertida
'''

import random

def procura_por_par_soma_alvo(lista, soma_alvo):
    rastreia_numeros = set()

    for numero in lista:
        diferenca_alvo = soma_alvo - numero

        if diferenca_alvo in rastreia_numeros:
            return [numero, diferenca_alvo]
        else:
            rastreia_numeros.add(numero)

    return []

# Exemplo de uso com array e soma alvo gerados aleatoriamente:
tamanho_lista = 7  # Defina o tamanho desejado para o array
lista_de_exemplo = [random.randint(-50, 50) for _ in range(tamanho_lista)]  # Gera números aleatórios entre -50 e 50
soma_alvo_de_exemplo = random.randint(-100, 100)  # Gera uma soma alvo aleatória entre -100 e 100

resultado = procura_por_par_soma_alvo(lista_de_exemplo, soma_alvo_de_exemplo)
print(f"Array de exemplo: {lista_de_exemplo}")
print(f"Soma alvo de exemplo: {soma_alvo_de_exemplo}")
print(f"Resultado: {resultado}")
