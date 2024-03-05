'''É o dia da foto da turma em uma escola local e você foi o fotógrado escolhido para tirá-la. 
A classe que você irá fotografar tem um número par de alunos e todos estes alunos estão 
usando uniformes pretos ou laranjas em iguais quantidades, ou seja, metade da turma está 
com uniformes pretos e metade com uniformes laranjas. Vocé é responsável por arranjar os 
alunos em duas filas para a fotografia, uma na frente na outra. Cada fila deve conter o 
mesmo numero de alunos e deve preencher os seguintes requisitos: 

Todos os alunos usando uniforme preto devem estar na mesma fila 
Todos os alunos usando uniforme laranja devem estar na mesma fila
Todos os alunos na fila de trás devem ser estritamente mais altos que o aluno diretamente
em sua frente na fila da frente

Você recebe dois arrays de entrada: um contendo a altura dos alunos com uniformes pretos 
e outro contendo a altura dos alunos com uniformes laranjas. Esses arrays sempre terão o 
mesmo tamanho e cada altura (em cm) será um inteiro positivo.

Escreva uma função que retorne True ou False caso seja possível ou não tirar a fotografia
de uma determinada turma seguindo os parâmetros estabelecidos. 
Você pode assumir que cada turma tem ao menos dois alunos.

Exemplo de entrada:

uniformes_pretos = [150, 179, 149, 152, 154]
uniformes_laranjas = [162, 181, 151, 160, 170]


Exemplo de saída:
true
'''


import random

def gerar_alturas_aleatorias(tamanho_turma, altura_min, altura_max):
    alturas = []
    for _ in range(tamanho_turma):
        alturas.append(random.randint(altura_min, altura_max))
    return alturas

def verificar_cor_uniformes_na_fotografia(alunos_uniformes_pretos, alunos_uniformes_laranjas):
    # Verificar se os arrays de altura têm o mesmo tamanho
    if len(alunos_uniformes_pretos) != len(alunos_uniformes_laranjas):
        print("Os arrays de altura devem ter o mesmo tamanho.")
        return False

    # Ordenar as alturas em ordem crescente para cada turma
    alunos_uniformes_pretos.sort()
    alunos_uniformes_laranjas.sort()

    for i in range(len(alunos_uniformes_pretos)):
        altura_preto = alunos_uniformes_pretos[i]
        altura_laranja = alunos_uniformes_laranjas[i]

        if altura_preto >= altura_laranja:
            return False

    # Se a condição for atendida para todos os pares, retorna True
    return True

# Definindo o tamanho das turmas e os intervalos de altura
tamanho_turma_pretos = 5
tamanho_turma_laranjas = 5
altura_min_pretos, altura_max_pretos = 138, 188
altura_min_laranjas, altura_max_laranjas = 137, 185

# Gerando alturas aleatórias para cada turma
alunos_uniformes_pretos = gerar_alturas_aleatorias(tamanho_turma_pretos, altura_min_pretos, altura_max_pretos)
alunos_uniformes_laranjas = gerar_alturas_aleatorias(tamanho_turma_laranjas, altura_min_laranjas, altura_max_laranjas)

# Chamada da função e impressão do resultado
resultado = verificar_cor_uniformes_na_fotografia(alunos_uniformes_pretos, alunos_uniformes_laranjas)

# Imprimindo os resultados
print("Alturas dos alunos com uniformes pretos:", alunos_uniformes_pretos)
print("Alturas dos alunos com uniformes laranjas:", alunos_uniformes_laranjas)
print("Resultado da fotografia:", resultado)
