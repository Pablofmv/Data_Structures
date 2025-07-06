
def are_equal(s1, s2):

    if len(s1) != len(s2):
        return False
    
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            return False
    
    return True

def find_substring_naive(T, P):

    m = len(T)
    n = len(P)
    solution = []

    for i in range(0, m - n + 1):

        if are_equal(T[i:i+n],P):
            solution.append(i)
    
    return solution

if __name__ == "__main__":

    T = "abcxabcdabxabcd"
    P = "abcd"  
    print(find_substring_naive(T, P))   
