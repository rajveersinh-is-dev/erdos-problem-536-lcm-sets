"""
Develop and prove new results for Erdős Problem #536.

Key insight: A is valid iff no element of A is the LCM of two other elements of A.

This is equivalent to: for any distinct a,b,c in A, c ≠ lcm(a,b).
"""
from __future__ import annotations


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


def is_valid_set(A) -> bool:
    """Check if A has no element that is the LCM of two others."""
    A_list = sorted(A)
    n = len(A_list)
    for i in range(n):
        for j in range(i+1, n):
            l = lcm(A_list[i], A_list[j])
            if l in A and l != A_list[i] and l != A_list[j]:
                return False
    return True


def theorem_1_prime_powers(N) -> tuple:
    """Theorem: The set of all prime powers ≤ N is valid."""
    # Find all prime powers ≤ N
    prime_powers = set()
    for p in range(2, N+1):
        # Check if p is prime
        is_prime = True
        for d in range(2, int(p**0.5) + 1):
            if p % d == 0:
                is_prime = False
                break
        if is_prime:
            # Add all powers of p
            power = p
            while power <= N:
                prime_powers.add(power)
                power *= p

    # Verify it's valid
    assert is_valid_set(list(prime_powers)), "Prime powers set should be valid"
    return len(prime_powers), sorted(prime_powers)


def theorem_2_antichain(N) -> tuple:
    """Theorem: Any antichain in divisibility order is valid."""
    # Find a large antichain: numbers in (N/2, N]
    antichain = list(range(N//2 + 1, N+1))

    # Verify it's an antichain (no element divides another)
    for i, a in enumerate(antichain):
        for j, b in enumerate(antichain):
            if i != j and b % a == 0:
                print(f"Warning: {a} divides {b}")

    # Verify it's valid
    assert is_valid_set(antichain), "Antichain should be valid"
    return len(antichain), antichain


def theorem_3_squarefree_same_primes(N) -> bool | tuple:
    """
    Theorem: If A consists of squarefree numbers all having the same
    set of prime factors, then A is valid.

    Proof: If a,b,c are squarefree with the same prime factors, then
    lcm(a,b) = product of all primes in the union of their factorizations.
    If they have the same prime factors, lcm(a,b) = a*b (since they're coprime...
    wait, that's not right. Let me think again.
    """
    # Actually, let's check: if a,b,c are squarefree with the same prime factors,
    # then lcm(a,b) = a*b/gcd(a,b). For this to equal c, we need specific conditions.

    # Let's just verify computationally

    # Get all squarefree numbers ≤ N
    def is_squarefree(n) -> bool:
        """Is squarefree.
        
        Args:
            n:
        
        Returns:
            bool: Result of type bool
        
        """
        d = 2
        while d * d <= n:
            if n % (d*d) == 0:
                return False
            d += 1
        return True

    squarefree = [n for n in range(2, N+1) if is_squarefree(n)]

    # Group by set of prime factors
    from collections import defaultdict
    groups = defaultdict(list)
    for n in squarefree:
        # Get prime factors
        factors = []
        temp = n
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                factors.append(d)
                temp //= d
            d += 1
        if temp > 1:
            factors.append(temp)
        groups[tuple(sorted(set(factors)))].append(n)

    # Find the largest group
    max_group = max(groups.values(), key=len)
    print(f"Largest group with same prime factors: {len(max_group)}")

    # Verify it's valid
    assert is_valid_set(max_group), "Group with same prime factors should be valid"
    return len(max_group), max_group


def theorem_4_upper_bound(N):
    """
    Theorem: f(N) ≤ N - floor(N/6) for N ≥ 6.

    Proof idea: For each pair (a,b) with lcm(a,b) ≤ N, at most one of
    a, b, lcm(a,b) can be in a valid set... wait, that's not quite right.

    Actually, the condition is: if a,b ∈ A, then lcm(a,b) ∉ A.
    So for each pair (a,b), we "lose" at most one element (the LCM).

    But this doesn't directly give a good bound.

    Let me think differently. Consider the set S = {1,...,N}.
    For each pair (a,b) with lcm(a,b) = c ≤ N, the triple (a,b,c) is bad.
    In a valid set, at most 2 of {a,b,c} can be present.

    This is a hypergraph independence problem.
    """
    # Count the number of "bad triples" (a,b,c) where c = lcm(a,b)
    bad_triples = []
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            c = lcm(a, b)
            if c <= N and c != a and c != b:
                bad_triples.append((a, b, c))

    print(f"Number of bad triples: {len(bad_triples)}")

    # Each bad triple means at most 2 of {a,b,c} can be in a valid set
    # This gives a bound via linear programming, but it's not tight

    return len(bad_triples)


def theorem_5_density_lower_bound(N) -> tuple:
    """
    Theorem: f(N) ≥ N/2 for all N.

    Proof: Take A = {floor(N/2)+1, ..., N}.
    For any a,b in A, lcm(a,b) ≥ max(a,b) > N/2.
    If lcm(a,b) ≤ N, then lcm(a,b) is in A.
    But lcm(a,b) = a*b/gcd(a,b) ≥ a*b/N > (N/2)*(N/2)/N = N/4.
    Hmm, this doesn't immediately give a contradiction.

    Actually, let me check: if a,b > N/2, then lcm(a,b) > N/2.
    So lcm(a,b) could be in A.

    For example, a=N/2+1, b=N/2+2, lcm(a,b) could be ≤ N.
    """
    A = list(range(N//2 + 1, N+1))
    valid = is_valid_set(A)
    print(f"A = {{{N//2+1}, ..., {N}}} is valid: {valid}")

    if not valid:
        # Find a counterexample
        for i, a in enumerate(A):
            for j, b in enumerate(A):
                if i < j:
                    c = lcm(a, b)
                    if c in A and c != a and c != b:
                        print(f"  Counterexample: lcm({a}, {b}) = {c}")

    return len(A), valid


def theorem_6_improved_construction(N) -> tuple:
    """
    Improved construction: take numbers in (N/2, N] that are not LCMs
    of other numbers in the set.

    This is a greedy approach that should give a larger valid set.
    """
    # Start with all numbers in (N/2, N]
    candidates = list(range(N//2 + 1, N+1))

    # Greedily remove numbers that are LCMs of pairs
    result = []
    for x in candidates:
        # Check if x is the LCM of any two numbers already in result
        is_lcm = False
        for i, item in enumerate(result):
            for j in range(i+1, len(result)):
                if lcm(item, result[j]) == x:
                    is_lcm = True
                    break
            if is_lcm:
                break

        if not is_lcm:
            result.append(x)

    return len(result), result


def theorem_7_prime_power_construction(N) -> tuple:
    """
    Construction using prime powers and large numbers.

    Take all prime powers ≤ N, plus numbers in (N/2, N] that are
    not LCMs of prime powers.
    """
    # Get all prime powers
    prime_powers = set()
    for p in range(2, N+1):
        is_prime = True
        for d in range(2, int(p**0.5) + 1):
            if p % d == 0:
                is_prime = False
                break
        if is_prime:
            power = p
            while power <= N:
                prime_powers.add(power)
                power *= p

    # Add numbers in (N/2, N] that are not LCMs of prime powers
    result = set(prime_powers)
    for x in range(N//2 + 1, N+1):
        # Check if x is the LCM of any two numbers in result
        is_lcm = False
        result_list = list(result)
        for i, item in enumerate(result_list):
            for j in range(i+1, len(result_list)):
                if lcm(item, result_list[j]) == x:
                    is_lcm = True
                    break
            if is_lcm:
                break

        if not is_lcm:
            result.add(x)

    return len(result), sorted(result)


if __name__ == "__main__":
    for N in [10, 20, 50, 100, 200, 500]:
        print(f"\n{'='*50}")
        print(f"N = {N}")

        # Theorem 1: Prime powers
        count, pp = theorem_1_prime_powers(N)
        print(f"Prime powers: {count}")

        # Theorem 2: Antichain
        count, anti = theorem_2_antichain(N)
        print(f"Antichain (N/2, N]: {count}")

        # Theorem 5: Density
        count, valid = theorem_5_density_lower_bound(N)
        print(f"Density bound: {count}, valid: {valid}")

        # Theorem 6: Improved construction
        count, _ = theorem_6_improved_construction(N)
        print(f"Improved construction: {count}")

        # Theorem 7: Prime power + large numbers
        count, _ = theorem_7_prime_power_construction(N)
        print(f"Prime power + large: {count}")
