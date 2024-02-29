'''Escreva uma função que receba uma string não vazia e a comprima de forma a substituir as 
sequencias de caracteres iguais por um contador seguido do caractere em si. Por exemplo. 
“AAA” deve ser codificado como “3A”, AABBB” como “2A3B” e assim por diante.
Para complicarmos um pouco, a string de entrada pode conter qualquer caractere, 
incluindo números e caracteres especiais. E já que as strings codificadas devem ser 
decodificáveis, nós não podemos ingenuamente codificar uma string longa simplesmente 
pelo numero de repetições. Por exemplo, “AAAAAAAAAAAA” (12 A’s) não poderia ser codificada 
como “12A”, uma vez que esta string poderia ser decodificada tanta como “AAAAAAAAAAAA” 
quanto “1AA”. Logo, repeticões de 10 ou mais caracteres, devem ser codificadas de forma 
dividida, ou seja, o exemplo acima deveria ser codificado como “9A3A”.

Exemplo de entrada 
string = “BBBBBBBBBBBBBAACCCDD”
“9B4B2A3C2D”
'''