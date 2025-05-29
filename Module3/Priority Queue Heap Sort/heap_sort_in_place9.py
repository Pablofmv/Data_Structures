def parent(i):
    return i //2 

def left_child(i):
    return i * 2

def right_child(i):
    return i * 2 + 1

def sift_down(A, i, size):

    maxSize = i
    left = left_child(i)
    if left <= size and A[left] > A[maxSize]:
        maxSize = left
    
    right = right_child(i)
    if right <= size and A[right] > A[maxSize]:
        maxSize = right
    
    if i != maxSize:
        A[i], A[maxSize] = A[maxSize], A[i]
        sift_down(A, maxSize, size)
    
def build_heap(A):

    n = len(A)
    size = n - 1

    for i in range(n // 2, 0, -1):
        sift_down(A, i, size)
    
    print(A)
    return size

def sort_heap(A):

    A = [None] + A[:]
    size = build_heap(A)
    
    for i in range(0, size - 1):
        A[1], A[size] = A[size], A[1]
        size -= 1
        sift_down(A, 1, size)

    return A[1:]



if __name__ == "__main__":
    A = [7,2,5,1,9,3]

    print(sort_heap(A))