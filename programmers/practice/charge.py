def solution(n, money):
  answer = 0
  money = [0] + sorted(money)
  dp = [[0 for i in range(n+1)] for i in range(len(money))]

  for i in range(1, len(money)):
    for j in range(n+1):
      dp[i][j] = dp[i-1][j]
      if j == money[i]:
        dp[i][j] += 1
      elif j > money[i]:
        dp[i][j] += dp[i][j-money[i]]

  answer = dp[len(dp)-1][n]
  return answer

print(solution(5, [1, 2, 5]))