from collections import deque

def solution(operations):
  dq = deque()

  for op in operations:
    opcode = op[0]
    number = int(op[2:])

    if opcode == 'I':
      dq.append(number)
      dq = deque(sorted(dq))
    else:
      if dq:
        if number == 1:
          dq.pop()
        else:
          dq.popleft()

  if not dq:
    return [0, 0]
  elif len(dq) == 1:
    num = dq.pop()
    return [num, num]
  else:
    return [dq.pop(), dq.popleft()]

print(solution(['I 7','I 5','I -5','D -1']))