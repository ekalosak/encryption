import numpy as np
import math

def prime(upto=100):
    ''' http://rebrained.com/?p=458 '''
    return [1] + filter(lambda num: (num %
        np.arange(2,1+int(math.sqrt(num)))).all(), range(2,upto+1))

def prime_factors(n):
    pfac = [(1, 1)]   # List of tuples (p, e) by FTA
    primes = prime(int(math.sqrt(n)) + 1)
    for p in primes:
        if p == 1: continue
        e = 0
        while not n % p:    # while n still divides p
            e = e + 1
            n = n / p   # chop away at the prime factorization
        if e:
            pfac = pfac + [(p, e)]
    if n > primes[-1]: pfac = pfac + [(n, 1)]    # if n was prime to begin with
    return pfac

def gcd(a, b):
    pfa = prime_factors(a)
    pfb = prime_factors(b)
    g = 1
    for p, e in pfa:
        for q, f in pfb:
            if p == q:
                g = g * p ** min(e, f)
    return g

def inv(e, t):
    # TODO implement Euler's extended algorithm
    for d in range(2, t):
        if e * d % t == 1:
            return d

def tests():
    assert prime(10) == [1, 2, 3, 5, 7]
    assert prime_factors(10) == [(1, 1), (2, 1), (5, 1)]
    assert gcd(5, 7) == 1
    assert gcd(10, 20) == 10
    assert gcd(40, 100) == 20
    assert inv(5, 7) == 3   # 3 * 5 mod 7 == 1
    print "Passed tests!!"

if __name__ == '__main__':
    tests()
