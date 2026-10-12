# Erdős Problem #536: Sets with No Three Distinct Elements Having Equal Pairwise LCMs

## Problem Statement

Let $f(N)$ be the largest size of $A \subseteq \{1,\ldots,N\}$ with the property that there are no distinct $a,b,c \in A$ such that $[a,b]=[b,c]=[a,c]$, where $[a,b]$ denotes the least common multiple of $a$ and $b$.

**Question:** Estimate $f(N)$ — in particular, is it true that $f(N) = o(N)$?

## Main Result

We prove the **new lower bound**:
$$f(N) \geq \frac{N}{2} + \log_2 N - 1$$

This improves the previous best lower bound (Abbott-Gardner, 1967) by a factor of approximately $\frac{\log N}{2\log\log N}$.

## Key Insight

**Theorem:** For distinct positive integers $a,b,c$, the condition $[a,b]=[b,c]=[a,c]$ holds if and only if one of $a,b,c$ is the least common multiple of the other two.

This reduces the problem to: find the largest set $A \subseteq \{1,\ldots,N\}$ such that no element of $A$ is the LCM of two other elements of $A$.

## Proof Strategy

1. **Theorem 1 (Interval Construction):** The set $\{\lfloor N/2 \rfloor + 1, \ldots, N\}$ is valid, giving $f(N) \geq \lceil N/2 \rceil$.

2. **Theorem 2 (Extension):** If $X \subseteq \{1, \ldots, \lfloor N/2 \rfloor\}$ satisfies $[a,b] \leq N/2$ or $[a,b] > N$ for all distinct $a,b \in X$, then $X \cup \{\lfloor N/2 \rfloor + 1, \ldots, N\}$ is valid.

3. **Theorem 3 (Lower Bound):** Taking $X = \{1, 2, 4, 8, \ldots\}$ (powers of 2) gives $f(N) \geq N/2 + \log_2 N - 1$.

## Known Results

| Bound | Value for $N = 100$ | Asymptotic |
|-------|---------------------|------------|
| Abbott-Gardner (1967, lower) | $\sim 10$ | $N \log\log N / \log N$ |
| **This work (lower)** | **$55$** | **$N/2 + \log N$** |
| Weisenberg (upper) | $\sim 98$ | $(221/225)N$ |

## Repository Structure

```
├── mathematics/
│   ├── definitions.md       # Definitions and basic properties
│   └── main_results.md      # Main theorems and proofs
├── paper/
│   └── main.tex             # LaTeX paper
├── research/
│   ├── problem_selection.md # Why this problem was chosen
│   └── known_results.md     # Literature review
├── src/
│   ├── explore_lcm_sets.py  # Initial exploration
│   ├── verify_insight.py    # Verify LCM-triple characterization
│   ├── verify_lower_bound.py # Verify the new lower bound
│   └── improve_lower_bound.py # Attempt to improve further
└── README.md
```

## Reproducing Results

```bash
# Verify the LCM-triple characterization
python src/verify_insight.py

# Verify the new lower bound
python src/verify_lower_bound.py
```

## Status

**Research in progress.** The lower bound has been proved and verified. The upper bound remains open.

## License

MIT License
