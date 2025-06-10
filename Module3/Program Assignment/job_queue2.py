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
    return [None] + [(0,x) for x in range(0,n)]

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    heap_thread = build_heap(n_workers)
    assigned_jobs = []

    for duration in jobs:
        free_time, thread_index = heap_thread[1]

        assigned_jobs.append([thread_index, free_time])
        heap_thread[1] = free_time + duration, thread_index

        sift_down(heap_thread, 1, n_workers)
    
    return assigned_jobs



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs


    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])

if __name__ == "__main__":
    main()
