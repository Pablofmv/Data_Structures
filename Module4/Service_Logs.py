



def update_access_list(logs, i, j , C , now):

    while i < len(logs) and logs[i][0] <= now:
        ip = logs[i][1]
        if ip in C:
            C[ip] += 1
        else:
            C[ip] = 1
        i += 1
    
    while i < len(logs) and logs[i][0] <= now - 3600:
        ip = logs[i][1]
        C[ip] -= 1
        j += 1
    
    return i, j

if __name__ == "__main__":

    logs = [(1000, "1.1.1.1"),(1100, "2.2.2.2"),(4600, "3.3.3.3")]

    logs.sort()

    i = 0
    j = 0
    C = {}
    now = 4700

    i , j = update_access_list(logs, i, j, C , now)