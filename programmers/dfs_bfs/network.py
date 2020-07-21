def dfs(computer_idx, computers, visited):
  visited[computer_idx] = True
  for i, is_connected in enumerate(computers[computer_idx]):
    if i == computer_idx:
      continue

    if is_connected and not visited[i]:
      dfs(i, computers, visited)

def solution(n, computers):
  answer = 0
  visited = [False for i in range(n+1)]
  for i, x in enumerate(computers):
    if not visited[i]:
      dfs(i, computers, visited)
      answer = answer + 1

  return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))