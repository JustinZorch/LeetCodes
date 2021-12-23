import math
from timeit import default_timer
def countprimes(n):

    #no primes
    if n <= 2:
        return 0

    #2 is the prime
    if n <= 3:
        return 1

    #2,3 are primes
    if n <= 5:
        return 2

    #2,3,5 are primes
    if n <= 7:
        return 3

    #2,3,5,7
    if n < 11:
        return 4

    primes = [2,3,5,7]

    #start from 3 and skip even numbers
    for num in range(9,n,2):

        #speed code up get rid of 3 and 5
        if num%3 != 0:
            if num%5 != 0:
                if num%7 != 0:

                    #if not then run a 2nd loop to check all the numbers between
                    p_val = True
                    for div in range(9,num,2):

                        #if divisor found break out of loop
                        if num % div == 0:
                            p_val = False
                            break

                    #if loop ends and no divisor found then prime
                    if p_val == True:
                        primes.append(num)




    print(len(primes))
    return len(primes)

def countprimesquare(n):

    t1 = default_timer()
    #no primes
    if n <= 2:
        return 0
    #2 is the prime
    if n <= 3:
        return 1
    #2,3 are primes
    if n <= 5:
        return 2
    #2,3,5 are primes
    if n <= 7:
        return 3
    #2,3,5,7
    if n < 11:
        return 4

    primes = [2,3,5,7]

    #start from 3 and skip even numbers
    for num in range(9,n,2):

        #speed code up get rid of 3 and 5
        #if num%3 != 0 and num%4 != 0 and num%5 != 0 and num%6 != 0 and num%7 != 0 and num%8 != 0:
        if num % 3 != 0:
            if num % 5 != 0:
                if num % 7 != 0:
                    #if not then run a 2nd loop to check all the numbers between
                    p_val = True
                    i = 0
                    sq = math.floor(math.sqrt(num))

                    #run through list as long as sq value is bigger than primes
                    while i <= len(primes) and primes[i]<= sq:
                        if num % primes[i] == 0:
                            #not a prime
                            p_val = False
                            break
                        i += 1

                    if p_val == True:
                        primes.append(num)

    print(len(primes))
    t2 = default_timer()
    print(t2-t1)
    return len(primes)


#superslow method
def countprimesfact(n):
    t1 = default_timer()

    #no primes
    if n <= 2:
        return 0
    #2 is the prime
    if n <= 3:
        return 1
    #2,3 are primes
    if n <= 5:
        return 2
    #2,3,5 are primes
    if n <= 7:
        return 3
    #2,3,5,7
    if n < 11:
        return 4

    primes = [2,3,5,7]

    #start from 3 and skip even numbers
    for num in range(9,n,2):

        #speed code up get rid of 3 and 5
        if num%3 != 0:
            if num%5 != 0:
                if num%7 != 0:

                    ##r k is prime then ((k-1)! + 1) % k must be 0.##
                    if (math.factorial(num-1)+1) % num == 0:
                        primes.append(num)

    print(len(primes))
    t2 = default_timer()
    print(t2-t1)
    return len(primes)


## Run Times##
#22.764057100000002 bnested if
#23.8511455 more conditions


n = 5000000
countprimesquare(n)