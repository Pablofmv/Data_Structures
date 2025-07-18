# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def parent(i):
    return i // 2

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


def build_heap(n):
    return [None] + [(0,i) for i in range(n)]

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.

    thread_heap = build_heap(n_workers)

    n = len(thread_heap)

    size = n - 1

    for duration in jobs:
        free_time, thread_index = thread_heap[1]

        print(thread_index, free_time)
        
        thread_heap[1] = free_time + duration, thread_index

        sift_down(thread_heap, 1, size)
    

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assign_jobs(n_workers, jobs)

    """
    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)
    """


if __name__ == "__main__":
    main()
