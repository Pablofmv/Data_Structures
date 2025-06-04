def parent(i):
    return i // 2

def left_child(i):
    return i * 2

def right_child(i):
    return i * 2 + 1

def sift_down(A, i, size):

    maxIndex = i
    left = left_child(i)
    if left <= size and A[left] > A[maxIndex]:
        maxIndex = left
    
    right = right_child(i)
    if right <= size and A[right] > A[maxIndex]:
        maxIndex = right
    
    if i != maxIndex:
        A[i], A[maxIndex] = A[maxIndex], A[i]
        sift_down(A, maxIndex, size)


def build_heap(A):

    n = len(A)
    size = n - 1

    for i in range(n//2, -1, -1):
        sift_down(A, i, size)
    
    return A

if __name__ == "__main__":

    A = [1,2,3]
    heap = build_heap(A)
    print(heap)