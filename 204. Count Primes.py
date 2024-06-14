class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        primes = [i for i in range(2, n)]
        for i in range(2, n):
            for prime in primes:
                if i ** (prime - 1) % prime != 1 and prime > i:
                    primes.remove(prime)
        return len(primes)        
