
def parents(i):
    return i // 2

def left_child(i):
    return i * 2

def right_child(i):
    return i * 2 + 1





def thread_heap(n):
    return [None] + [(0,i) for i in range(n)]

def assign_jobs(n, m, jobs):



if __name__ == "__main__":
    n, m = input().split()
    jobs = list(map(int, input().split()))

    assign_jobs(n,m,jobs)