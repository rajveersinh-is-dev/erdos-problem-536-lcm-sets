"""
Improve the lower bound by using numbers of the form 2^i * 3^j.

Key insight: If X consists of numbers of the form 2^i * 3^j ≤ N/2,
then for any a, b ∈ X, [a,b] = 2^max(i,k) * 3^max(j,l) ≤ N/2.
So X is good, and X ∪ (N/2, N] is valid.

The number of such numbers is approximately (log_2(N/2) * log_3(N/2)) / 2.
"""
from __future__ import annotations

from math import gcd, log




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
    A_set = set(A)
    A_list = sorted(A)
    n = len(A_list)
    for i in range(n):
        for j in range(i+1, n):
            l = lcm(A_list[i], A_list[j])
            if l in A_set and l != A_list[i] and l != A_list[j]:
                return False
    return True


def construct_set_powers_of_2(N):
    """Construct X = powers of 2 up to N/2."""
    X = []
    power = 1
    while power <= N // 2:
        X.append(power)
        power *= 2
    return X


def construct_set_2_3(N):
    """Construct X = numbers of the form 2^i * 3^j up to N/2."""
    X = []
    i = 0
    while 2**i <= N // 2:
        j = 0
        while 2**i * 3**j <= N // 2:
            X.append(2**i * 3**j)
            j += 1
        i += 1
    return sorted(X)


def construct_set_2_3_5(N):
    """Construct X = numbers of the form 2^i * 3^j * 5^k up to N/2."""
    X = []
    i = 0
    while 2**i <= N // 2:
        j = 0
        while 2**i * 3**j <= N // 2:
            k = 0
            while 2**i * 3**j * 5**k <= N // 2:
                X.append(2**i * 3**j * 5**k)
                k += 1
            j += 1
        i += 1
    return sorted(X)


def verify_construction(N, X) -> tuple:
    """Verify that X ∪ (N/2, N] is valid."""
    A = set(X)
    for x in range(N // 2 + 1, N + 1):
        A.add(x)
    A = sorted(A)

    valid = is_valid_set(A)
    return valid, len(A)


if __name__ == "__main__":
    print("Improving the lower bound using numbers with more prime factors")
    print("=" * 70)

    for N in [50, 100, 200, 500, 1000, 2000, 5000]:
        print(f"\nN = {N}:")

        # Powers of 2
        X_2 = construct_set_powers_of_2(N)
        valid_2, size_2 = verify_construction(N, X_2)
        print(f"  Powers of 2: |X| = {len(X_2)}, total = {size_2}, valid = {valid_2}")

        # Numbers of form 2^i * 3^j
        X_2_3 = construct_set_2_3(N)
        valid_2_3, size_2_3 = verify_construction(N, X_2_3)
        print(f"  2^i * 3^j: |X| = {len(X_2_3)}, total = {size_2_3}, valid = {valid_2_3}")

        # Numbers of form 2^i * 3^j * 5^k
        X_2_3_5 = construct_set_2_3_5(N)
        valid_2_3_5, size_2_3_5 = verify_construction(N, X_2_3_5)
        print(f"  2^i * 3^j * 5^k: |X| = {len(X_2_3_5)}, total = {size_2_3_5}, valid = {valid_2_3_5}")

        # Asymptotic estimate
        log_N = log(N)
        estimate = (log_N)**2 / (2 * log(2) * log(3))
        print(f"  Asymptotic estimate: (log N)^2 / (2 log 2 log 3) ≈ {estimate:.1f}")
