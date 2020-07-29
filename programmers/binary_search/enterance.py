def solution(n, times):
  answer = 0
  left, right = 1, max(times)*n

  while left <= right:
    mid = (left + right) // 2
    s = 0
    for time in times:
      s = s + (mid // time)
    if s >= n:
      answer = mid
      right = mid - 1
    else:
      left = mid + 1

  return answer

print(solution(6, [7, 10]))