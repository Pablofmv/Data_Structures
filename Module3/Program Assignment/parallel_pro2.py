def parent(i):
    return i // 2

def left_child(i):
    return i * 2

def right_child(i):
    return i * 2 + 1

def sift_down(A, i, size):

    minIndex = i
    left = left_child(minIndex)
    if left <= size and A[left] < A[minIndex]:
        minIndex = left
    
    right = right_child(minIndex)
    if right <= size and A[right] < A[minIndex]:
        minIndex = right
    
    if i != minIndex:
        A[minIndex], A[i] = A[i], A[minIndex]
        sift_down(A, minIndex, size)

def build_heap(n):
    return [None] + [(0,i) for i in range(0,n)]

def assign_jobs(n,m, jobs):
    
    threads_list = build_heap(n)
    
    for duration in jobs:
        
        time_free, thread = threads_list[1]

        print(thread, time_free)

        threads_list[1] = (time_free + duration, thread)

        sift_down(threads_list, 1, n + 1)
    


if __name__ == "__main__":
    n, m = map(int, input().split())
    jobs = list(map(int, input().split()))

    assign_jobs(n,m,jobs)