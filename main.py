from datetime import datetime
import time


# Part 1
def clock(n):
  """
  clock return time

  the first number
  n -> int
  """
  prev = ""
  while (n>0):
    timenow = datetime.now()
    timenow = timenow.strftime("%H:%M:%S")
    if (prev!=timenow):
      prev = timenow
      print(timenow, end='')
      print("\r", end='')
      n-=1

  


# Part 2
def lcm(a, b):
  """
  lcm return lowerest common multiple of a, b
  the first number a -> int
  the second number b -> int
  """
  #return a*b//gcd(a,b)
  original_a = a
  original_b = b
  while (a!=b):
    if a<b:
      a += original_a
    else:
      b += original_b

  return a



# Part 3
def gcf(a, b):
  """
  gcf return greatest common factor of a, b
  the first number a -> int
  the second number b -> int
  """
  while a!=0:
    newa = b%a
    b = a
    a = newa
  return b

clock(3)