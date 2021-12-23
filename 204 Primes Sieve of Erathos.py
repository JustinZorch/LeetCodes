import math

def countpimes(n):

    num = 2
    prime_vals = []
    #create an array of True values with index values representing 0,1,2,3,4....n
    primes = [True]*(n+1)

    while num**2 <= n:

        #only evaluate if True(not yet a divisor)
        if primes[num] == True:

           #loop over in mutiples of n starting from n^2
           for i in range(num**2,n,num):
                primes[i] = False

        num += 1

    #find the primes
    for j in range(2,len(primes)-1):
        if primes[j] == True:
            prime_vals.append(j)

    return len(prime_vals )

n = 5000000
countprimes(n)