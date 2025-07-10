import random

def poly_hash(S, p, x):
    hash_value = 0
    for c in reversed(S):
        hash_value = (hash_value * x + ord(c)) % p
    return hash_value

def pre_compute_hashes(T, pattern_len, p, x):
    n = len(T)
    H = [0] * (n - pattern_len + 1)
    S = T[n - pattern_len:]
    H[-1] = poly_hash(S, p , x)

    y = 1
    for i in range(0, pattern_len):
        y = (y * x) % p
    
    for i in reversed(range(n - pattern_len)):
        pre_hash = (x * H[i+1] + ord(T[i]) - y * ord(T[i + pattern_len])) % p
        H[i] = (pre_hash + p) % p
    
    return H

def are_equal(S1, S2):
    return S1 == S2

def rabin_karp(T, P):

    p = 10 ** 9 + 7
    x = random.randint(1, p -1)
    result = []

    p_hash = poly_hash(P, p, x)

    H = pre_compute_hashes(T, len(P), p, x)

    for i in range(0, len(T) - len(P) + 1):
        if H[i] != p_hash:
            continue

        if are_equal(T[i:i+len(P)],P):
            result.append(i)
    
    return result

if __name__ == "__main__":

    text = "abracadabra"
    pattern = "abra"
    print(rabin_karp(text, pattern))