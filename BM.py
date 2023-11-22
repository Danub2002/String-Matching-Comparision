"""
Ao inves de comparar os caracteres do texto com os do padrao pelo incio
pega pelo final

"""

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
    m = len(pattern)
    n = len(text)

    # Create the bad character heuristic table
    bad_char = bad_character_heuristic(pattern, m)

    s = 0
    while(s <= n-m):
        j = m-1

        # Decrease index j of pattern while characters of
        # pattern and text are matching at this shift s
        while j>=0 and pattern[j] == text[s+j]:
            j -= 1

        # If the pattern is present at the current shift,
        # then index j will become -1 after the above loop
        if j < 0:
            print(f"Pattern occurs at shift = {s}")
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
    return False
# Example usage
text = "ABAAABCD"
pattern = "ABC"
boyer_moore_search(text, pattern)
