"""
Verify the key insight: [a,b]=[b,c]=[a,c] iff one element is the LCM of the other two.

This would mean: (a,b,c) is a bad triple iff c = lcm(a,b) or a = lcm(b,c) or b = lcm(a,c).
"""

from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def is_bad_triple(a, b, c):
    """Check if [a,b]=[b,c]=[a,c]."""
    lab = lcm(a, b)
    lbc = lcm(b, c)
    lac = lcm(a, c)
    return lab == lbc == lac


def is_lcm_triple(a, b, c):
    """Check if one element is the LCM of the other two."""
    return (c == lcm(a, b)) or (a == lcm(b, c)) or (b == lcm(a, c))


def verify_insight(N):
    """Verify the insight for all triples in [1,N]."""
    mismatches = []
    bad_count = 0
    lcm_count = 0

    for a in range(1, N+1):
        for b in range(a+1, N+1):
            for c in range(b+1, N+1):
                bad = is_bad_triple(a, b, c)
                lcm_trip = is_lcm_triple(a, b, c)

                if bad:
                    bad_count += 1
                if lcm_trip:
                    lcm_count += 1

                if bad != lcm_trip:
                    mismatches.append((a, b, c, bad, lcm_trip))

    print(f"N = {N}")
    print(f"Bad triples: {bad_count}")
    print(f"LCM triples: {lcm_count}")
    print(f"Mismatches: {len(mismatches)}")

    if mismatches:
        print("Mismatches found:")
        for m in mismatches[:20]:
            print(f"  {m}")
    else:
        print("[OK] Insight verified: bad triples = LCM triples")

    return len(mismatches) == 0


def analyze_lcm_characterization(N):
    """Analyze what the LCM condition means structurally."""
    print(f"\n=== LCM Characterization for N={N} ===")

    # For each number, find which pairs have it as their LCM
    lcm_pairs = {}
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            l = lcm(a, b)
            if l <= N:
                if l not in lcm_pairs:
                    lcm_pairs[l] = []
                lcm_pairs[l].append((a, b))

    print(f"Numbers that are LCMs of pairs: {len(lcm_pairs)}")

    # For each such number, count how many pairs have it as LCM
    counts = [(l, len(pairs)) for l, pairs in lcm_pairs.items()]
    counts.sort(key=lambda x: -x[1])

    print("\nTop 20 numbers with most pairs having them as LCM:")
    for l, count in counts[:20]:
        print(f"  {l}: {count} pairs")

    return lcm_pairs


def find_max_set_avoiding_lcm(N):
    """
    Find maximum set where no element is the LCM of two others.

    This is equivalent to: for any distinct a,b,c in the set,
    c ≠ lcm(a,b).
    """
    # Greedy approach
    result = []
    for x in range(1, N+1):
        # Check if x is the LCM of any two elements in result
        is_lcm_of_pair = False
        for i in range(len(result)):
            for j in range(i+1, len(result)):
                if lcm(result[i], result[j]) == x:
                    is_lcm_of_pair = True
                    break
            if is_lcm_of_pair:
                break

        # Check if any element in result is the LCM of x and another element
        creates_lcm = False
        for i in range(len(result)):
            if lcm(result[i], x) in result:
                creates_lcm = True
                break

        if not is_lcm_of_pair and not creates_lcm:
            result.append(x)

    return result


if __name__ == "__main__":
    for N in [10, 20, 30, 50, 100]:
        verify_insight(N)

    print("\n" + "="*50)
    analyze_lcm_characterization(100)

    print("\n" + "="*50)
    for N in [20, 50, 100, 200]:
        S = find_max_set_avoiding_lcm(N)
        print(f"N={N}: |S| = {len(S)}")
        if N <= 50:
            print(f"  Set: {S}")
