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
        p=candidates[0]
        for candidate in candidates:
            if candidate%p == 0:
                candidates.remove(candidate)
        primes.append(p)
    return primes

print(sieve(15))
