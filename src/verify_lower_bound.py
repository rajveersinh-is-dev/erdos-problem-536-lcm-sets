"""
Verify the new lower bound: f(N) >= N/2 + log_2(N) - 1.

Construction: Take X = {1, 2, 4, 8, ...} (powers of 2) and
A = X union {floor(N/2)+1, ..., N}.
"""

from math import gcd, log2


def lcm(a, b):
    return a * gcd(a, b) // gcd(a, b)  # Fix: should be a * b // gcd(a, b)


def lcm(a, b):
    return a * b // gcd(a, b)


def is_valid_set(A):
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


def construct_set(N):
    """Construct the set X union (N/2, N] where X is powers of 2."""
    # X = powers of 2 up to N/2
    X = []
    power = 1
    while power <= N // 2:
        X.append(power)
        power *= 2

    # A = X union (N/2, N]
    A = set(X)
    for x in range(N // 2 + 1, N + 1):
        A.add(x)

    return sorted(A)


def verify_theorem(N):
    """Verify Theorem 1 and Theorem 2 for given N."""
    # Theorem 1: (N/2, N] is valid
    A1 = list(range(N // 2 + 1, N + 1))
    valid1 = is_valid_set(A1)

    # Theorem 2: X union (N/2, N] is valid
    A2 = construct_set(N)
    valid2 = is_valid_set(A2)

    # Check the bound
    bound = N // 2 + int(log2(N)) - 1

    print(f"N = {N}")
    print(f"  Theorem 1: (N/2, N] valid = {valid1}, size = {len(A1)}")
    print(f"  Theorem 2: X union (N/2, N] valid = {valid2}, size = {len(A2)}")
    print(f"  Predicted bound: {bound}")
    print(f"  Actual size: {len(A2)}")
    print(f"  Bound satisfied: {len(A2) >= bound}")

    return valid1 and valid2 and len(A2) >= bound


if __name__ == "__main__":
    print("Verifying the new lower bound f(N) >= N/2 + log_2(N) - 1")
    print("=" * 60)

    all_passed = True
    for N in [10, 20, 50, 100, 200, 500, 1000, 2000]:
        passed = verify_theorem(N)
        all_passed = all_passed and passed
        print()

    print("=" * 60)
    if all_passed:
        print("[OK] All tests passed! The lower bound is verified.")
    else:
        print("[FAIL] Some tests failed!")
