def cent_savings():
    import sys
    input = sys.stdin.readline

    n, d = map(int, input().split())
    prices = list(map(int, input().split()))

    # prefix sums to compute group totals fast
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + prices[i]

    # rounding function
    def rounded(x):
        return ((x + 5) // 10) * 10

    # dp[i][g] = min cost for first i items using g groups
    INF = 10**15
    dp = [[INF] * (d + 2) for _ in range(n + 1)]
    dp[0][0] = 0  # base case: 0 items, 0 groups = 0 cost

    for i in range(1, n + 1):           # first i items
        for g in range(1, d + 2):       # up to g groups
            for j in range(i):          # cut before j
                group_sum = prefix[i] - prefix[j]
                dp[i][g] = min(dp[i][g], dp[j][g - 1] + rounded(group_sum))

    # answer = min cost for all items with up to d+1 groups
    print(min(dp[n]))


if __name__ == "__main__":
    cent_savings()