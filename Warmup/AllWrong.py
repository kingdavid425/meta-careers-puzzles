# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  wrongAnswers = ''
  for i in range(N):
    if C[i] == 'A':
      wrongAnswers += 'B'
    else:
      wrongAnswers += 'A'
  
  return wrongAnswers