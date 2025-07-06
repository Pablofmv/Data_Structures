
def are_equal(s1, s2):

    if len(s1) != len(s2):
        return False
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    
    return True


def find_substring_naive(T, P):

    positions = []
    n = len(T)
    m = len(P)

    for i in range(0, n - m + 1):
        if are_equal(T[i:i+m], P):
            positions.append(i)
    
    return positions

if __name__ == "__main__":

    T = "abcxabcdabxabcd"
    P = "abcd"
    print(find_substring_naive(T, P))