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

def BuildHeap(A):

    n = len(A)
    size = n - 1

    for i in range(size // 2, 0, -1):
        sift_down(A, i, size)

    return size

def HeapSort(orig):

    A = [None] + orig[:]
    size = BuildHeap(A)

    for i in range(0, size -1):
        A[1], A[size] = A[size], A[1]
        size -= 1
        sift_down(A, 1, size)
    
    return A[1:]

if __name__ == "__main__":
    A = [7,2,5,1,9,3]
    print(HeapSort(A))
