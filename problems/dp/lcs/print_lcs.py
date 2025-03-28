def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[n-1] == s2[m-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    x,y= n,m
    res = ""
    while x > 0 and y > 0:
        if s1[x-1] == s2[y-1]:
            res = s1[x-1] + res
            x -= 1
            y -= 1
        else:
            if dp[x-1][y] > dp[x][y-1]:
                x -= 1
            else:
                y -= 1
    return res


if __name__ == "__main__":
    s1 = "abcqed"
    s2 = "abcwd"
    res = findLCS(len(s1), len(s2) , s1, s2)
    print(res)
    
    
    
    