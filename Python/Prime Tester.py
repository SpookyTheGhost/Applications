import math
def isPrime(n):
    if (n <= 1): # base case
        #print("invalid")
        return False

    elif (n <= 3):
        #print("input is either 2 or 3")
        return True
    
    elif (n % 2 == 0 or n % 3 == 0): 
        return False

    i = 4
    while (i <= math.sqrt(n)):
        if (n % i == 0):
            return False
        #faulty
        #if (n % (6*i+1) == 0 or n % (6*i-1) == 0): # analysis that primes are of form 6k+1 or 6k-1
            #return False

        i += 1
    return True
                

print( sum([1 for i in range(501) if (isPrime(i) == True)]) ) # prints 95
for i in range(501):
    if (isPrime(i) == True):
        print(i)
