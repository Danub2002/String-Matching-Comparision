"""
Ao inves de comparar os caracteres do texto com os do padrao pelo incio
pega pelo final

"""

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0

    # Preprocess bad character heuristic
    bad_char = {pattern[i]: max(1, m - i - 1) for i in range(m - 1)}

    # Preprocess good suffix heuristic
    suffix = [0] * m
    prefix = [False] * m
    last_prefix_index = m

    for i in range(m - 2, -1, -1):
        if i > last_prefix_index and suffix[i + m - 1 - last_prefix_index] < i - last_prefix_index:
            suffix[i] = suffix[i + m - 1 - last_prefix_index]
        else:
            last_prefix_index = i
            j = i
            while j >= 0 and pattern[j] == pattern[j + m - 1 - i]:
                j -= 1
            suffix[i] = i - j

    for i in range(m - 1, -1, -1):
        if i == m - 1 or suffix[i] == i + 1:
            for j in range(m - 1 - i, -1, -1):
                if not prefix[j]:
                    prefix[j] = i + 1
                comparisons += 1

    # Boyer-Moore search
    i = j = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
            comparisons += 1

        if j < 0:
            print(f"Pattern found at index {i}")
            i += suffix[0]
        else:
            char_shift = bad_char.get(text[i + j], m)
            suffix_shift = suffix[j] if j < m - 1 else 1
            i += max(char_shift, suffix_shift)
            comparisons += 1

    return comparisons

text = "ABABCABABABCABABCABAB"
pattern = "ABABCABAB"
total_comparisons = boyer_moore_search(text, pattern)
print(f"Total comparisons made: {total_comparisons}")





'''
def bad_character_heuristic(string, size):
    """
    Generates the bad character heuristic table.
    """
    bad_char = [-1]*256

    for i in range(size):
        bad_char[ord(string[i])] = i

    return bad_char

def boyer_moore_search(text, pattern):
    """
    Boyer Moore search algorithm implementation.
    """
    iterations = 0
    m = len(pattern)
    n = len(text)

    result = []

    # Create the bad character heuristic table
    bad_char = bad_character_heuristic(pattern, m)

    s = 0
    while(s <= n-m):
        iterations += 1
        j = m-1

        # Decrease index j of pattern while characters of
        # pattern and text are matching at this shift s
        while j>=0 and pattern[j] == text[s+j]:
            iterations += 1
            j -= 1

        # If the pattern is present at the current shift,
        # then index j will become -1 after the above loop
        if j < 0:
            print(f"Pattern occurs at shift = {s}")
            result.append(iterations)
            # Shift the pattern so that the next character in text
            # aligns with the last occurrence of it in pattern.
            # The condition s+m < n is necessary for the case when
            # pattern occurs at the end of text
            s += (m-bad_char[ord(text[s+m])] if s+m<n else 1)
            
        else:
            # Shift the pattern so that the bad character in text
            # aligns with the last occurrence of it in pattern. The
            # max function is used to make sure that we get a positive
            # shift. We may get a negative shift if the last occurrence
            # of bad character in pattern is on the right side of the
            # current character.
            s += max(1, j-bad_char[ord(text[s+j])])
    return result
'''