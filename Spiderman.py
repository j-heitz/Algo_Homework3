import sys
input = sys.stdin.readline
INF = float('inf')
T = int(input())
for _ in range(T):
    X = int(input())
    d = list(map(int, input().split()))
    S = [[INF] * 2001 for _ in range(X + 1)]
    state = [[0] * 2001 for _ in range(X + 1)]
    S[0][0] = 0
    for i in range(1, X + 1):
        for h in range(2001):
            # Down move
            if h + d[i - 1] < 2001 and S[i-1][h + d[i - 1]] != INF:
                peak = S[i-1][h + d[i - 1]]
                if peak < S[i][h]:
                    S[i][h] = peak
                    state[i][h] = (h + d[i - 1], 'D')
            # Up move
            if h >= d[i - 1] and S[i-1][h - d[i - 1]] != INF:
                peak = max(S[i-1][h - d[i - 1]], h)
                if peak < S[i][h]:
                    S[i][h] = peak
                    state[i][h] = (h - d[i - 1], 'U')
    if S[X][0] == INF:
        print("IMPOSSIBLE")
    else:
        moves = []
        h = 0
        for i in range(X, 0, -1):
            prev_h, move = state[i][h]
            moves.append(move)
            h = prev_h
        print(''.join(reversed(moves)))