answer = []
max_depth = 0
adjs = {}
visited_cnt = {}

def dfs(curr):
  answer.append(curr)

  if len(answer) == max_depth:
    return
  if adjs.get(curr) is None:
    answer.pop()
    return

  for i, _ in enumerate(adjs[curr]):
    next_area = adjs[curr][i]
    if visited_cnt[(curr, next_area)] != 0:
      visited_cnt[(curr, next_area)] = visited_cnt[(curr, next_area)]-1
      dfs(next_area)
      if len(answer) == max_depth:
        return
      visited_cnt[(curr, next_area)] = visited_cnt[(curr, next_area)]+1

  answer.pop()

def solution(tickets):
  global max_depth
  max_depth = len(tickets)+1
  for ticket in tickets:
    adjs[ticket[0]] = []
    visited_cnt[(ticket[0], ticket[1])] = 0
  for ticket in tickets:
    adjs[ticket[0]].append(ticket[1])
    visited_cnt[(ticket[0], ticket[1])] = visited_cnt[(ticket[0], ticket[1])]+1

  for k, v in adjs.items():
    v.sort()

  dfs('ICN')
  return answer

print(solution([['ICN','A'],['ICN','A'],['A','ICN']]))