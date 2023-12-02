def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    comparisons = 0
 
    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*M
    j = 0  # index for pat[]
 
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
 
    i = 0  # index for txt[]
    while (N - i) >= (M - j):
      comparisons += 1
      if pat[j] == txt[i]:
        i += 1
        j += 1
 
      if j == M:
        #print("Found pattern at index " + str(i-j))
        j = lps[j-1]
 
      # mismatch after j matches
      elif i < N and pat[j] != txt[i]:
        # Do not match lps[0..lps[j-1]] characters,
        # they will match anyway
        if j != 0:
          j = lps[j-1]
        else:
          i += 1

    return comparisons
              


def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] = 0 # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i] == pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if len != 0:
				len = lps[len-1]

				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1


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