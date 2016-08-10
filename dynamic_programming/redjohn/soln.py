import sys
sys.stdin = open("/home/maksim/dev_projects/hackerrank/dynamic_programming/redjohn/input/input09.txt", "r")
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2): # skip all multiples of 2 and don't need to consider
                                                                # larger than sqrt(n) since n=pq implies prime factors are smaller than
                                                                # sqrt(n)
        if sieve[i]: # skip if already crossed out
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1) # start with i^2 and cross out all *odd* (that's the 2*i) multiples of i in a slick way
    return [2] + [i for i in range(3,n,2) if sieve[i]]

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    # the problem is similar to fibonacci: let A[i] be the number of arrangments
    # for a wall of length i. then we can take a step to a smaller problem by using
    # a 4x1 tile at the end, in which case we need to solve A[i-1], or we can use 
    # 4 1x4 tiles, in which case we have to solve A[i-4]. both are valid ways to 
    # explore possible arrangments. hence the total number of arrangements
    # for a wall of length i is their sum: 
    # A[i] = A[i-1]+A[i-4]
    # the base cases are A[0]=A[1]=A[2]=A[3]=1
    A = n*[0]
    A[0]=A[1]=A[2]=A[3]=1
    i = 4
    while i <= n:
        A[i] = A[i-1]+A[i-4]
        i +=1
    print(len(primes(A[-1])))