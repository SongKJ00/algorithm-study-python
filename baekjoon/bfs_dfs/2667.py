from collections import deque

N = int(input())
m = []
visited = []
for _ in range(N):
  m.append(list(map(int, list(input()))))
  visited.append([False]*N)

def bfs(y, x):
  cnt = 1
  q = deque()
  q.append((y, x))
  visited[y][x] = True
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]

  while q:
    curr_y, curr_x = q.popleft()
    for dir in range(4):
      next_y = curr_y + dy[dir]
      next_x = curr_x + dx[dir]
      if 0 <= next_y < N and 0 <= next_x < N:
        if not visited[next_y][next_x] and m[next_y][next_x] == 1:
          cnt += 1
          visited[next_y][next_x] = True
          q.append((next_y, next_x))

  return cnt

answer = []
for y in range(N):
  for x in range(N):
    if not visited[y][x] and m[y][x] == 1:
      answer.append(bfs(y, x))

print(len(answer))
for a in sorted(answer):
  print(a)