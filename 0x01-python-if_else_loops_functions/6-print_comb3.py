#!/usr/bin/python3
for i in range(10):
  for j in range(1,10):
    if i < j:
      if i == 8 and j == 9:
        print("{}{}\n".format(i,j))
      else:
        print("{i}{j}, ".format(i,j))
