from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  start = 1
  count = 0
  
  for Ci in C:
    end = Ci
    count += getMinMovement(N, start, end)
    start = Ci
  
  return count

def getMinMovement(N, start, end):
  if end < start:
    return getLesser(N+end-start, start-end)
  if start < end:
    return getLesser(end-start, N+start-end)
  return 0

def getLesser(forward, backward):
  if forward < backward:
    return forward
  return backward