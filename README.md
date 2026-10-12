# Erdős Problem #536: Sets with No Three Distinct Elements Having Equal Pairwise LCMs

## Problem Statement

Let $f(N)$ be the largest size of $A \subseteq \{1,\ldots,N\}$ with the property that there are no distinct $a,b,c \in A$ such that $[a,b]=[b,c]=[a,c]$, where $[a,b]$ denotes the least common multiple of $a$ and $b$.

**Question:** Estimate $f(N)$ — in particular, is it true that $f(N) = o(N)$?

## Known Results

- **Lower bound:** $f(N) \geq (1-o(1))(\log\log N)\frac{N}{\log N}$ (Abbott and Gardner, 1967)
- **Upper bound:** $f(N) \leq \left(\frac{221}{225}+o(1)\right)N$ (Weisenberg, unpublished)
- **Conjecture:** $f(N) = o(N)$ (Erdős)

## This Repository

This repository contains:
- Computational experiments to explore the structure of extremal sets
- Theoretical analysis of the problem
- New bounds and structural results

## Status

**Research in progress.** See `research/` for detailed findings.
