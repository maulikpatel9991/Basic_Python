# Python has two primitive loop commands:
#
# while loops
# for loops
# break statement we can stop the loop
# continue statement we can stop the current iteration, and continue with the next

i = 1
while i < 6:
  print(i)
  i += 1
#########break #######
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

################ continue ############
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)