import csv
import copy
f = open('input.csv', 'r')
rdr = csv.reader(f)

for line in rdr:
  origin_arr = list(map(int, line))

result = 0
for i in range(100):
  for j in range(100):
    input_arr = copy.deepcopy(origin_arr)

    input_arr[1] = i
    input_arr[2] = j

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

    if input_arr[0] == 19690720:
      result = 100 * input_arr[1] + input_arr[2]
      print(result)