"""Computing primes."""


def sieve(n): # : int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = [] 
    while candidates:
        i=1
        length = len(candidates)
        while i < length:
            if candidates[i] % candidates[0] == 0:
                    candidates.remove(candidates[i])
                    length -= 1
            else: 
                i += 1 
        primes.append(candidates[0])
        del candidates[0]
    return primes

print(sieve(15))
