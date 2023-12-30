from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  
  shipSpaces = 0
  for row in G:
    shipSpaces += sum(row)
  
  return shipSpaces / (R * C)