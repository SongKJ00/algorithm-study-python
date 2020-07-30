def solution(n):
  answer = 0
  if n == 1 or n == 2:
    return n

  dp = [0 for i in range(n+1)]
  dp[1] = 1
  dp[2] = 2

  for i in range(3, len(dp)):
    dp[i] = dp[i-1] + dp[i-2]

  answer = dp[n] % 1234567
  return answer

print(solution(4))