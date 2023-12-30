from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here
  count = 0
  for i in range(N-1, 0, -1):
    j = i-1
    if R[i] > R[j]:
      continue
      
    if R[i] == 1:
      return -1

    count += 1
    R[j] = R[i] - 1
    
  return count    