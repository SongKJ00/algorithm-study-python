import csv

class IntCode:
  def __init__(self, first, second):
    f = open('input.csv', 'r')
    rdr = csv.reader(f)
    for line in rdr:
      input_arr = list(map(int, line))

