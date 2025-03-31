def solution(triangle):
    
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        for j in range(1, i+1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    return max(dp[n-1])
        