from collections import deque

N, K = map(int, input().split())
visited = [False] * 200001
answer = 0
depth = 0

q = deque()
q.append((N, depth))
visited[N] = True
while q:
  curr_pos, d = q.popleft()
  if curr_pos == K:
    answer = d
    break

  next_poses = [curr_pos-1, curr_pos+1, curr_pos*2]
  for next_pos in next_poses:
    if 0 <= next_pos <= 200000:
      if not visited[next_pos]:
        visited[next_pos] = True
        q.append((next_pos, d+1))

print(answer)