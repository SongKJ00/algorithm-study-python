
input_map = []
asteroid_locations = []

# Get input map
with open('input.txt', 'r') as f:
  while True:
    line = f.readline()
    if not line:
      break
    else:
      line = line.split('\n')[0]
      input_map.append([x for x in line])

# Get asteroid locations
for i, y in enumerate(input_map):
  for j, x in enumerate(y):
    if input_map[i][j] == '#':
      asteroid_locations.append((j, i))

print(asteroid_locations)
res = 0
for start_x, start_y in asteroid_locations:
  s = set()
  flags = [False]*4
  for target_x, target_y in asteroid_locations:
    if start_x == target_x and start_y == target_y:
      pass
    else:
      if target_y == start_y:
        if target_x > start_x:
          flags[0] = True
        else:
          flags[1] = True
      elif target_x == start_x:
        if target_y > start_y:
          flags[2] = True
        else:
          flags[3] = True
      else:
        m = (target_y - start_y) / float((target_x - start_x))
        if target_x > start_x:
          direction = True
        else:
          direction = False
        s.add((m, direction))
  print(s)
  temp = 0
  for flag in flags:
    if flag:
      temp = temp+1
  res = max(res, len(s)+temp)

print(res)