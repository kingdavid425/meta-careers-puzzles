from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  eaten = {}
  count = 0
  for i in range(N):
    Di = D[i]
    if Di not in eaten or count - eaten[Di] > K:
      eaten[Di] = count
      count += 1
      
  return count