answer = 0

def check(y, x, n, row):
  for i in range(y):
    if x == row[i] or abs(x - row[i]) == y-i:
      return False
  return True

def dfs(y, n, row):
  global answer
  if y == n:
    answer += 1
    return

  for i in range(n):
    if check(y, i, n, row):
      row[y] = i
      dfs(y+1, n, row)

def solution(n):
  row = [0] * n
  dfs(0, n, row)

  return answer

print(solution(4))