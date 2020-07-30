import math

def solution(n, k):
  answer = []
  num_list = [i for i in range(1, n+1)]
  k -= 1
  while n > 0:
    fac = math.factorial(n-1)
    pop_idx = k // fac
    k = k % fac
    answer.append(num_list.pop(pop_idx))
    n -= 1

  return answer

print(solution(4, 9))