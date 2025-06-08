def parent(i):
    return i //2

def left_child(i):
    return i * 2

def right_child(i):
    return i * 2 + 1

def sift_down(A, i, size):

    minIndex = i
    left = left_child(i)
    if left <= size and A[left] < A[minIndex]:
        minIndex = left
    
    right = right_child(i)
    if right <= size and A[right] < A[minIndex]:
        minIndex = right
    
    if i != minIndex:
        A[i], A[minIndex] = A[minIndex], A[i]
        sift_down(A, minIndex, size)

def build_min_heap(n):

    return [None] + [(0,i) for i in range(0,n)]

if __name__ == "__main__":
    A = [1,2,3,4,5]
    build_min_heap(A)
    print(A)