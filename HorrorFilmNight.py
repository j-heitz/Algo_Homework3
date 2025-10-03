import sys
input = sys.stdin.readline
# Read input
emma_data = list(map(int, input().split()))
marcos_data = list(map(int, input().split()))
# Build film array using sets (order-independent, touches only listed days)
emma = set(emma_data[1:])
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
# DP table
# H[i][last_disliked] = max films from day i to end
# last_disliked: 0 = nobody, 1 = Marcos, 2 = Emma
H = [[0]*3 for _ in range(n+1)]
# Bottom-up DP
for i in range(n-1, -1, -1):
    for d in range(3):
        # Default: skip current film
        H[i][d] = H[i+1][d]
        if film[i] == -1:
            continue  # neither likes → cannot watch
        elif film[i] == 2 and d != 2:  # Emma dislikes today, she didn't dislike yesterday
            H[i][d] = max(H[i][d], 1 + H[i+1][2])
        elif film[i] == 1 and d != 1:  # Marcos dislikes today, he didn't dislike yesterday
            H[i][d] = max(H[i][d], 1 + H[i+1][1])
        elif film[i] == 0:  # both like today → neutral, no restriction
            H[i][d] = max(H[i][d], 1 + H[i+1][0])
print(max(H[0][0], H[0][1], H[0][2]))


