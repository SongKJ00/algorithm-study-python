def solution(n, s):
  if n > s:
    return [-1]

  answer = []
  init_val = s // n
  remain = s % n
  for i in range(n):
    answer.append(init_val)

  idx = len(answer)-1
  for i in range(remain, 0, -1):
    answer[idx] += 1
    idx -= 1

  return answer

print(solution(2, 9))