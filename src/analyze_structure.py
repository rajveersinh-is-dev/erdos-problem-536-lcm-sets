"""
Deeper analysis of Erdős Problem #536.

Key insight: [a,b]=[b,c]=[a,c] iff for every prime p,
at least two of a,b,c have the maximum exponent of p.

This is equivalent to: the "maximum" prime factorization is achieved
by at least two of the three elements.
"""

from collections import defaultdict
from math import gcd


def lcm(a, b):
    """Lcm.
    
    Args:
        a:
        b:
    
    Returns:
        The computed result
    
    """
    return a * b // gcd(a, b)


def prime_factors(n):
    """Return dict of prime -> exponent."""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def is_bad_triple(a, b, c):
    """Check if [a,b]=[b,c]=[a,c]."""
    lab = lcm(a, b)
    lbc = lcm(b, c)
    lac = lcm(a, c)
    return lab == lbc == lac


def analyze_bad_triples(N):
    """Find all bad triples in {1,...,N}."""
    bad_triples = []
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            for c in range(b+1, N+1):
                if is_bad_triple(a, b, c):
                    bad_triples.append((a, b, c, lcm(a, b)))
    return bad_triples


def classify_numbers(N):
    """Classify numbers by their prime factorization structure."""
    classes = defaultdict(list)
    for n in range(1, N+1):
        pf = prime_factors(n)
        # Classify by number of distinct prime factors
        num_primes = len(pf)
        # Classify by total number of prime factors (with multiplicity)
        total_factors = sum(pf.values())
        # Classify by whether it's a prime power
        is_prime_power = len(pf) == 1
        # Classify by whether it's squarefree
        is_squarefree = all(e == 1 for e in pf.values())

        classes[(num_primes, is_prime_power, is_squarefree)].append(n)

    return classes


def find_valid_set_via_independent_set(N):
    """
    Model as independent set problem:
    - Create graph where vertices are numbers 1..N
    - Connect two numbers if they form a bad triple with some third number
    - Find maximum independent set
    """
    # First, find all bad triples
    bad_triples = analyze_bad_triples(N)
    print(f"Found {len(bad_triples)} bad triples")

    # Create a graph where we connect numbers that appear together in bad triples
    # Actually, we need a 3-uniform hypergraph
    # For now, let's just use a greedy approach

    # Greedy: add numbers that don't create bad triples
    result = []
    for x in range(1, N+1):
        # Check if adding x creates any bad triple
        creates_bad = False
        for i, item in enumerate(result):
            for j in range(i+1, len(result)):
                if is_bad_triple(item, result[j], x):
                    creates_bad = True
                    break
            if creates_bad:
                break
        if not creates_bad:
            result.append(x)

    return result


def analyze_prime_power_sets(N):
    """Analyze sets of prime powers."""
    # Group numbers by their prime base
    prime_powers = defaultdict(list)
    for n in range(1, N+1):
        pf = prime_factors(n)
        if len(pf) == 1:
            p = list(pf.keys())[0]
            prime_powers[p].append(n)

    print(f"\nPrime power sets:")
    for p in sorted(prime_powers.keys()):
        powers = prime_powers[p]
        print(f"  Prime {p}: {len(powers)} powers: {powers[:10]}{'...' if len(powers) > 10 else ''}")

    # Any set of prime powers with the same base is valid
    # (since [p^i, p^j] = p^{max(i,j)}, and for i<j<k, [p^i,p^j]=p^j ≠ p^k=[p^j,p^k])
    # So we can take all prime powers!
    all_prime_powers = []
    for p, powers in prime_powers.items():
        all_prime_powers.extend(powers)

    print(f"\nTotal prime powers: {len(all_prime_powers)}")
    return sorted(all_prime_powers)


def analyze_squarefree_sets(N):
    """Analyze sets of squarefree numbers."""
    squarefree = []
    for n in range(1, N+1):
        pf = prime_factors(n)
        if all(e == 1 for e in pf.values()):
            squarefree.append(n)

    print(f"\nSquarefree numbers: {len(squarefree)}")

    # For squarefree numbers, [a,b] = a*b/gcd(a,b)
    # The condition [a,b]=[b,c]=[a,c] is equivalent to:
    # a*b/gcd(a,b) = b*c/gcd(b,c) = a*c/gcd(a,c)

    # Let's check which squarefree numbers can be together
    # Greedy approach
    result = []
    for x in squarefree:
        test = result + [x]
        valid = True
        for i, item in enumerate(test):
            for j in range(i+1, len(test)):
                for k in range(j+1, len(test)):
                    if is_bad_triple(item, test[j], test[k]):
                        valid = False
                        break
                if not valid:
                    break
            if not valid:
                break
        if valid:
            result.append(x)

    print(f"Greedy squarefree set: {len(result)}")
    return result


def analyze_multiples_of_primes(N):
    """Analyze sets based on multiples of primes."""
    # Key insight: if all elements are multiples of a fixed prime p,
    # then for any three elements a,b,c, we have p|a, p|b, p|c
    # But this doesn't directly prevent [a,b]=[b,c]=[a,c]

    # Let's try: take all numbers divisible by primes from a specific set
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    # Try: numbers divisible by at least one of the first k primes
    for k in range(1, 6):
        prime_set = primes[:k]
        candidates = []
        for n in range(1, N+1):
            if any(n % p == 0 for p in prime_set):
                candidates.append(n)

        # Greedy selection
        result = []
        for x in candidates:
            test = result + [x]
            valid = True
            for i, item in enumerate(test):
                for j in range(i+1, len(test)):
                    for l in range(j+1, len(test)):
                        if is_bad_triple(item, test[j], test[l]):
                            valid = False
                            break
                    if not valid:
                        break
                if not valid:
                    break
            if valid:
                result.append(x)

        print(f"  First {k} primes: {len(result)} elements")


if __name__ == "__main__":
    N = 100

    print("=== Bad Triples Analysis ===")
    bad = analyze_bad_triples(30)
    print(f"Bad triples in [1,30]: {len(bad)}")
    for t in bad[:
        20]:
        print(f"  {t}")

    print("\n=== Prime Power Analysis ===")
    pp = analyze_prime_power_sets(N)

    print("\n=== Squarefree Analysis ===")
    sf = analyze_squarefree_sets(N)

    print("\n=== Multiples of Primes ===")
    analyze_multiples_of_primes(N)

    print("\n=== Greedy Valid Set ===")
    valid = find_valid_set_via_independent_set(N)
    print(f"Size: {len(valid)}")
    print(f"Set: {valid}")
