def contains_duplicate(input)-> bool:
  temp = []
  for i in input:
    if i in temp:
      return True # Found a duplicate, return True
    else:
      temp.append(i) 
  return False  # No duplicates found, return False
