import sys
input = sys.stdin.readline
# n is number of items, d is number of dividers
n, d = map(int, input().split())
prices = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + prices[i-1]
def round10(x):
    return ((x + 5) // 10) * 10
INF = float('inf')
C = [[INF] * (d + 1) for _ in range(n + 1)]
for k in range(d + 1):
    C[0][k] = 0
for i in range(1, n + 1):
    for k in range(d + 1):
        if k == 0:
            # No dividers
            C[i][k] = round10(prefix[i])
        else:
            for j in range(i):
                cost = C[j][k-1] + round10(prefix[i] - prefix[j])
                if cost < C[i][k]:
                    C[i][k] = cost
print(C[n][d])