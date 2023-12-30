from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  ones = 0
  twos = 0
  
  S = set(S)
  for Si in S:
    if Si // 2 > twos:
      twos = Si // 2
      
    if Si % 2 > ones:
      ones = Si % 2
    
  return twos + ones