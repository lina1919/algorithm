def solution(land):
    answer = 0
    dp = []
    temp = [0]
    for _ in range(len(land)+1):
        dp.append([0,0,0,0,0])
    cnt = 1
    for i in land:
        for j in i:
            temp.append(j)
        dp[cnt] = temp
        cnt += 1
        temp = [0]
        
    for i in range(2,len(land)+1):
        for j in range(1,5):
            if j == 1:
                dp[i][j] = dp[i][j] + max(dp[i-1][2], dp[i-1][3], dp[i-1][4])
            elif j == 2:
                dp[i][j] = dp[i][j] + max(dp[i-1][1], dp[i-1][3], dp[i-1][4])
            elif j == 3:
                dp[i][j] = dp[i][j] + max(dp[i-1][1], dp[i-1][2], dp[i-1][4])
            elif j == 4:
                dp[i][j] = dp[i][j] + max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
        
        answer = max(dp[len(land)])
    return answer
