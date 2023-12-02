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

def boyer_moore_horspool_search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0

    # Preprocess bad character heuristic
    bad_char = {pattern[i]: max(1, m - i - 1) for i in range(m - 1)}

    # Boyer-Moore-Horspool search
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
            comparisons += 1

        if j < 0:
            # Pattern found at index i
            print(f"Pattern found at index {i}")
            i += 1
        else:
            char_shift = bad_char.get(text[i + j], m)
            i += char_shift
            comparisons += 1

    return comparisons

text = "ABABCABABABCABABCABAB"
pattern = "ABABCABAB"
total_comparisons = boyer_moore_horspool_search(text, pattern)
print(f"Total comparisons made: {total_comparisons}")





'''
from collections import defaultdict

def search(text, pattern):
    iterations = 0

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
        iterations += 1
        j = M - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            iterations += 1
            j -= 1
            i -= 1
        if j == -1:
            Indices.append(iterations)

        k += Skip[ord(text[k])]
    
    return Indices
'''