def isPrime(num, primed):
  all(x % num == 0 for x in primed)

  if num == 2:
    return True
  elif num < 2 or not num % 2 or (num != 3 and not num % 3):
    return False

  for i in range(3, int(num ** .5 + 1), 2):
    if not num % i:
      return False

  return True

def genPrimes(n):  
  primes = [2,]
  count = 1
  testNum = 3

  while count < n:
    if isPrime(testNum, primes):
      primes.append(testNum)
      count += 1
    testNum += 2

  return primes

import time
start = time.time()

all_primes = genPrimes(1000)
print all_primes
print sum(all_primes)

print time.time()-start, 'seconds.'
