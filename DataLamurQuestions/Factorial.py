def factorial(n):
  temp = n 
  empty = 1
  for i in range(n,0,-1):
    empty = i*empty
  return empty  
