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

def comprimir_string_tradicional(frase):
    if not frase:
        return "A frase de entrada não pode ser vazia."

    resultado_comprimido = ""
    contagem_caracteres = 1

    for i in range(1, len(frase)):
        caractere_atual = frase[i]
        caractere_anterior = frase[i - 1]

        if caractere_atual == caractere_anterior:
            contagem_caracteres += 1
        else:
            if contagem_caracteres > 1:
                resultado_comprimido += str(contagem_caracteres) + caractere_anterior
            else:
                resultado_comprimido += caractere_anterior

            contagem_caracteres = 1

    # Lidar com o último conjunto de caracteres
    if contagem_caracteres > 1:
        resultado_comprimido += str(contagem_caracteres) + frase[-1]
    else:
        resultado_comprimido += frase[-1]

    return resultado_comprimido

# Solicitar entrada do usuário
frase_usuario = input("Digite a frase que deseja codificar: ")
resultado_codificado = comprimir_string_tradicional(frase_usuario)
print(f"Resultado codificado: {resultado_codificado}")
