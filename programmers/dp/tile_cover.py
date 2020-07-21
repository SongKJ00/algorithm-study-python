def solution(N):
  dp = [0 for i in range(80+1)]
  dp[1], dp[2] = 1, 1
  for i in range(3, len(dp)):
    dp[i] = dp[i-1] + dp[i-2]

  if N == 1:
    return 4
  else:
    return 2*(dp[N]+(dp[N]+dp[N-1]))

print(solution(5))