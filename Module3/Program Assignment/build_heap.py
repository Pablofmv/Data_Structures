# python3

def parent(i):
    return i // 2

def left_child(i):
    return i * 2

def right_child(i):
    return i * 2 + 1

def sift_down(data, i, size, sort_set):

    maxIndex = i
    left = left_child(i)
    if left <= size and data[left] < data[maxIndex]:
        maxIndex = left
    
    right = right_child(i)
    if right <= size and data[right] < data[maxIndex]:
        maxIndex = right
    
    if i != maxIndex:
        sort_set.append((i - 1, maxIndex - 1))
        data[i], data[maxIndex] = data[maxIndex] ,data[i]
        sift_down(data, maxIndex, size, sort_set)



def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    
    A = [None] + data[:]
    n = len(data)
    size = n
    sort_set = []

    for i in range(n//2, 0, -1):
        sift_down(A, i, size, sort_set)
    
    return sort_set


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    
    print(swaps)
    print(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
