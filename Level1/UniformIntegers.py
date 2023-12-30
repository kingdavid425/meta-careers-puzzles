# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here
  i = 1
  commonInc = 1
  endInc = 2
  candidate = 1
  
  count = 0
  while candidate <= B:
    if A <= candidate:
      count += 1
    
    if candidate % 10 == 9:
      candidate += endInc
      commonInc = (commonInc * 10) + 1
      endInc = endInc + 10**i
      i += 1
    else:
      candidate += commonInc
    
  return count