import math
import multiprocessing
import itertools
from timeit import Timer


def check_prime(n):
    if n % 2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_sequential():
    primes = []
    number_range = xrange(100000000, 101000000) 
    for possible_prime in number_range:
        if check_prime(possible_prime):
            primes.append(possible_prime)
    print len(primes), primes[:10], primes[-10:]


def primes_parallel():
    pass


if __name__ == "__main__":
    t = Timer(lambda: primes_sequential())
    print "Completed sequential in %s seconds." % t.timeit(1)

    t = Timer(lambda: primes_parallel())
    print "Completed parallel in %s seconds." % t.timeit(1)
    

