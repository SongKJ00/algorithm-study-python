def solution(weight):
  answer = 0
  curr_sum = 0
  for w in sorted(weight):
    if w - curr_sum <= 1:
      curr_sum += w
    else:
      answer = curr_sum + 1
      return answer
    
  return curr_sum + 1

print(solution([3, 1, 6, 2, 7, 30, 1]	))