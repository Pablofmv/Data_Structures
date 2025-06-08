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

def assign_jobs(n, jobs):

    heap = build_min_heap(n)
    size = n 
    print(heap)
    print(jobs)

    for duration in jobs:
        free_time, thread_index = heap[1]
        print(thread_index, free_time)

        heap[1] = (free_time + duration, thread_index)
        sift_down(heap, 1, size)

if __name__ == "__main__":
    n, m = map(int, input().split())
    jobs = list(map(int, input().split()))
    assign_jobs(n, jobs)