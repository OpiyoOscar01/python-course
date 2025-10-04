def analyse_numbers(numbers):
  if not numbers:
    return 0,0,0
  total=sum(numbers)
  number_of_items=len(numbers)
  average=total/number_of_items
  return total,number_of_items,average
numbers=[10,20,30,40,50]
total,count,avg=analyse_numbers(numbers)
print(f"Total: {total}, Count: {count}, Average: {avg}")