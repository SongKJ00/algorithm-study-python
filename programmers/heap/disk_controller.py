from queue import PriorityQueue
from collections import deque

class Disk:
  def __init__(self, req_time, task_time):
    self.req_time = req_time
    self.task_time = task_time
  def __lt__(self, other):
    return self.task_time < other.task_time

def solution(jobs):
  answer = 0
  curr_time = 0
  dq = deque(sorted(jobs))
  pq = PriorityQueue()

  while not pq.empty() or len(dq) > 0:
    while True:
      if len(dq) == 0: break
      if dq[0][0] > curr_time: break
      else:
        temp = dq.popleft()
        pq.put(Disk(req_time=temp[0], task_time=temp[1]))

    if not pq.empty():
      temp = pq.get()
      curr_time = curr_time + temp.task_time
      answer = answer + (curr_time - temp.req_time)
    else:
      if len(dq) > 0:
        curr_time = dq[0][0]

  return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))