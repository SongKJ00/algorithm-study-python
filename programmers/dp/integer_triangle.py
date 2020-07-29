def solution(triangle):
  answer = 0
  N = len(triangle) + 1
  dp = [[0 for i in range(N)] for j in range(N)]

  for i in range(1, len(dp)):
    for j in range(1, i+1):
      dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i-1][j-1]

  answer = max(dp[len(dp)-1])
  return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))