# This code has a few issues when not prime numbers are inputted. The output prints "Not Prime Not Prime Not Prime" etc. It has something to do with the for loop, but I'm not sure if it needs a break or something else.

n = input()
# make sure n is a positive integer
n = abs(int(n))

# 0 and 1 are not primes
if n < 2:
    print("Not Prime")

  # 2 is the only even prime number
if n == 2: 
    print("Prime")    
  
    # all other even numbers are not primes
if not n & 1: 
    print("Not Prime")

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
for x in range(3, int(n**0.5) + 1, 2):
    if n % x == 0:
      print("Not Prime")
    else:
      print("Prime")
    break
