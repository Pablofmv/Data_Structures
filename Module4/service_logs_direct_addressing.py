def ip_to_int(ip):
    parts = list(map(int, ip.split('.')))
    return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

def update_access_list(logs, i, j, A, now):

    while i < len(logs) and logs[i][0] <= now:
        ip = ip_to_int(logs[i][1])
        A[ip] += 1
        i += 1
    
    while j < len(logs) and logs[j][0] <= now - 3600:
        ip = ip_to_int(logs[j][1])
        A[ip] -= 1
        j += 1
    
    return i,j

def accessed_last_hour(ip_str, A):
    return A[ip_to_int(ip_str)] > 0

if __name__ == "__main__":

    logs = [
        (1000,"1.1.1.1"),
        (2000,"2.2.2.2"),
        (3000,"2.2.2.2"),
        (4600,"3.3.3.3")
    ]

    logs.sort()

    A = [0] * (2**32)

    i = 0
    j = 0
    now = 4800

    i, j = update_access_list(logs, i, j , A, now)

    for ip in ["2.2.2.2", "3.3.3.3", "4.4.4.4"]:
        print(accessed_last_hour(ip,A))

