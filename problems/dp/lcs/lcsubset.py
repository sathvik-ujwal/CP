# longest common subset

def lcs(str1: str, str2: str) -> int:
    n, m = len(str1), len(str2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    max_length = 0

    for i in range(1,n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                max_length = max(max_length, dp[i][j])
            

    return max_length