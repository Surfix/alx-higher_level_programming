#!/usr/bin/python3
for i in range(10):
  for j in range(1,10):
    if i < j:
      if i == 8 and j == 9:
        print(f"{i}{j}\n")
      else:
        print(f"{i}{j}, ")
