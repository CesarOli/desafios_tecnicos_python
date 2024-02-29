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