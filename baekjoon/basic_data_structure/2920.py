inputs = list(input().split())

is_ascending = False
is_descending = False

for i in range(len(inputs)-1):
  if inputs[i] < inputs[i+1]:
    is_ascending = True
  else:
    is_descending = True

if is_ascending and not is_descending:
  print('ascending')
elif not is_ascending and is_descending:
  print('descending')
else:
  print('mixed')