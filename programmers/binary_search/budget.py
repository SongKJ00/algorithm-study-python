def solution(budgets, M):
  answer = 0
  left, right = 0, max(budgets)
  while left <= right:
    mid = (left + right) // 2
    print(mid)
    temp_sum = 0
    for budget in budgets:
      if budget <= mid:
        temp_sum = temp_sum + budget
      else:
        temp_sum = temp_sum + mid

    if temp_sum <= M:
      answer = mid
      left = mid+1
      if temp_sum == M:
        break
    else:
      right = mid-1

  return answer

print(solution([120, 110, 140, 150], 485))