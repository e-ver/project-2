def spce():
  print('\n__________________________________________')
def counts(x):
  count = 0
  while x > 0:
    x //= 10
    count += 1
  return count