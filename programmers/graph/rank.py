def solution(n, results):
  answer = 0
  win = [set() for i in range(n+1)]
  lose = [set() for i in range(n+1)]

  for r in results:
    win[r[0]].add(r[1])
    lose[r[1]].add(r[0])

  for i in range(1, n+1):
    for winner in lose[i]:
      win[winner].update(win[i])
    for loser in win[i]:
      lose[loser].update(lose[i])

  for winners, losers in zip(win, lose):
    if len(winners) + len(losers) == n-1:
      answer += 1

  return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))