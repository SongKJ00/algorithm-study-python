from collections import deque

def solution(n, edge):
  answer = 1
  adjs = [[] for i in range(n+1)]
  visited = [False for i in range(n+1)]
  for s, e in edge:
    adjs[s].append(e)
    adjs[e].append(s)

  q = deque()
  q.append((1, 0))
  visited[1] = True

  max_depth = 0
  while q:
    node, depth = q.popleft()
    node_adjs = adjs[node]
    if max_depth == depth:
      answer = answer + 1
    else:
      max_depth = depth
      answer = 1

    for node in node_adjs:
      if not visited[node]:
        q.append((node, depth+1))
        visited[node] = True

  return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))