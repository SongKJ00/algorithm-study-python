import sys
sys.setrecursionlimit(10**6)

class Disjoints:
  def __init__(self, n):
    self.root = [i for i in range(n)]
    self.rank = [0 for i in range(n)]

  def find(self, x):
    if self.root[x] == x:
      return x
    else:
      self.root[x] = self.find(self.root[x])
      return self.root[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return False

    if self.rank[x] < self.rank[y]:
      self.root[x] = y
    else:
      self.root[y] = x
      if self.rank[x] == self.rank[y]:
        self.rank[x] = self.rank[x] + 1
    return True

def solution(n, costs):
  disjoints = Disjoints(n)
  answer = 0
  connected_cnt = 0
  for edge in sorted(costs, key=lambda x: x[2]):
    start, end, cost = edge
    if disjoints.union(start, end):
      answer = answer + cost
      connected_cnt = connected_cnt + 1
      if connected_cnt == (n - 1):
        break

  return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))