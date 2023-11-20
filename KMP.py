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


  for i in range(n):
    while j > 0 and text[i] != pattern[j]:
      # Buca um prefixo menor que da matching
      j = pi[j - 1]

    # Incrementa o mathching
    if text[i] == pattern[j]:
      j += 1
      
    if j == m:  
      print("encontrei o padrao na posicao", i - m +1)
      return True
      

  return False



text = "ABCABABABACA"
pattern = "ABABACA"
print(kmp_matcher(text, pattern))