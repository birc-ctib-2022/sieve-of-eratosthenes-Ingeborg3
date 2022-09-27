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

# faster version, where elements are added to list (faster) instead of
# being removed from the middle of a list (slower).

def sieve2(n):
    candidates = list(range(2,n+1))
    primes = []
    while candidates:
        p, remaining_candidates = candidates[0], []
        primes.append(p)
        for cand in candidates:
            if cand % p != 0:
                remaining_candidates.append(cand)
        candidates = remaining_candidates
    return primes

print(sieve2(15))

# faster version where list comprehension is used.
def sieve3(n):
    candidates = list(range(2,n+1))
    primes = []
    while candidates:
        primes.append(candidates[0])
        candidates = [candidate for candidate in candidates if candidate % primes[-1] != 0] 
    return primes

print(sieve3(15))

# Even faster version.

def sieve4(n):
    candidates = [False]*2 + [True]*(n-1)
    i = 2
    while i*i < n:
        if not candidates[i]: # If candidate[0] is False, not candidate[0] is 
            # True and the if-body is executed. 
            break # break while-loop.
        for j in range(i**2, n+1, i): # nb i**2 must be used, not i^2.
            candidates[j] = False
        i += 1
    
    return [i for i, b in enumerate(candidates) if b]

    # The list returned can be made as below instead of list 
    # comprehension:
candidates = [False]*2 + [True]*14
lst = []
for i, b in enumerate(candidates):
    if b:
        lst.append(i)
print(lst) # non-primes still in list. 

print(sieve4(15))
