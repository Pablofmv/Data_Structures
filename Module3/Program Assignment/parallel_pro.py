def parent(i):
    return i //2

def left_child(i):
    return i * 2

def right_child(i):
    return i * 2 + 1

def sift_down(A, i, size):

    minIndex = i
    left = left_child(i)
    if left <= size and left < minIndex:
        minIndex = left
    
    right = right_child(i)
    if right <= size and right < minIndex:
        minIndex = right
    
    if i != minIndex:
        i, minIndex = minIndex, i
        sift_down(A, minIndex, size)

def build_min_heap(A):

    A = [None] + A[:]
    n = len(A)
    size = n - 1
    output = []

    for i in range(n // 2, -1, -1):
        sift_down(A, i, size, output)
    
    return size

if __name__ == "__main__":
    A = [1,2,3,4,5]
    build_min_heap(A)
    print(A)