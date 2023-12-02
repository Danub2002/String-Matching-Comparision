# Rabin-Karp Algorithm for String Matching
def rabin_karp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0

    # Define a prime number to use in hashing
    prime = 101

    # Function to calculate hash value for a given substring
    def calculate_hash(substring):
        hash_value = 0
        for char in substring:
            hash_value = (hash_value * prime + ord(char)) % (2**64)
        return hash_value

    # Calculate the hash value for the pattern and the initial substring of the text
    pattern_hash = calculate_hash(pattern)
    text_hash = calculate_hash(text[:m])

    # Rabin-Karp search
    for i in range(n - m + 1):
        if text_hash == pattern_hash and text[i:i+m] == pattern:
            # Pattern found at index i
            print(f"Pattern found at index {i}")
        comparisons += 1

        # Update the hash value for the next substring
        if i < n - m:
            text_hash = (prime * (text_hash - ord(text[i]) * (prime**(m - 1))) + ord(text[i + m])) % (2**64)

    return comparisons

text = "ABABCABABABCABABCABAB"
pattern = "ABABCABAB"
total_comparisons = rabin_karp_search(text, pattern)
print(f"Total comparisons made: {total_comparisons}")



'''
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
    number_of_comparations = []
    comparations = 0

    # Preprocessing
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over the text one by one
    for s in range(n - m + 1):
        # Check the hash values of current window of text and pattern
        # If the hash values match then only check for characters one by one
        comparations += 1
        if p == t:
            match = True
            for i in range(m):
                comparations += 1
                if pattern[i] != text[s + i]:
                    match = False
                    break
            if match:
                number_of_comparations.append(comparations)

        # Calculate hash value for next window of text: Remove leading digit,
        # add trailing digit
        if s < n - m:
            t = (d*(t - ord(text[s]) * h) + ord(text[s + m])) % q

            # We might get negative value of t, converting it to positive
            if t < 0:
                t = t + q

    return number_of_comparations
'''

