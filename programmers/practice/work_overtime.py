import heapq

def solution(n, works):
  answer = 0
  if sum(works) <= n:
    return 0

  heap = []
  for w in works:
    heapq.heappush(heap, (-w, w))

  while n > 0:
    curr = heapq.heappop(heap)[1]
    curr -= 1
    n -= 1
    heapq.heappush(heap, (-curr, curr))

  for i in heap:
    answer += i[1] ** 2

  return answer

print(solution(4, [4, 3, 3]))