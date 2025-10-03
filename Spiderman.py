import sys
input = sys.stdin.readline
INF = float('inf')

T = int(input())  # number of test cases
for j in range(T):
    M = int(input())  # number of climbing stages
    d = list(map(int, input().split()))  # distances
    # DP table
    S = [[INF] * 2001 for _ in range(M + 1)]
    path = [[0] * 2001 for _ in range(M + 1)]
    S[0][0] = 0
    for i in range(1, M + 1):
        climb = d[i - 1]
        for h in range(2001):
            # DOWN move
            if h + climb < 2001 and S[i-1][h + climb] != INF:
                peak = S[i-1][h + climb]
                if peak < S[i][h]:
                    S[i][h] = peak
                    path[i][h] = (h + climb, 'D')
            # UP move
            if h >= climb and S[i-1][h - climb] != INF:
                peak = max(S[i-1][h - climb], h)
                if peak < S[i][h]:
                    S[i][h] = peak
                    path[i][h] = (h - climb, 'U')
    if S[M][0] == INF:
        print("IMPOSSIBLE")
    else:
        moves = []
        h = 0
        for i in range(M, 0, -1):
            prev_h, move = path[i][h]
            moves.append(move)
            h = prev_h
        print(''.join(reversed(moves)))
