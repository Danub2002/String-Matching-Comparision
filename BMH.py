'''
É um algorirmo para achar substrings dentro de strings. 
Esse algoritmo compara cada caracter de uma substring para achar
uma palavra ou o mesmo caractere dentro da string.

Quando os caracteres não batem, a busca 'pula' para a próxima posição
que dá match no padrão, a partir de um valor em uma tabela.
'''

'''
Por exemplo, queremos achar 'abcd' na string 'eovadabcdftoy'.

O primeiro passo é calcular o valor de cada letra da substring para
criar a tablea de 'Bad Match', usando a fórmula:

valor = tamanho_substring - index_cada_letra - 1

Note que, o valor da última letra e de outras letras que não estão
na substring serçao o tamanho da substring.

Finalmente, o valor deve ser definido para cada letra, no 
'Bad match Table'.

Com a tabela, você pode comparar a substring com as strings.
Começamos do índice da última letra, nesse caso a letra 'd'.

Se a letra bater, comparamos com a letra anterior com 'c', se não
checamos o valor na 'Bad Match Table', e pulamos o número de
espaço do valor da tabela.
'''

from collections import defaultdict

def search(text, pattern):
    M = len(pattern)
    N = len(text)

    if M > N:
        return -1
    
    #Se tentarmos recuperar uma key que não está no texto
    #É retornado M, tamanho do texto
    Skip = defaultdict(lambda: M)

    Indices = []

    for k in range(M-1):
        Skip[ord(pattern[k])] = M - k - 1

    k = M - 1

    while k < N:
        j = M - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            Indices.append(i+1)

        k += Skip[ord(text[k])]
    
    return Indices

if __name__ == '__main__':
    print(search("eovadabcdftoyabcd", "abcd"))