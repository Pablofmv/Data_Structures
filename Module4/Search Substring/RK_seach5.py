import random


def poly_hash(S, x, p):

    hash_value = 0
    for c in reversed(S):
        hash_value = (hash_value * x + ord(c)) % p
    
    return hash_value

def are_equal(S1, S2):

    if len(S1) != len(S2):
        return False
    
    for i in range(0, len(S1)):
        if S1[i] != S2[i]:
            return False
    
    return True


def rabin_karp_search(T, P):

    p = 10 ** 9 + 7
    x = random.randint(1, p -1)
    positions = []

    p_hash = poly_hash(P, x, p)

    for i in range(0, len(T) - len(P) + 1):
        window = T[i:i + len(P)]
        window_hash = poly_hash(window, x, p)

        if window_hash != p_hash:
            continue

        if are_equal(P, window):
            positions.append(i)

    return positions

if __name__ == "__main__":

    T = "abracadabra"
    P = "abra"

    print("Matches found at positions:", rabin_karp_search(T, P))
