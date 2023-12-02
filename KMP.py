def compute_lps_array(pattern):
  m = len(pattern)
  lps = [0] * m
  length = 0
  i = 1

  while i < m:
    if pattern[i] == pattern[length]:
      length += 1
      lps[i] = length
      i += 1
    else:
      if length != 0:
        length = lps[length - 1]
      else:
        lps[i] = 0
        i += 1

    return lps

def kmp_search(text, pattern):
  n = len(text)
  m = len(pattern)
  comparisons = 0

  lps = compute_lps_array(pattern)

  i = j = 0
  while i < n:
    comparisons += 1
    if pattern[j] == text[i]:
      i += 1
      j += 1

      if j == m:
        print(f"Pattern found at index {i - j}")
        j = lps[j - 1]
      else:
        if j != 0:
          j = lps[j - 1]
        else:
          i += 1

  return comparisons

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
total_comparisons = kmp_search(text, pattern)
print(f"Total comparisons made: {total_comparisons}")



'''
def prefix_function(s):
  n = len(s)
  pi = [0]*n
  for i in range(1,n):
    j = pi[i-1] # tam do maior prefix que tambem e suffix ate agr
    while j > 0 and s[i] != s[j]:
      # Lida com o mismatch n hora de expandir o prefixo
      # Entao temos que procura outro menor para essa posicao
      j = pi[j-1]

    # precisamos verificar isso pq o while pode ter parado pq 
    # o prefix ficou com tamanho zero
    if s[j] == s[i]:
      j+=1
    
    pi[i] = j
  
  return pi
  
def kmp_matcher(text, pattern):


  n = len(text)
  m = len(pattern)
  pi = prefix_function(pattern)
  j = 0  # Matching Atual
  iterations = 0

  occurrences = []
  for i in range(n):
    iterations += 1
    while j > 0 and text[i] != pattern[j]:
      iterations += 1
      # Buca um prefixo menor que da matching
      j = pi[j - 1]

    # Incrementa o mathching
    if text[i] == pattern[j]:
      j += 1
      
    if j == m:  
      print("encontrei o padrao na posicao", i - m +1)
      occurrences.append(iterations)  # +1 for 0-based indexing
      # Update the current match length for the next potential match
      j = pi[j - 1]
    
    return occurrences
'''