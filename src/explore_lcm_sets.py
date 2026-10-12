"""
Explore Erdős Problem #536: Sets with no three distinct elements
having equal pairwise LCMs.

We want to find the maximum size of A ⊆ {1,...,N} such that
there are no distinct a,b,c ∈ A with [a,b] = [b,c] = [a,c].
"""

from math import gcd
from itertools import combinations
from functools import lru_cache


def lcm(a, b):
    """Compute least common multiple."""
    return a * b // gcd(a, b)


def has_bad_triple(A):
    """Check if set A contains distinct a,b,c with [a,b]=[b,c]=[a,c]."""
    A_list = sorted(A)
    n = len(A_list)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a, b, c = A_list[i], A_list[j], A_list[k]
                lab = lcm(a, b)
                lbc = lcm(b, c)
                lac = lcm(a, c)
                if lab == lbc == lac:
                    return True, (a, b, c, lab)
    return False, None


def is_valid_set(A):
    """Check if A has no bad triples."""
    bad, _ = has_bad_triple(A)
    return not bad


def find_max_set_bruteforce(N):
    """Find maximum valid subset of {1,...,N} by brute force."""
    from itertools import combinations

    # Try sizes from large to small
    for size in range(N, 0, -1):
        print(f"  Trying size {size}...")
        for subset in combinations(range(1, N+1), size):
            if is_valid_set(subset):
                return list(subset)
    return []


def find_max_set_greedy(N):
    """Greedy construction of a valid set."""
    result = []
    for x in range(1, N+1):
        # Try adding x
        test = result + [x]
        if is_valid_set(test):
            result.append(x)
    return result


def find_max_set_smart(N):
    """Smarter construction using structural insights."""
    # Key insight: if a,b,c all divide L and [a,b]=[b,c]=[a,c]=L,
    # then L is the LCM of all three, and each pair has LCM = L.
    # This means for each pair, one element must contain all prime factors
    # of L that the other doesn't.

    # Strategy: use numbers with specific prime factor structures
    result = []
    for x in range(1, N+1):
        test = result + [x]
        if is_valid_set(test):
            result.append(x)
    return result


def analyze_structure(N):
    """Analyze the structure of valid sets."""
    print(f"\n=== Analysis for N={N} ===")

    # Find a large valid set
    S = find_max_set_greedy(N)
    print(f"Greedy construction: |S| = {len(S)}")
    print(f"Set: {S[:50]}{'...' if len(S) > 50 else ''}")

    # Check which numbers are excluded and why
    excluded = [x for x in range(1, N+1) if x not in S]
    print(f"Excluded numbers: {len(excluded)}")

    # Analyze prime factorizations
    from collections import Counter
    prime_counts = Counter()
    for x in S:
        # Count prime factors
        temp = x
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                prime_counts[d] += 1
                temp //= d
            d += 1
        if temp > 1:
            prime_counts[temp] += 1

    print(f"Prime factor distribution: {dict(prime_counts.most_common(10))}")

    return S


if __name__ == "__main__":
    for N in [10, 20, 30, 50, 100]:
        analyze_structure(N)
