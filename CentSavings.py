import sys
input = sys.stdin.readline
# Read input
n, d = map(int, input().split())  # n = number of items, d = number of dividers
prices = list(map(int, input().split()))
# Build prefix sum array for fast group totals
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + prices[i-1]
# Function to round to nearest 10 cents
def round10(x):
    return ((x + 5) // 10) * 10
# DP table
# C[i][k] = minimum total cost to buy first i items using k dividers
C = [[float('inf')] * (d + 1) for _ in range(n + 1)]
# Base cases
for k in range(d + 1):
    C[0][k] = 0  # No items → cost 0
# Bottom-up DP
for i in range(1, n + 1):          # i = number of items considered
    for k in range(d + 1):         # k = number of dividers used
        if k == 0:
            # No dividers → pay for all items from 1 to i as a single group
            C[i][k] = round10(prefix[i])
        else:
            # Try putting the last divider after every possible previous item j
            for j in range(i):
                cost = C[j][k-1] + round10(prefix[i] - prefix[j])
                if cost < C[i][k]:
                    C[i][k] = cost
# Final answer: minimum cost for all n items using up to d dividers
print(C[n][d])
