# Rabin-Karp Algorithm for String Matching

def rabin_karp_search(text, pattern, d, q):
    """
    Rabin-Karp Algorithm for String Matching.
    :param text: the text to search within
    :param pattern: the pattern to search for
    :param d: the number of characters in the input alphabet
    :param q: a prime number
    :return: index positions where pattern is found in text
    """
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q
    p = 0
    t = 0
    result = []

    # Preprocessing
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over the text one by one
    for s in range(n - m + 1):
        # Check the hash values of current window of text and pattern
        # If the hash values match then only check for characters one by one
        if p == t:
            match = True
            for i in range(m):
                if pattern[i] != text[s + i]:
                    match = False
                    break
            if match:
                result.append(s)

        # Calculate hash value for next window of text: Remove leading digit,
        # add trailing digit
        if s < n - m:
            t = (d*(t - ord(text[s]) * h) + ord(text[s + m])) % q

            # We might get negative value of t, converting it to positive
            if t < 0:
                t = t + q

    return result

# Example usage
text = "GEEKS FOR GEEKS"
pattern = "GEEK"
# A prime number
q = 101
# Number of characters in the input alphabet
d = 256

# Search for occurrences
positions = rabin_karp_search(text, pattern, d, q)
print("Pattern found at positions:", positions)



