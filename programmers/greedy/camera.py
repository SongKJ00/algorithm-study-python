def solution(routes):
  answer = 1
  routes.sort(key=lambda x: x[0])
  prev = routes[0]
  for i in range(1, len(routes)):
    curr = routes[i]
    if curr[1] < prev[1]:
      prev = curr
    elif curr[0] > prev[1]:
      answer = answer + 1
      prev = curr

  return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))