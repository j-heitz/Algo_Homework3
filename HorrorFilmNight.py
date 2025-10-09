import sys
input = sys.stdin.readline
emmas_data = list(map(int, input().split()))
marcos_data = list(map(int, input().split()))
emma = set(emmas_data[1:])
marcos = set(marcos_data[1:])
max_day = max((emma | marcos) or {0})
n = max_day + 1
film = [-1] * n
for day in emma | marcos:
    if day in emma and day in marcos:
        film[day] = 0
    elif day in emma:
        film[day] = 2
    else:
        film[day] = 1
H = [[0]*3 for _ in range(n+1)]
for i in range(n-1, -1, -1):
    # d is the last diskliked
    for d in range(3):
        H[i][d] = H[i+1][d]
        if film[i] == -1:
            continue
        elif film[i] == 2 and d != 2:
            H[i][d] = max(H[i][d], 1 + H[i+1][2])
        elif film[i] == 1 and d != 1:
            H[i][d] = max(H[i][d], 1 + H[i+1][1])
        elif film[i] == 0 and d != 0:
            H[i][d] = max(H[i][d], 1 + H[i+1][0])
print(H[0][0])