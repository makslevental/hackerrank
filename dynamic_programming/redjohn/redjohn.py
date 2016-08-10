from math import factorial as fac
import sys
sys.stdin = open("/home/maksim/dev_projects/hackerrank/dynamic_programming/redjohn/input/input09.txt", "r")

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * int(n/3)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      int((k*k)/3)      :int(2*k)]=[False]*int((n/6-(k*k)/6-1)/k+1)
            sieve[int(k*k+4*k-2*k*(i&1))//3:int(2*k)]=[False]*int((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in range(1,int(n//3-correction)) if sieve[i]]

def binomial(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())

    combs = [binomial(n-3*k, k) for k in range(1,n//4+1)]
#     print(combs)
    combs = sum(combs)+1
    
#     combs = sum(combs[:-1]) + 1
    if combs == 1:
        print(0)
    elif combs == 2:
        print(1)
    elif 3 <=combs <=4 :
        print(2)
    elif 5 <= combs <= 6:
        print(3)
    else:
        ps = rwh_primes1(combs+1)
        print(len(ps))
#         print(ps)
#     print()

# print(rwh_primes1(100+1))        
            