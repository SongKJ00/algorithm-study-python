import csv

f = open('input.csv', 'r')
rdr = csv.reader(f)
for line in rdr:
  input_arr = list(map(int, line))

input_arr[1] = 12
input_arr[2] = 2

idx = 0
while True:
  op_code = input_arr[idx]
  if op_code == 99:
    break
  nums = [input_arr[input_arr[idx+1]], input_arr[input_arr[idx+2]]]
  idx_to_save = input_arr[idx+3]
  if op_code == 1:
    input_arr[idx_to_save] = nums[0] + nums[1]
  else:
    input_arr[idx_to_save] = nums[0] * nums[1]
  idx = idx + 4

print(input_arr[0])