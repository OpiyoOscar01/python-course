# #Nested loop is a loop inside another loop.
# for i in range(1,8):
#   for j in range(1,6):
#     result=i*j
#     print(f"{i} * {j} = {result:2d}",end=" ")
#   print() #For a new line after the inner loop completes.

#Printing a pattern using nested loops.
for i in range(1,6):
  for j in range(i):
    print("%",end=" ")
  print() #For a new line after the inner loop completes.